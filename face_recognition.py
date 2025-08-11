from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import cv2
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.state('zoomed')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.configure(bg="#f0f2f5")

        # Header 
        header_frame = Frame(self.root, bg="white", bd=4, relief=RAISED)
        header_frame.pack(side=TOP, fill=X, pady=8)
        back_btn = Button(
            header_frame, text="←", font=("Arial Rounded MT Bold", 24),
            fg="#2563eb", bg="white", bd=0, cursor="hand2",
            command=self.root.destroy
        )
        back_btn.pack(side=LEFT, padx=20)
        title_lbl = Label(
            header_frame, text="🤖 FACE RECOGNITION SYSTEM",
            font=("Arial Rounded MT Bold", 38, "bold"), bg="white", fg="#1d3557"
        )
        title_lbl.pack(pady=8)

        # Main Images
        main_frame = Frame(self.root, bg="#f0f2f5")
        main_frame.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=(10,0))
        img_left = Image.open("back_images/img1.png").resize((600, screen_height - 220), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(main_frame, image=self.photoimg_left, bd=2, relief=GROOVE).pack(side=LEFT, fill=Y, padx=(0,10))
        img_right = Image.open("back_images/img2.png").resize((screen_width - 680, screen_height - 220), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(main_frame, image=self.photoimg_right, bd=2, relief=GROOVE).pack(side=LEFT, fill=BOTH, expand=True)

        # Start Button
        bottom_frame = Frame(self.root, bg="#f0f2f5")
        bottom_frame.pack(side=BOTTOM, fill=X, pady=(10,20))
        btn = Button(
            bottom_frame, text="🚀 START FACE RECOGNITION",
            font=("Arial Rounded MT Bold", 28, "bold"),
            bg="#118ab2", fg="white",
            activebackground="#073b4c", activeforeground="white",
            cursor="hand2", bd=5, relief=RAISED,
            command=self.face_recog
        )
        btn.pack(padx=200, fill=X)

    def mark_attendance(self, i, n, d):
        filename = "attendance.csv"
        now = datetime.now()
        date_str = now.strftime('%d/%m/%Y')
        time_str = now.strftime('%H:%M:%S')

        # Write header if file doesn't exist
        if not os.path.exists(filename):
            with open(filename, 'w', newline="") as f:
                f.write("ID,Name,Department,Time,Date,Attendance\n")

        # Avoid duplicate for today
        with open(filename, "r+", newline="") as f:
            lines = f.readlines()
            existing = [line.strip().split(',') for line in lines[1:]]
            ids_today = [row[0] for row in existing if row[4]==date_str]
            if i not in ids_today:
                f.write(f"{i},{n},{d},{time_str},{date_str},Present\n")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            for (x, y, w, h) in features:
                id, predict = clf.predict(gray[y:y+h, x:x+w])
                confidence = int(100*(1 - predict/300))
                conn = mysql.connector.connect(host="localhost", username="root", password="14232239", database="face_recognizer")
                cursor = conn.cursor()

                cursor.execute(f"SELECT Name FROM student WHERE Student_id={id}")
                n = cursor.fetchone()
                n = n[0] if n else "Unknown"

                cursor.execute(f"SELECT Dep FROM student WHERE Student_id={id}")
                d = cursor.fetchone()
                d = d[0] if d else "Unknown"

                conn.close()
                i = str(id)

                if confidence>77:
                    cv2.rectangle(img, (x,y), (x+w, y+h), color, 3)
                    cv2.putText(img, f"ID:{i}", (x, y-50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                    cv2.putText(img, f"Name:{n}", (x, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                    cv2.putText(img, f"Dept:{d}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                    self.mark_attendance(i, n, d)
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
            return img

        def recognize(img, clf, faceCascade):
            return draw_boundary(img, faceCascade, 1.1, 10, (255,0,255), clf)

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret: break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition (Press q/Esc to exit)", cv2.resize(img, (800,600)))
            key = cv2.waitKey(1)
            if key in [13, ord('q'), 27]: break
        video_cap.release()
        cv2.destroyAllWindows()

        # ✅ Open attendance table after recognition:
        from attendance import Attendance
        new_window = Toplevel(self.root)
        Attendance(new_window)

if __name__ == "__main__":
    root = Tk()
    Face_Recognition(root)
    root.mainloop()
