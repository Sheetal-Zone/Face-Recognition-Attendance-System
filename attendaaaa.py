# ##from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import os
# import csv
# from datetime import datetime

# mydata = []  # global list to store csv data

# class Attendance:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Attendance Management System")
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()
#         self.root.geometry(f"{screen_width}x{screen_height}+0+0")

#         # ============== Variables ==============
#         self.var_atten_id = StringVar()
#         self.var_atten_name = StringVar()
#         self.var_atten_dep = StringVar()
#         self.var_atten_time = StringVar()
#         self.var_atten_date = StringVar()
#         self.var_atten_attendance = StringVar()

#         self.var_search = StringVar()  # Search text variable

#         # ============== Top Banner Images ==============
#         img_top_left = Image.open("back_images/img1.png").resize((screen_width//2, 140), Image.Resampling.LANCZOS)
#         self.photo_top_left = ImageTk.PhotoImage(img_top_left)
#         lbl_top_left = Label(self.root, image=self.photo_top_left)
#         lbl_top_left.place(x=0, y=0, width=screen_width//2, height=140)

#         img_top_right = Image.open("back_images/img1.png").resize((screen_width//2, 140), Image.Resampling.LANCZOS)
#         self.photo_top_right = ImageTk.PhotoImage(img_top_right)
#         lbl_top_right = Label(self.root, image=self.photo_top_right)
#         lbl_top_right.place(x=screen_width//2, y=0, width=screen_width//2, height=140)

#         # ============== Background Image ==============
#         img_bg = Image.open("back_images/img1.png").resize((screen_width, screen_height - 140), Image.Resampling.LANCZOS)
#         self.photo_bg = ImageTk.PhotoImage(img_bg)
#         lbl_bg = Label(self.root, image=self.photo_bg)
#         lbl_bg.place(x=0, y=140, width=screen_width, height=screen_height - 140)

#         # ============== Title ==============
#         title_lbl = Label(lbl_bg, text="ATTENDANCE MANAGEMENT SYSTEM",
#                           font=("Arial Rounded MT Bold", 32, "bold"), bg="white", fg="green")
#         title_lbl.place(x=0, y=0, width=screen_width, height=50)

#         # ============== Main Frame ==============
#         main_frame_height = screen_height - 240
#         main_frame = Frame(lbl_bg, bd=2, bg="white")
#         main_frame.place(x=20, y=60, width=screen_width - 40, height=main_frame_height)

#         # ============== Left Frame ==============
#         left_frame_width = (screen_width - 80) // 2
#         left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
#                                 font=("Arial Rounded MT Bold", 14, "bold"))
#         left_frame.place(x=10, y=10, width=left_frame_width, height=main_frame_height - 20)

#         img_left = Image.open("back_images/img4.png").resize((700, 130), Image.Resampling.LANCZOS)
#         self.photo_left = ImageTk.PhotoImage(img_left)
#         lbl_left = Label(left_frame, image=self.photo_left)
#         lbl_left.place(x=5, y=0, width=700, height=130)

#         left_inner = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
#         left_inner.place(x=0, y=135, width=720, height=380)

#         lbl_font = ("times new roman", 13, "bold")

#         Label(left_inner, text="Attendance ID:", font=lbl_font, bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
#         ttk.Entry(left_inner, textvariable=self.var_atten_id, width=15, font=lbl_font).grid(row=0, column=1, padx=10, pady=5, sticky=W)

#         Label(left_inner, text="Name:", font=lbl_font, bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
#         ttk.Entry(left_inner, textvariable=self.var_atten_name, width=15, font=lbl_font).grid(row=1, column=1, padx=10, pady=5, sticky=W)

#         Label(left_inner, text="Department:", font=lbl_font, bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
#         ttk.Entry(left_inner, textvariable=self.var_atten_dep, width=15, font=lbl_font).grid(row=1, column=3, padx=10, pady=5, sticky=W)

#         Label(left_inner, text="Time:", font=lbl_font, bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
#         ttk.Entry(left_inner, textvariable=self.var_atten_time, width=15, font=lbl_font).grid(row=2, column=1, padx=10, pady=5, sticky=W)

#         Label(left_inner, text="Date:", font=lbl_font, bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
#         ttk.Entry(left_inner, textvariable=self.var_atten_date, width=15, font=lbl_font).grid(row=2, column=3, padx=10, pady=5, sticky=W)

