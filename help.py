from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser

class Help:
    def __init__(self, root):
        self.root = root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Face Recognition System - Help Desk")
        self.root.configure(bg="#f5f7fa")

        # Title Frame
        title_frame = Frame(self.root, bg="#264653")
        title_frame.place(x=0, y=0, width=screen_width, height=70)

        # Back arrow button
        back_btn = Button(
            title_frame, text="←", font=("Arial Rounded MT Bold", 24),
            fg="#e9c46a", bg="#264653", bd=0, cursor="hand2",
            activebackground="#264653", activeforeground="#f4a261",
            command=self.root.destroy
        )
        back_btn.pack(side=LEFT, padx=20)
        back_btn.bind("<Enter>", lambda e: back_btn.config(fg="#f4a261"))
        back_btn.bind("<Leave>", lambda e: back_btn.config(fg="#e9c46a"))

        title_lbl = Label(
            title_frame,
            text="HELP DESK",
            font=("Arial Rounded MT Bold", 36, "bold"),
            bg="#264653",
            fg="#e9c46a"
        )
        title_lbl.pack(pady=5)

        # Background Image
        img_top = Image.open("back_images/img8.png")
        img_top = img_top.resize((screen_width, screen_height - 70), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_lbl = Label(self.root, image=self.photoimg_top)
        bg_lbl.place(x=0, y=70, width=screen_width, height=screen_height - 70)

        # Overlay Frame
        overlay_frame = Frame(bg_lbl, bg="white", bd=3, relief=RIDGE)
        overlay_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=700, height=400)

        # Contact Info Section
        contact_title = Label(
            overlay_frame,
            text="Contact Information",
            font=("Arial Rounded MT Bold", 22, "bold"),
            fg="#264653",
            bg="white"
        )
        contact_title.pack(pady=(10, 15))

        # Email
        email_label = Label(
            overlay_frame,
            text="📧 Email: ",
            font=("Helvetica", 16, "bold"),
            fg="#2a9d8f",
            bg="white"
        )
        email_label.pack(anchor="w", padx=20)
        email_link = Label(
            overlay_frame,
            text="ss8061547@gmail.com",
            font=("Helvetica", 16),
            fg="#1d3557",
            bg="white", cursor="hand2"
        )
        email_link.pack(anchor="w", padx=40)
        email_link.bind("<Button-1>", lambda e: webbrowser.open("mailto:ss8061547@gmail.com"))

        # Phone
        phone_label = Label(
            overlay_frame,
            text="📞 Phone: ",
            font=("Helvetica", 16, "bold"),
            fg="#2a9d8f",
            bg="white"
        )
        phone_label.pack(anchor="w", padx=20, pady=(10,0))
        phone_num = Label(
            overlay_frame,
            text="+91-7006348852",
            font=("Helvetica", 16),
            fg="#1d3557",
            bg="white"
        )
        phone_num.pack(anchor="w", padx=40)

        # GitHub
        github_label = Label(
            overlay_frame,
            text="🐙 GitHub: ",
            font=("Helvetica", 16, "bold"),
            fg="#2a9d8f",
            bg="white"
        )
        github_label.pack(anchor="w", padx=20, pady=(10,0))
        github_link = Label(
            overlay_frame,
            text="https://github.com/Sheetal-Zone",
            font=("Helvetica", 16, "underline"),
            fg="#1d3557",
            bg="white", cursor="hand2"
        )
        github_link.pack(anchor="w", padx=40)
        github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Sheetal-Zone"))

        # Help/FAQ Section
        faq_title = Label(
            overlay_frame,
            text="FAQs / Help",
            font=("Arial Rounded MT Bold", 20, "bold"),
            fg="#264653",
            bg="white"
        )
        faq_title.pack(pady=(20, 10))

        # Text box with scrollbar
        help_text_frame = Frame(overlay_frame, bg="white")
        help_text_frame.pack(fill=BOTH, expand=True, padx=20)

        scrollbar = Scrollbar(help_text_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        help_text = Text(
            help_text_frame,
            wrap=WORD,
            font=("Helvetica", 14),
            bg="#f7f9fa",
            fg="#333333",
            yscrollcommand=scrollbar.set,
            relief=RIDGE,
            bd=2
        )
        help_text.pack(fill=BOTH, expand=True)
        scrollbar.config(command=help_text.yview)

        help_content = """
Welcome to the Face Recognition System Help Desk!

• How to register new users?
  - Use the 'Register' module to add student details and capture face data.

• How to train the system?
  - Use the 'Train Data' button to train the face recognizer on collected data.

• How to perform face recognition?
  - Click on 'Start Face Recognition' and look into the camera.

• Troubleshooting:
  - Ensure your webcam is connected and accessible.
  - Check the database connection settings.
  - Verify all required files (haarcascade, classifier.xml) are present.

For further assistance, contact us via email or phone.
        """
        help_text.insert(END, help_content)
        help_text.config(state=DISABLED)  # Make read-only

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
