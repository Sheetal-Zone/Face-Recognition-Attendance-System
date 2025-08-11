from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime

# login page
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Face Recognition System")
        self.root.state('zoomed')
        self.root.config(bg="#e6f2ff")

        # Main frame 
        self.main_frame = Frame(root, bg="white", bd=5, relief=RIDGE)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=900, height=500)

        # Left Frame 
        left_frame = Frame(self.main_frame, bg="white")
        left_frame.place(x=0, y=0, width=450, height=500)

    
        img1 = Image.open("back_images/img1.png")  
        img1= img1.resize((450, 500), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(left_frame, image=self.photo, bg="white")
        lbl_img1.pack()

        # Right Frame 
        right_frame = Frame(self.main_frame, bg="#e6f2ff")
        right_frame.place(x=450, y=0, width=450, height=500)

        # Title Label
        Label(right_frame, text="Login", font=("Arial Rounded MT Bold", 36, "bold"), bg="#e6f2ff", fg="#004080").pack(pady=50)

        # Variables
        self.username = StringVar()
        self.password = StringVar()

        form_frame = Frame(right_frame, bg="#e6f2ff")
        form_frame.pack(pady=20)

        # Username
        Label(form_frame, text="Username:", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#003366").grid(row=0, column=0, padx=15, pady=15, sticky=E)
        Entry(form_frame, textvariable=self.username, font=("Arial", 18), width=25, bd=3, relief=RIDGE).grid(row=0, column=1, padx=15, pady=15)

        # Password
        Label(form_frame, text="Password:", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#003366").grid(row=1, column=0, padx=15, pady=15, sticky=E)
        Entry(form_frame, textvariable=self.password, font=("Arial", 18), show="*", width=25, bd=3, relief=RIDGE).grid(row=1, column=1, padx=15, pady=15)

        # Login Button
        self.btn_login = Button(right_frame, text="Login", command=self.check_login, width=20,
                                font=("Arial Rounded MT Bold", 20), bg="#007acc", fg="white",
                                activebackground="#005999", cursor="hand2", bd=0, relief=RIDGE)
        self.btn_login.pack(pady=40)

        # Hover effect for button
        self.btn_login.bind("<Enter>", lambda e: self.btn_login.config(bg="#005999"))
        self.btn_login.bind("<Leave>", lambda e: self.btn_login.config(bg="#007acc"))

    def check_login(self):
        user = self.username.get()
        pwd = self.password.get()

        if user == "admin" and pwd == "1234":
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            open_main_window()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

# main app
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')

        # Images & Layout
        self.load_images()
        self.create_widgets()

    def load_images(self):
        # Load and store all image
        self.photoimg1 = ImageTk.PhotoImage(Image.open("back_images/img1.png").resize((500,130), Image.Resampling.LANCZOS))
        self.photoimg2 = ImageTk.PhotoImage(Image.open("back_images/img2.png").resize((500,130), Image.Resampling.LANCZOS))
        self.photoimg3 = ImageTk.PhotoImage(Image.open("back_images/img3.png").resize((530,130), Image.Resampling.LANCZOS))
        self.photoimg4 = ImageTk.PhotoImage(Image.open("back_images/img4.png").resize((1530,668), Image.Resampling.LANCZOS))
        self.photoimg5 = ImageTk.PhotoImage(Image.open("back_images/img5.png").resize((180,180), Image.Resampling.LANCZOS))
        self.photoimg6 = ImageTk.PhotoImage(Image.open("back_images/img6.png").resize((180,180), Image.Resampling.LANCZOS))
        self.photoimg7 = ImageTk.PhotoImage(Image.open("back_images/img7.png").resize((180,180), Image.Resampling.LANCZOS))
        self.photoimg11 = ImageTk.PhotoImage(Image.open("back_images/img11.png").resize((180,180), Image.Resampling.LANCZOS))
        self.photoimg8 = ImageTk.PhotoImage(Image.open("back_images/img8.png").resize((180,180), Image.Resampling.LANCZOS))
        self.photoimg9 = ImageTk.PhotoImage(Image.open("back_images/img1.png").resize((180,180), Image.Resampling.LANCZOS))
        self.photoimg10 = ImageTk.PhotoImage(Image.open("back_images/img9.png").resize((180,180), Image.Resampling.LANCZOS))
        self.photoimg12 = ImageTk.PhotoImage(Image.open("back_images/img10.png").resize((180,180), Image.Resampling.LANCZOS))

    def create_widgets(self):
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=530, height=130)

        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0, y=130, width=1530, height=668)
        bg_lbl.lower()

        title_lbl = Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("Arial Rounded MT Bold", 28,"bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Time display
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('Arial Rounded MT Bold',12,'bold'), bg='white', fg='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # Buttons
        Button(bg_lbl, image=self.photoimg5, command=self.student_details, cursor="hand2").place(x=100, y=70, width=180, height=180)
        Button(bg_lbl, text="Student Details", command=self.student_details, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=100, y=250, width=180, height=35)

        Button(bg_lbl, image=self.photoimg6, command=self.face_data, cursor="hand2").place(x=400, y=70, width=180, height=180)
        Button(bg_lbl, text="Face Detector", command=self.face_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=400, y=250, width=180, height=35)

        Button(bg_lbl, image=self.photoimg7, command=self.attendance_data, cursor="hand2").place(x=700, y=70, width=180, height=180)
        Button(bg_lbl, text="Attendance", command=self.attendance_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=700, y=250, width=180, height=35)

        Button(bg_lbl, image=self.photoimg11, command=self.help_data, cursor="hand2").place(x=1000, y=70, width=180, height=180)
        Button(bg_lbl, text="Help Desk", command=self.help_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=1000, y=250, width=180, height=35)

        Button(bg_lbl, image=self.photoimg8, command=self.train_data, cursor="hand2").place(x=100, y=330, width=180, height=180)
        Button(bg_lbl, text="Train Data", command=self.train_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=100, y=510, width=180, height=35)

        Button(bg_lbl, image=self.photoimg9, command=self.open_img, cursor="hand2").place(x=400, y=330, width=180, height=180)
        Button(bg_lbl, text="Photos", command=self.open_img, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=400, y=510, width=180, height=35)

        Button(bg_lbl, image=self.photoimg10, command=self.developer_data, cursor="hand2").place(x=700, y=330, width=180, height=180)
        Button(bg_lbl, text="Developer", command=self.developer_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=700, y=510, width=180, height=35)

        Button(bg_lbl, image=self.photoimg12, command=self.iExit, cursor="hand2").place(x=1000, y=330, width=180, height=180)
        Button(bg_lbl, text="Exit", command=self.iExit, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=1000, y=510, width=180, height=35)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        exit_confirm = messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?", parent=self.root)
        if exit_confirm:
            self.root.destroy()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


# ==================== OPEN MAIN WINDOW AFTER LOGIN ====================
def open_main_window():
    root2 = Tk()
    obj = Face_Recognition_System(root2)
    root2.mainloop()


# ==================== MAIN ====================
if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