#         Label(left_inner, text="Attendance:", font=lbl_font, bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
#         self.atten_status = ttk.Combobox(left_inner, textvariable=self.var_atten_attendance, width=15, font=lbl_font, state="readonly")
#         self.atten_status["values"] = ("Status", "Present", "Absent")
#         self.atten_status.current(0)
#         self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)

#         btn_frame = Frame(left_inner, bd=2, relief=RIDGE)
#         btn_frame.place(x=0, y=250, width=700, height=40)

#         Button(btn_frame, text="Add", command=self.add_attendance, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=0)
#         Button(btn_frame, text="Import CSV", command=self.importCsv, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=1)
#         Button(btn_frame, text="Export CSV", command=self.exportCsv, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=2)
#         Button(btn_frame, text="Update", command=self.update_data, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=3)
#         Button(btn_frame, text="Reset", command=self.reset_data, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=4)

#         # ============== Right Frame ==============
#         right_frame_width = (screen_width - 80)//2 - 30
#         right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details",
#                                  font=("Arial Rounded MT Bold", 14, "bold"))
#         right_frame.place(x=left_frame_width + 30, y=10, width=right_frame_width, height=main_frame_height - 20)

#         # ============== Search Bar ==============
#         search_frame = Frame(right_frame, bd=2, relief=RIDGE)
#         search_frame.pack(fill=X, padx=5, pady=5)

#         lbl_search = Label(search_frame, text="Search (ID, Name, Department):", font=lbl_font)
#         lbl_search.pack(side=LEFT, padx=5)

#         self.search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=30, font=lbl_font)
#         self.search_entry.pack(side=LEFT, padx=5)
#         self.search_entry.bind("<KeyRelease>", self.search_data)  # Call search on key release

#         btn_search = Button(search_frame, text="Search", command=self.search_data, font=lbl_font, bg="green", fg="white")
#         btn_search.pack(side=LEFT, padx=5)

#         btn_clear_search = Button(search_frame, text="Clear", command=self.clear_search, font=lbl_font, bg="red", fg="white")
#         btn_clear_search.pack(side=LEFT, padx=5)

#         table_frame = Frame(right_frame, bd=2, relief=RIDGE)
#         table_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.AttendanceReportTable = ttk.Treeview(table_frame,
#                                                   columns=("id", "name", "department", "time", "date", "attendance"),
#                                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.AttendanceReportTable.xview)
#         scroll_y.config(command=self.AttendanceReportTable.yview)

#         for col in ("id", "name", "department", "time", "date", "attendance"):
#             self.AttendanceReportTable.heading(col, text=col.capitalize())
#             self.AttendanceReportTable.column(col, width=140)

#         self.AttendanceReportTable["show"] = "headings"
#         self.AttendanceReportTable.pack(fill=BOTH, expand=1)
#         self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

#         self.auto_fill_datetime()
#         self.importCsv()
#         self.fetch_today_attendance()   # initial load

#     # ============== Methods ==============

#     def auto_fill_datetime(self):
#         now = datetime.now()
#         self.var_atten_time.set(now.strftime("%H:%M:%S"))
#         self.var_atten_date.set(now.strftime("%d/%m/%Y"))

#     def is_duplicate_attendance(self, student_id, date):
#         for row in mydata:
#             if row[0] == student_id and row[4] == date:
#                 return True
#         return False

#     def add_attendance(self):
#         new_data = (
#             self.var_atten_id.get().strip(),
#             self.var_atten_name.get().strip(),
#             self.var_atten_dep.get().strip(),
#             self.var_atten_time.get().strip(),
#             self.var_atten_date.get().strip(),
#             self.var_atten_attendance.get().strip()
#         )
#         if "" in new_data or new_data[5] == "Status":
#             messagebox.showerror("Error", "All fields must be filled correctly!")
#             return
#         if self.is_duplicate_attendance(new_data[0], new_data[4]):
#             messagebox.showerror("Error", "Attendance already marked for this student on this date!")
#             return
#         mydata.append(new_data)
#         self.save_to_csv()
#         messagebox.showinfo("Success", "Attendance added successfully!")
#         self.fetch_today_attendance()
#         self.reset_data()

