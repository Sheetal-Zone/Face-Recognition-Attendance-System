from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System - Developers")
        self.root.configure(bg="#f5f7fa")  # Soft background
        self.root.state('zoomed')

        # Header
        header = Frame(self.root, bg="#f5f7fa", height=80)
        header.pack(fill=X)

        # Back arrow button on top-left
        back_btn = Button(
            header, text="←", font=("Arial Rounded MT Bold", 24),
            fg="#2563eb", bg="#f5f7fa", bd=0, cursor="hand2",
            activebackground="#f5f7fa", activeforeground="#3b82f6",
            command=self.root.destroy
        )
        back_btn.pack(side=LEFT, padx=25, pady=10)
        back_btn.bind("<Enter>", lambda e: back_btn.config(fg="#3b82f6"))
        back_btn.bind("<Leave>", lambda e: back_btn.config(fg="#2563eb"))

        # Title
        Label(
            header, text="✨ Meet The Developers ✨",
            font=("Segoe UI", 28, "bold"), fg="#1d4ed8", bg="#f5f7fa"
        ).pack(pady=10)

        # Main Frame
        main = Frame(self.root, bg="#f5f7fa")
        main.pack(fill=BOTH, expand=True, padx=40, pady=20)

        left = Frame(main, bg="#f5f7fa")
        left.pack(side=LEFT, expand=True, fill=BOTH, padx=30)

        right = Frame(main, bg="#f5f7fa")
        right.pack(side=RIGHT, expand=True, fill=BOTH, padx=30)

        # Developer Sections
        self.dev_section(
            left, "back_images/img12.png", "Sheetal Sharma",
            "Machine Learning Engineer & AI Enthusiast",
            "✨ Passionate about building intelligent systems.\n"
            "⚙️ Skilled in Python, AI, ML, full-stack web apps.\n"
            "🚀 Developed this system to automate attendance smartly.",
            "ss8061547@gmail.com", "https://github.com/Sheetal-Zone", "https://www.linkedin.com/in/sheetal-sharma23/"
        )

        self.dev_section(
            right, "back_images/img14.jpg", "Shivam Gemini",
            "Machine Learning Engineer & AI Enthusiast",
            "🔍 Focused on real-world ML solutions.\n"
            "📊 Experience with Python, TensorFlow, data analysis.\n"
            "🤝 Co-developed this system to improve security automation.",
            "shivamgemini2004@gmail.com", "https://github.com/shivaa", "https://linkedin.com/in/shivam-gemini"
        )

    def dev_section(self, parent, img_path, name, role, bio, email, github, linkedin):
        # Process image into circle with shadow
        circle_img = self.make_circle_image(img_path, size=160)
        photo = ImageTk.PhotoImage(circle_img)

        img_lbl = Label(parent, image=photo, bg="#f5f7fa")
        img_lbl.image = photo
        img_lbl.pack(pady=15)

        # Name
        Label(
            parent, text=name, font=("Segoe UI", 20, "bold"),
            fg="#1e40af", bg="#f5f7fa"
        ).pack()

        # Role
        Label(
            parent, text=role, font=("Arial Rounded MT Bold", 13, "italic"),
            fg="#3b82f6", bg="#f5f7fa"
        ).pack(pady=6)

        # Bio
        Label(
            parent, text=bio, font=("Segoe UI", 12), fg="#374151", bg="#f5f7fa",
            wraplength=450, justify=LEFT
        ).pack(padx=10, pady=12)

        # Links
        self.link(parent, "📧", email, f"mailto:{email}")
        self.link(parent, "🐙", github, github)
        self.link(parent, "🔗", linkedin, linkedin)

    def make_circle_image(self, img_path, size=160):
        img = Image.open(img_path).resize((size, size), Image.Resampling.LANCZOS).convert("RGBA")

        # Create same size mask with circle
        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        # Apply mask to image
        img.putalpha(mask)

        # Create shadow
        shadow = Image.new('RGBA', (size+10, size+10), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.ellipse((5, 5, size+5, size+5), fill=(0,0,0,100))
        shadow = shadow.filter(ImageFilter.GaussianBlur(4))

        # Paste image on shadow
        shadow.paste(img, (5, 5), img)
        return shadow

    def link(self, parent, icon, text, url):
        frame = Frame(parent, bg="#f5f7fa")
        frame.pack(pady=4)
        Label(frame, text=icon, font=("Arial Rounded MT Bold", 13), fg="#2563eb", bg="#f5f7fa").pack(side=LEFT)
        link = Label(frame, text=text, font=("Segoe UI", 12, "underline"), fg="#2563eb", bg="#f5f7fa", cursor="hand2")
        link.pack(side=LEFT, padx=5)
        link.bind("<Enter>", lambda e: link.config(fg="#3b82f6"))
        link.bind("<Leave>", lambda e: link.config(fg="#2563eb"))
        link.bind("<Button-1>", lambda e: webbrowser.open(url))

if __name__ == "__main__":
    root = Tk()
    Developer(root)
    root.mainloop()
