from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import os

class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.configure(bg="#f0f2f5")
        self.root.state('zoomed')

        # === Title frame with back arrow and title centered ===
        title_frame = Frame(self.root, bg="white", relief=RAISED, bd=3)
        title_frame.pack(side=TOP, fill=X, pady=10)

        back_btn = Button(
            title_frame, text="←", font=("Arial Rounded MT Bold", 28),
            bg="white", fg="#d62828", bd=0, cursor="hand2",
            activebackground="white", activeforeground="red",
            command=self.root.destroy
        )
        back_btn.pack(side=LEFT, padx=10)

        # Hover effect
        back_btn.bind("<Enter>", lambda e: back_btn.config(fg="red"))
        back_btn.bind("<Leave>", lambda e: back_btn.config(fg="#d62828"))

        # Center the title label
        title_lbl = Label(
            title_frame, text="🛠️ TRAIN DATASET",
            font=("Arial Rounded MT Bold", 40, "bold"),
            bg="white", fg="#d62828"
        )
        title_lbl.pack(side=LEFT, expand=True, fill=X, padx=20)

        # === Main frame with images ===
        main_frame = Frame(self.root, bg="#f0f2f5")
        main_frame.pack(fill=BOTH, expand=True, padx=50, pady=(0, 20))

        img_width = (screen_width - 150) // 2
        img_height = 400

        # Left Image
        left_frame = Frame(main_frame, bg="white", bd=2, relief=RIDGE)
        left_frame.pack(side=LEFT, expand=True, fill=BOTH, padx=(0, 20))
        img_left = Image.open("back_images/img1.png").resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lbl_left = Label(left_frame, image=self.photoimg_left, bd=0)
        lbl_left.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Right Image
        right_frame = Frame(main_frame, bg="white", bd=2, relief=RIDGE)
        right_frame.pack(side=LEFT, expand=True, fill=BOTH)
        img_right = Image.open("back_images/img2.png").resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        lbl_right = Label(right_frame, image=self.photoimg_right, bd=0)
        lbl_right.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # === Rounded button at bottom ===
        btn_frame = Frame(self.root, bg="#f0f2f5")
        btn_frame.pack(side=BOTTOM, fill=X, padx=200, pady=30)

        # Since Tkinter Button has no real rounded corners, simulate by padding & color
        train_btn = Button(
            btn_frame, text="🚀 START TRAINING DATA",
            command=self.train_classifier,
            font=("Arial Rounded MT Bold", 30, "bold"),
            bg="#118ab2", fg="white",
            activebackground="#073b4c", activeforeground="white",
            relief=FLAT, bd=0, cursor="hand2",
            padx=20, pady=10, highlightthickness=0
        )
        train_btn.pack(fill=X, ipady=10, pady=5)

        # Add rounded effect by wrapping in a Frame with same bg
        train_btn.config(borderwidth=0, highlightbackground="#118ab2", highlightcolor="#118ab2")

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "⚠️ Data directory not found!")
            return

        image_paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces, ids = [], []

        for image_path in image_paths:
            try:
                img = Image.open(image_path).convert('L')
                image_np = np.array(img, 'uint8')
                id = int(os.path.split(image_path)[1].split('.')[1])
                faces.append(image_np)
                ids.append(id)
                cv2.imshow("Training (Press Enter to stop)", cv2.resize(image_np, (600, 600)))
                cv2.waitKey(1)
            except Exception as e:
                print(f"Skipping file {image_path}: {e}")

        if faces:
            ids_np = np.array(ids)
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids_np)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Success", "✅ Training completed and saved as classifier.xml!")
        else:
            messagebox.showwarning("Warning", "⚠️ No data found to train!")


if __name__ == "__main__":
    root = Tk()
    Train(root)
    root.mainloop()