#     def importCsv(self):
#         global mydata
#         mydata.clear()
#         filename = "attendance.csv"
#         if os.path.exists(filename):
#             with open(filename, newline="", encoding="utf-8") as myFile:
#                 csvreader = csv.reader(myFile)
#                 next(csvreader, None)  # skip header if exists
#                 for row in csvreader:
#                     if len(row) == 6:
#                         mydata.append(row)
#         else:
#             # Create empty csv with header if not exists
#             with open(filename, mode="w", newline="", encoding="utf-8") as f:
#                 writer = csv.writer(f)
#                 writer.writerow(["ID", "Name", "Department", "Time", "Date", "Attendance"])
#         self.fetch_today_attendance()

#     def save_to_csv(self):
#         filename = "attendance.csv"
#         with open(filename, mode="w", newline="", encoding="utf-8") as myFile:
#             writer = csv.writer(myFile)
#             writer.writerow(["ID", "Name", "Department", "Time", "Date", "Attendance"])
#             for row in mydata:
#                 writer.writerow(row)

#     def fetch_today_attendance(self):
#         today = datetime.now().strftime("%d/%m/%Y")
#         today_data = [row for row in mydata if row[4] == today]
#         self.fetchData(today_data)

#     def update_data(self):
#         selected = self.AttendanceReportTable.focus()
#         if not selected:
#             messagebox.showerror("Error", "No row selected to update!")
#             return
#         updated_data = (
#             self.var_atten_id.get().strip(),
#             self.var_atten_name.get().strip(),
#             self.var_atten_dep.get().strip(),
#             self.var_atten_time.get().strip(),
#             self.var_atten_date.get().strip(),
#             self.var_atten_attendance.get().strip()
#         )
#         if self.is_duplicate_attendance(updated_data[0], updated_data[4]):
#             selected_data = self.AttendanceReportTable.item(selected, "values")
#             if not (selected_data[0] == updated_data[0] and selected_data[4] == updated_data[4]):
#                 messagebox.showerror("Error", "Attendance already marked for this student on this date!")
#                 return
#         self.AttendanceReportTable.item(selected, values=updated_data)
#         for idx, row in enumerate(mydata):
#             if row[0] == updated_data[0] and row[4] == updated_data[4]:
#                 mydata[idx] = updated_data
#                 break
#         self.save_to_csv()
#         messagebox.showinfo("Success", "Record updated successfully!")
#         self.fetch_today_attendance()

#     def exportCsv(self):
#         if len(mydata) < 1:
#             messagebox.showerror("No Data", "No data found to export!")
#             return
#         filename = "exported_attendance.csv"
#         with open(filename, mode="w", newline="", encoding="utf-8") as myFile:
#             exp_write = csv.writer(myFile)
#             exp_write.writerow(["ID", "Name", "Department", "Time", "Date", "Attendance"])
#             for row in mydata:
#                 exp_write.writerow(row)
#         messagebox.showinfo("Data Exported", f"Data exported successfully to {os.path.abspath(filename)}")

#     def reset_data(self):
#         self.var_atten_id.set("")
#         self.var_atten_name.set("")
#         self.var_atten_dep.set("")
#         self.var_atten_time.set("")
#         self.var_atten_date.set("")
#         self.var_atten_attendance.set("Status")
#         self.auto_fill_datetime()

#     def get_cursor(self, event=""):
#         cursor_row = self.AttendanceReportTable.focus()
#         content = self.AttendanceReportTable.item(cursor_row)
#         data = content.get('values', [])
#         if data:
#             self.var_atten_id.set(data[0])
#             self.var_atten_name.set(data[1])
#             self.var_atten_dep.set(data[2])
#             self.var_atten_time.set(data[3])
#             self.var_atten_date.set(data[4])
#             self.var_atten_attendance.set(data[5])

#     def fetchData(self, rows):
#         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
#         for i in rows:
#             self.AttendanceReportTable.insert("", END, values=i)

#     def search_data(self, event=None):
#         search_txt = self.var_search.get().strip().lower()
#         if search_txt == "":
#             self.fetch_today_attendance()
#             return
#         filtered = []
#         for row in mydata:
#             if (search_txt in row[0].lower()) or (search_txt in row[1].lower()) or (search_txt in row[2].lower()):
#                 filtered.append(row)
#         self.fetchData(filtered)

#     def clear_search(self):
#         self.var_search.set("")
#         self.fetch_today_attendance()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Attendance(root)
#     root.mainloop()


















# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import os
# from student import Student
# from train import Train
# from face_recognition import Face_Recognition
# from attendance import Attendance
# from developer import Developer
# from help import Help
# from time import strftime

