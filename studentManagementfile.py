from tkinter import *
from tkinter import ttk
import pymysql
class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1550x800+0+0")
        title = Label(self.root, text="Eshan College Management System", bd=10, relief=GROOVE, font=("times new roman",40,"bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)


# ======================variable ================

        self.Roll_N0_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()


        self.search_by = StringVar()
        self.search_txt = StringVar()



            
# =================== Manage Fram ===========================
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20, y=100, width=440, height=650)
        m_title = Label(Manage_Frame, text="Manage Student", font=("times new roman",20,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)
        lbl_roll = Label(Manage_Frame, text="Roll Number", font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1, column=0, pady=13, padx=20, sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_N0_var, font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=13, padx=10, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=2, column=0, pady=13, padx=20, sticky="w")
        txt_Name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=13, padx=10, sticky="w")

        lbl_email= Label(Manage_Frame, text="Email", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_email.grid(row=3, column=0, pady=13, padx=20, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=13, padx=10, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_gender.grid(row=4, column=0, pady=13, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 12, "bold"))
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, pady=13, padx=20, sticky="w")

        # txt_Gender = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # txt_Gender.grid(row=4, column=1, pady=20, padx=10, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_contact.grid(row=5, column=0, pady=13, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame,  textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=13, padx=10, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_dob.grid(row=6, column=0, pady=13, padx=20, sticky="w")

        txt_DOB= Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=13, padx=10, sticky="w")

        lbl_address = Label(Manage_Frame, text="ADDRESS", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_address.grid(row=7, column=0, pady=13, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=25,height=4)
        self.txt_Address.grid(row=7, column=1, pady=13, padx=15, sticky="w")
# ========= Button Frame ===================================================================
        btn_Fram = Frame(Manage_Frame,bd=4, relief=RIDGE,bg="crimson")
        btn_Fram.place(x=10,y=570,width=400)
        AddBtn = Button(btn_Fram,text="Add",width=10, command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updateBtn = Button(btn_Fram,text="Update",width=10 , command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deleteBtn = Button(btn_Fram,text="Delete",width=10, command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        ClearBtn = Button(btn_Fram,text="Clear",width=10, command=self.clear).grid(row=0,column=3,padx=10,pady=10)






# =================== Detail Fram ===========================

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=480, y=100, width=1040, height=650)

        lbl_search = Label(Detail_Frame, text="Search By", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")


        search_btn = Button(Detail_Frame, text="Search", width=10, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        show_btn = Button(Detail_Frame, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
        n_window_btn = Button(Detail_Frame, text="new window", width=10, command=self.next).grid(row=0, column=5, padx=10, pady=10)
# ==================================== Table Frame ==============================================
        Table_Frame = Frame(Detail_Frame,bd=4, relief=RIDGE, bg='crimson')
        Table_Frame.place(x=10,y=70,width=1020, height=570)
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email.")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column('roll',width=100)
        self.Student_table.column('name',width=130)
        self.Student_table.column('email',width=130)
        self.Student_table.column('gender',width=130)
        self.Student_table.column('contact',width=130)
        self.Student_table.column('dob',width=130)
        self.Student_table.column('address',width=240)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def next(self):
        nx = Tk()
        class New_Window:
            def __init__(self, nx):
                self.nx = nx
                self.nx.geometry("500x500")
                self.nx.resizable(0, 0)
                self.nx.title("Student Registration records")
                self.label = Label(nx, text= "Student Registration Records", font=("time 15 bold", 20, "bold"),bg="blue",fg="white",padx=70,pady=1)
                self.label.grid(row = 0, column = 0,columnspan = 20)
        obj = New_Window(nx)
    def add_students(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
            self.Roll_N0_var.get(),
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_Address.get('1.0', END)
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            con.commit()
        con.close()


    def clear(self):
        self.Roll_N0_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        # print(row)
        self.Roll_N0_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[6])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("update students set name =%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (

            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_Address.get('1.0', END),
            self.Roll_N0_var.get()

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_N0_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from students where"+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            con.commit()
        con.close()



root = Tk()
ob = Student(root)
root.mainloop()