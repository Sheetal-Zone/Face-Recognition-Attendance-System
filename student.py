from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.root.title("Face Recognition System")
        self.root.state('zoomed')

        #variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.photo_avr = StringVar()
        



         # Image 1
        img1 = Image.open("back_images/img1.png")
        img1 = img1.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl1 = Label(self.root, image=self.photoimg1)
        lbl1.place(x=0, y=0, width=500, height=130)

        # Image 2
        img2 = Image.open("back_images/img2.png")
        img2 = img2.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl2 = Label(self.root, image=self.photoimg2)
        lbl2.place(x=500, y=0, width=500, height=130)

        # Image 3
        img3 = Image.open("back_images/img3.png")
        img3 = img3.resize((530,130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl3 = Label(self.root, image=self.photoimg3)
        lbl3.place(x=1000, y=0, width=530, height=130)
        


         # Background Image
        img4 = Image.open("back_images/img4.png")
        img4 = img4.resize((1530,668), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0, y=130, width=1530, height=668)
        bg_lbl.lower() 



        title_lbl=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM ",font=("Arial Rounded MT Bold", 28,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=10,y=55,width=1260,height=500)


        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=485)
        
        #current course
        course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information",font=("times new roman", 12, "bold"))
        course_frame.place(x=10, y=10, width=700, height=120)
        
        
        #Department
        dep_label=Label(course_frame,text="Department", font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),state="read only",width=17)
        dep_combo["values"]=("Select Department","ECE","CSE","IT","Civil","Mechanical","Pharmacy","MBA","MCA","AIML","AIDS","CyberSecurity" )
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=5)

        
        #Course
        Course_label=Label(course_frame,text="Courses", font=("times new roman",12,"bold"))
        Course_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman", 12, "bold"),state="read only",width=17)
        Course_combo["values"]=("Select Course","CYS","DS","ML","FSD")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=10,pady=5,sticky=W)
       

        #Year
        year_label=Label(course_frame,text="Year", font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman", 12, "bold"),state="read only",width=17)
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
       

        #Semester
        Semester_label=Label(course_frame,text="Semester", font=("times new roman",12,"bold"))
        Semester_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Semester_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),state="read only",width=17)
        Semester_combo["values"]=("Select Semester","odd","even")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)
              

        #Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE,text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=10, y=140, width=700, height=320)  
        
       # studentid
        studentID_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",13,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #student name
        studentName_label=Label(class_Student_frame,text="StudentName:",font=("times new roman",13,"bold"))
        studentName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        
        #student gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),state="read only",width=17)
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)



        #radio buttons
        self.var_radio1=StringVar()
        self.photo_avr = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, text="Take Photo Sample", variable=self.photo_avr, value="Yes")
        radiobtn1.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.var_radio1=StringVar()
        radiobtn2 = ttk.Radiobutton(class_Student_frame,text="No Photo Sample", variable=self.photo_avr, value="No")
        radiobtn2.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Buttons frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=10, y=150, width=680, height=100)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=6,pady=5)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=6,pady=5)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=6,pady=5)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=6,pady=5)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=25,font=("times new roman",13,"bold"),bg="skyblue")
        take_photo_btn.grid(row=1,column=0,columnspan=2,padx=10,pady=8)


        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=25,font=("times new roman",13,"bold"),bg="skyblue")
        update_photo_btn.grid(row=1,column=2,columnspan=2,padx=10,pady=8)




        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=770,y=10,width=740,height=485)


        #Search system
        # Search Frame
        Search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search Student", font=("times new roman", 12, "bold"))
        Search_frame.place(x=10, y=10, width=695, height=100)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"))
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # ✅ Use self. to make it accessible in other methods
        self.Search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="read only", width=15)
        self.Search_combo["values"] = ("Select", "Student_id", "Year")
        self.Search_combo.current(0)
        self.Search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
        self.search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # ✅ Bind command methods
        search_btn = Button(Search_frame, text="Search", command=self.search_data, width=11, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        search_btn.grid(row=1, column=1, padx=10, pady=5)

        searchAll_btn = Button(Search_frame, text="Show All", command=self.fetch_data, width=11, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        searchAll_btn.grid(row=1, column=2, padx=10, pady=5)


        
       #table frame
        table_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=10, y=115, width=695, height=340) 
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="PhotoSamplesStatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
       

        self.student_table.bind("<MouseWheel>", self.on_mouse_wheel)
        
        

    
    def on_mouse_wheel(self, event):
        self.student_table.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

   # function declaration
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="14232239", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student WHERE Student_id=%s", (self.var_std_id.get(),))
                existing = my_cursor.fetchone()
                
                if existing:
                    messagebox.showerror("Error", "This Student ID already exists!", parent=self.root)
                else:
                    my_cursor.execute("INSERT INTO student (Dep, Course, Year, Semester, Student_id, Name, Gender, Photosample) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_radio1.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
           


       # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="14232239", database="face_recognizer")   
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert("", END, values=row)
            conn.commit()
        conn.close()



    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gender.set(data[7])
        self.var_radio1.set(data[8]) 

        #update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="14232239", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, Photosample=%s WHERE Student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)   
    
    
    #delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="14232239", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM student WHERE Student_id=%s", (self.var_std_id.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                                   

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_gender.set("Male")
        self.var_radio1.set("No") 
#search function
    def search_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="14232239", database="face_recognizer")
            my_cursor = conn.cursor()

            selected_field = self.Search_combo.get()
            search_value = self.search_entry.get()

            if selected_field == "Select" or search_value == "":
                messagebox.showerror("Error", "Please select a field and enter a search value", parent=self.root)
                return

            query = f"SELECT * FROM student WHERE {selected_field} LIKE %s"
            my_cursor.execute(query, ('%' + search_value + '%',))
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No matching records found", parent=self.root)

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)               


#Generate data set or take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                face_classifier = cv2.CascadeClassifier(
                    r"C:\Users\DELL\OneDrive\Desktop\Face Recognition\haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = f"data/user.{self.var_std_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset generation completed!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)





                    # load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        # Minimum Neighbor=5
                                                
           

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450)) 
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)    
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path)
                            cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Generating data sets completed !!!")






if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


    