# # login page
# class LoginPage:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Login - Face Recognition System")
#         self.root.state('zoomed')
#         self.root.config(bg="#e6f2ff")

#         # Main frame 
#         self.main_frame = Frame(root, bg="white", bd=5, relief=RIDGE)
#         self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=900, height=500)

#         # Left Frame 
#         left_frame = Frame(self.main_frame, bg="white")
#         left_frame.place(x=0, y=0, width=450, height=500)

    
#         img1 = Image.open("back_images/img1.png")  
#         img1= img1.resize((450, 500), Image.Resampling.LANCZOS)
#         self.photo = ImageTk.PhotoImage(img1)
#         lbl_img1 = Label(left_frame, image=self.photo, bg="white")
#         lbl_img1.pack()

#         # Right Frame 
#         right_frame = Frame(self.main_frame, bg="#e6f2ff")
#         right_frame.place(x=450, y=0, width=450, height=500)

#         # Title Label
#         Label(right_frame, text="Login", font=("Arial Rounded MT Bold", 36, "bold"), bg="#e6f2ff", fg="#004080").pack(pady=50)

#         # Variables
#         self.username = StringVar()
#         self.password = StringVar()

#         form_frame = Frame(right_frame, bg="#e6f2ff")
#         form_frame.pack(pady=20)

#         # Username
#         Label(form_frame, text="Username:", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#003366").grid(row=0, column=0, padx=15, pady=15, sticky=E)
#         Entry(form_frame, textvariable=self.username, font=("Arial", 18), width=25, bd=3, relief=RIDGE).grid(row=0, column=1, padx=15, pady=15)

#         # Password
#         Label(form_frame, text="Password:", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#003366").grid(row=1, column=0, padx=15, pady=15, sticky=E)
#         Entry(form_frame, textvariable=self.password, font=("Arial", 18), show="*", width=25, bd=3, relief=RIDGE).grid(row=1, column=1, padx=15, pady=15)

#         # Login Button
#         self.btn_login = Button(right_frame, text="Login", command=self.check_login, width=20,
#                                 font=("Arial Rounded MT Bold", 20), bg="#007acc", fg="white",
#                                 activebackground="#005999", cursor="hand2", bd=0, relief=RIDGE)
#         self.btn_login.pack(pady=40)

#         # Hover effect for button
#         self.btn_login.bind("<Enter>", lambda e: self.btn_login.config(bg="#005999"))
#         self.btn_login.bind("<Leave>", lambda e: self.btn_login.config(bg="#007acc"))

#     def check_login(self):
#         user = self.username.get()
#         pwd = self.password.get()

#         if user == "admin" and pwd == "1234":
#             messagebox.showinfo("Success", "Login successful!")
#             self.root.destroy()
#             open_main_window()
#         else:
#             messagebox.showerror("Error", "Invalid username or password!")

# # main app
# class Face_Recognition_System:
#     def __init__(self, root):
#         self.root = root
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()
#         self.root.geometry(f"{screen_width}x{screen_height}+0+0")
#         self.root.title("Face Recognition System")
#         self.root.state('zoomed')

#         # Images & Layout
#         self.load_images()
#         self.create_widgets()

#     def load_images(self):
#         # Load and store all image
#         self.photoimg1 = ImageTk.PhotoImage(Image.open("back_images/img1.png").resize((500,130), Image.Resampling.LANCZOS))
#         self.photoimg2 = ImageTk.PhotoImage(Image.open("back_images/img2.png").resize((500,130), Image.Resampling.LANCZOS))
#         self.photoimg3 = ImageTk.PhotoImage(Image.open("back_images/img3.png").resize((530,130), Image.Resampling.LANCZOS))
#         self.photoimg4 = ImageTk.PhotoImage(Image.open("back_images/img4.png").resize((1530,668), Image.Resampling.LANCZOS))
#         self.photoimg5 = ImageTk.PhotoImage(Image.open("back_images/img5.png").resize((180,180), Image.Resampling.LANCZOS))
#         self.photoimg6 = ImageTk.PhotoImage(Image.open("back_images/img6.png").resize((180,180), Image.Resampling.LANCZOS))
#         self.photoimg7 = ImageTk.PhotoImage(Image.open("back_images/img7.png").resize((180,180), Image.Resampling.LANCZOS))
#         self.photoimg11 = ImageTk.PhotoImage(Image.open("back_images/img11.png").resize((180,180), Image.Resampling.LANCZOS))
#         self.photoimg8 = ImageTk.PhotoImage(Image.open("back_images/img8.png").resize((180,180), Image.Resampling.LANCZOS))
#         self.photoimg9 = ImageTk.PhotoImage(Image.open("back_images/img1.png").resize((180,180), Image.Resampling.LANCZOS))
#         self.photoimg10 = ImageTk.PhotoImage(Image.open("back_images/img9.png").resize((180,180), Image.Resampling.LANCZOS))
#         self.photoimg12 = ImageTk.PhotoImage(Image.open("back_images/img10.png").resize((180,180), Image.Resampling.LANCZOS))

