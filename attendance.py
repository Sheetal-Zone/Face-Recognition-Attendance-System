from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os, csv
from datetime import datetime

mydata = []        # All data
today_data = []    # Only today's data

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # ============== Variables ==============
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_search = StringVar()

        # ============== Top Banner Images ==============
        img_top_left = Image.open("back_images/img1.png").resize((screen_width//2, 140), Image.Resampling.LANCZOS)
        self.photo_top_left = ImageTk.PhotoImage(img_top_left)
        Label(self.root, image=self.photo_top_left).place(x=0, y=0, width=screen_width//2, height=140)

        img_top_right = Image.open("back_images/img1.png").resize((screen_width//2, 140), Image.Resampling.LANCZOS)
        self.photo_top_right = ImageTk.PhotoImage(img_top_right)
        Label(self.root, image=self.photo_top_right).place(x=screen_width//2, y=0, width=screen_width//2, height=140)

        # ============== Background Image ==============
        img_bg = Image.open("back_images/img1.png").resize((screen_width, screen_height - 140), Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)
        lbl_bg = Label(self.root, image=self.photo_bg)
        lbl_bg.place(x=0, y=140, width=screen_width, height=screen_height - 140)

        # ============== Title ==============
        Label(lbl_bg, text="ATTENDANCE MANAGEMENT SYSTEM",
              font=("Arial Rounded MT Bold", 32, "bold"), bg="white", fg="green").place(x=0, y=0, width=screen_width, height=50)

        # ============== Main Frame ==============
        main_frame_height = screen_height - 240
        main_frame = Frame(lbl_bg, bd=2, bg="white")
        main_frame.place(x=20, y=60, width=screen_width - 40, height=main_frame_height)

        # ============== Left Frame ==============
        left_frame_width = (screen_width - 80) // 2
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("Arial Rounded MT Bold", 14, "bold"))
        left_frame.place(x=10, y=10, width=left_frame_width, height=main_frame_height - 20)

        img_left = Image.open("back_images/img4.png").resize((700, 130), Image.Resampling.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photo_left).place(x=5, y=0, width=700, height=130)

        left_inner = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inner.place(x=0, y=135, width=720, height=380)

        lbl_font = ("times new roman", 13, "bold")

        # ============== Entry Fields ==============
        Label(left_inner, text="Attendance ID:", font=lbl_font, bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inner, textvariable=self.var_atten_id, width=15, font=lbl_font).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(left_inner, text="Name:", font=lbl_font, bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inner, textvariable=self.var_atten_name, width=15, font=lbl_font).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(left_inner, text="Department:", font=lbl_font, bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inner, textvariable=self.var_atten_dep, width=15, font=lbl_font).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(left_inner, text="Time:", font=lbl_font, bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inner, textvariable=self.var_atten_time, width=15, font=lbl_font).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(left_inner, text="Date:", font=lbl_font, bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inner, textvariable=self.var_atten_date, width=15, font=lbl_font).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(left_inner, text="Attendance:", font=lbl_font, bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.atten_status = ttk.Combobox(left_inner, textvariable=self.var_atten_attendance, width=15, font=lbl_font, state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ============== Buttons ==============
        btn_frame = Frame(left_inner, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=700, height=40)

        Button(btn_frame, text="Add", command=self.add_attendance, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Import CSV", command=self.importCsv_and_show, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Export CSV", command=self.exportCsv, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Update", command=self.update_data, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=3)
        Button(btn_frame, text="Reset", command=self.reset_data, width=14, font=lbl_font, bg="blue", fg="white").grid(row=0, column=4)

        # ============== Right Frame (Table & Search) ==============
        right_frame_width = (screen_width - 80)//2 - 30
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details",
                                 font=("Arial Rounded MT Bold", 14, "bold"))
        right_frame.place(x=left_frame_width + 30, y=10, width=right_frame_width, height=main_frame_height - 20)

        search_frame = Frame(right_frame, bd=2, relief=RIDGE)
        search_frame.pack(fill=X, padx=5, pady=5)

        Label(search_frame, text="Search (ID, Name, Department):", font=lbl_font).pack(side=LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=30, font=lbl_font)
        self.search_entry.pack(side=LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.search_data)
        self.search_entry.bind("<Return>", self.search_data)  # << add this line

        Button(search_frame, text="Search", command=self.search_data, font=lbl_font, bg="green", fg="white").pack(side=LEFT, padx=5)
        Button(search_frame, text="Clear", command=self.clear_search, font=lbl_font, bg="red", fg="white").pack(side=LEFT, padx=5)

        # ============== Table Frame ==============
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                  columns=("id", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        for col in ("id", "name", "department", "time", "date", "attendance"):
            self.AttendanceReportTable.heading(col, text=col.capitalize())
            self.AttendanceReportTable.column(col, width=140)
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

        # Auto-fill time/date + load data
        self.auto_fill_datetime()
        self.importCsv_and_show()

    # ==================== Methods ====================
    def auto_fill_datetime(self):
        now = datetime.now()
        self.var_atten_time.set(now.strftime("%H:%M:%S"))
        self.var_atten_date.set(now.strftime("%d/%m/%Y"))

    def is_duplicate_attendance(self, student_id, date):
        return any(row[0] == student_id and row[4] == date for row in mydata)

    def add_attendance(self):
        new_data = (
            self.var_atten_id.get().strip(),
            self.var_atten_name.get().strip(),
            self.var_atten_dep.get().strip(),
            self.var_atten_time.get().strip(),
            self.var_atten_date.get().strip(),
            self.var_atten_attendance.get().strip()
        )
        if "" in new_data or new_data[5] == "Status":
            messagebox.showerror("Error", "All fields must be filled correctly!")
            return
        if self.is_duplicate_attendance(new_data[0], new_data[4]):
            messagebox.showerror("Error", "Attendance already marked for this student on this date!")
            return
        mydata.append(new_data)
        self.save_to_csv()
        messagebox.showinfo("Success", "Attendance added successfully!")
        self.fetch_today_attendance()
        self.reset_data()

    def importCsv_and_show(self):
        self.importCsv()
        self.fetch_today_attendance()

    def importCsv(self):
        global mydata
        mydata.clear()
        filename = "attendance.csv"
        if os.path.exists(filename):
            with open(filename, newline="", encoding="utf-8") as f:
                csvreader = csv.reader(f)
                next(csvreader, None)
                for row in csvreader:
                    if len(row) == 6:
                        mydata.append(row)
        else:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(["ID", "Name", "Department", "Time", "Date", "Attendance"])

    def save_to_csv(self):
        filename = "attendance.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Time", "Date", "Attendance"])
            writer.writerows(mydata)

    def fetch_today_attendance(self):
        global today_data
        today = datetime.now().strftime("%d/%m/%Y")
        today_data = [row for row in mydata if row[4] == today]
        self.fetchData(today_data)

    def update_data(self):
        selected = self.AttendanceReportTable.focus()
        if not selected:
            messagebox.showerror("Error", "No row selected to update!")
            return
        updated = (
            self.var_atten_id.get().strip(),
            self.var_atten_name.get().strip(),
            self.var_atten_dep.get().strip(),
            self.var_atten_time.get().strip(),
            self.var_atten_date.get().strip(),
            self.var_atten_attendance.get().strip()
        )
        if self.is_duplicate_attendance(updated[0], updated[4]):
            selected_data = self.AttendanceReportTable.item(selected, "values")
            if not (selected_data[0] == updated[0] and selected_data[4] == updated[4]):
                messagebox.showerror("Error", "Attendance already marked for this student on this date!")
                return
        self.AttendanceReportTable.item(selected, values=updated)
        for idx, row in enumerate(mydata):
            if row[0] == updated[0] and row[4] == updated[4]:
                mydata[idx] = updated
                break
        self.save_to_csv()
        messagebox.showinfo("Success", "Record updated successfully!")
        self.fetch_today_attendance()

    def exportCsv(self):
        if not mydata:
            messagebox.showerror("No Data", "No data to export!")
            return
        filename = "exported_attendance.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["ID", "Name", "Department", "Time", "Date", "Attendance"])
            csv.writer(f).writerows(mydata)
        messagebox.showinfo("Exported", f"Data exported to {os.path.abspath(filename)}")

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
        self.auto_fill_datetime()

    def get_cursor(self, event=""):
        cur = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cur)
        data = content.get('values', [])
        if data:
            self.var_atten_id.set(data[0])
            self.var_atten_name.set(data[1])
            self.var_atten_dep.set(data[2])
            self.var_atten_time.set(data[3])
            self.var_atten_date.set(data[4])
            self.var_atten_attendance.set(data[5])

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for row in rows:
            self.AttendanceReportTable.insert("", END, values=row)

    def search_data(self, event=None):
        text = self.var_search.get().strip().lower()
        if text == "":
            self.fetch_today_attendance()
            return
        filtered = [row for row in mydata if text in row[0].lower() or text in row[1].lower() or text in row[2].lower()]
        self.fetchData(filtered)

    def clear_search(self):
        self.var_search.set("")
        self.fetch_today_attendance()

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