#     def create_widgets(self):
#         Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
#         Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)
#         Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=530, height=130)

#         bg_lbl = Label(self.root, image=self.photoimg4)
#         bg_lbl.place(x=0, y=130, width=1530, height=668)
#         bg_lbl.lower()

#         title_lbl = Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM",
#                           font=("Arial Rounded MT Bold", 28,"bold"), bg="white", fg="red")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # Time display
#         def time():
#             string = strftime('%H:%M:%S %p')
#             lbl.config(text=string)
#             lbl.after(1000, time)

#         lbl = Label(title_lbl, font=('Arial Rounded MT Bold',12,'bold'), bg='white', fg='blue')
#         lbl.place(x=0, y=0, width=110, height=50)
#         time()

#         # Buttons
#         Button(bg_lbl, image=self.photoimg5, command=self.student_details, cursor="hand2").place(x=100, y=70, width=180, height=180)
#         Button(bg_lbl, text="Student Details", command=self.student_details, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=100, y=250, width=180, height=35)

#         Button(bg_lbl, image=self.photoimg6, command=self.face_data, cursor="hand2").place(x=400, y=70, width=180, height=180)
#         Button(bg_lbl, text="Face Detector", command=self.face_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=400, y=250, width=180, height=35)

#         Button(bg_lbl, image=self.photoimg7, command=self.attendance_data, cursor="hand2").place(x=700, y=70, width=180, height=180)
#         Button(bg_lbl, text="Attendance", command=self.attendance_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=700, y=250, width=180, height=35)

#         Button(bg_lbl, image=self.photoimg11, command=self.help_data, cursor="hand2").place(x=1000, y=70, width=180, height=180)
#         Button(bg_lbl, text="Help Desk", command=self.help_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=1000, y=250, width=180, height=35)

#         Button(bg_lbl, image=self.photoimg8, command=self.train_data, cursor="hand2").place(x=100, y=330, width=180, height=180)
#         Button(bg_lbl, text="Train Data", command=self.train_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=100, y=510, width=180, height=35)

#         Button(bg_lbl, image=self.photoimg9, command=self.open_img, cursor="hand2").place(x=400, y=330, width=180, height=180)
#         Button(bg_lbl, text="Photos", command=self.open_img, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=400, y=510, width=180, height=35)

#         Button(bg_lbl, image=self.photoimg10, command=self.developer_data, cursor="hand2").place(x=700, y=330, width=180, height=180)
#         Button(bg_lbl, text="Developer", command=self.developer_data, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=700, y=510, width=180, height=35)

#         Button(bg_lbl, image=self.photoimg12, command=self.iExit, cursor="hand2").place(x=1000, y=330, width=180, height=180)
#         Button(bg_lbl, text="Exit", command=self.iExit, font=("Arial Rounded MT Bold", 13, "bold"), bg="darkblue", fg="white").place(x=1000, y=510, width=180, height=35)

#     def open_img(self):
#         os.startfile("data")

#     def iExit(self):
#         exit_confirm = messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?", parent=self.root)
#         if exit_confirm:
#             self.root.destroy()

#     def student_details(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Student(self.new_window)

#     def train_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Train(self.new_window)

#     def face_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Face_Recognition(self.new_window)

#     def attendance_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Attendance(self.new_window)

#     def developer_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Developer(self.new_window)

#     def help_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Help(self.new_window)


# # ==================== OPEN MAIN WINDOW AFTER LOGIN ====================
# def open_main_window():
#     root2 = Tk()
#     obj = Face_Recognition_System(root2)
#     root2.mainloop()


# # ==================== MAIN ====================
# if __name__ == "__main__":
#     root = Tk()
#     app = LoginPage(root)
#     root.mainloop()
