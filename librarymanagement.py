from msilib.schema import ListBox
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkinter.messagebox import askyesno
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1360x700+0+0")
        self.root.wm_iconbitmap("lib.ico")
        



        # ====================================variable===================================

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()




        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",50,"bold"),padx=0,pady=2)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=5,bg="powder blue")
        frame.place(x=0,y=105,width=1360,height=370)

        #=========================Data Frame Left=========================

        DataFrameLeft=LabelFrame(frame,text="Library Membership information",bg="powder blue",fg="green",bd=8,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=0,width=680,height=345)   

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,),textvariable=self.member_var,width=24,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.prn_var,width=26)
        txtPRN_No.grid(row=1,column=1,sticky=W)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.id_var,width=26)
        txtTitle.grid(row=2,column=1,sticky=W)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.firstname_var,width=26)
        txtFirstName.grid(row=3,column=1,sticky=W)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="LastName:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.lastname_var,width=26)
        txtLastName.grid(row=4,column=1,sticky=W)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address1_var,width=26)
        txtAddress1.grid(row=5,column=1,sticky=W)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address2_var,width=26)
        txtAddress2.grid(row=6,column=1,sticky=W)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="PostCode:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.postcode_var,width=26)
        txtPostCode.grid(row=7,column=1,sticky=W)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.mobile_var,width=26)
        txtMobile.grid(row=8,column=1,sticky=W)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="BookId:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.bookid_var,width=26)
        txtBookId.grid(row=0,column=3,sticky=W)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="BookTitle:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.booktitle_var,width=26)
        txtBookTitle.grid(row=1,column=3,sticky=W)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.author_var,width=26)
        txtAuthor.grid(row=2,column=3,sticky=W)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="DateBorrowed:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateborrowed_var,width=26)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="DateDue:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.datedue_var,width=26)
        txtDateDue.grid(row=4,column=3,sticky=W)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="DaysOnBook:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.daysonbook_var,width=26)
        txtDaysOnBook.grid(row=5,column=3,sticky=W)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="LateReturnFine:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.latereturnfine_var,width=26)
        txtLateReturnFine.grid(row=6,column=3,sticky=W)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var,width=26)
        txtDateOverDue.grid(row=7,column=3,sticky=W)

        lblActuralPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActuralPrice.grid(row=8,column=2,sticky=W)
        txtActuralPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.finalprice_var,width=26)
        txtActuralPrice.grid(row=8,column=3,sticky=W)


        #========================Data Frame Right====================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",padx=20,fg="green",bd=8,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=685,y=0,width=645,height=345)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=33,height=16,padx=0,pady=0)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book',"Learn Python the Hard way","Python Programming","Secrete Rahshy",'Python CookBook','Intro to Machine Learning','Fluent Python','Programming Python','The Algorithm','The technique Python',
                                            "Machine technology","My Python",'Joss Ellif Gure','Elite Jungle Python','Mumbai Python',"Pune Python","Guru of Python","Yellow Dragon","Red Python",
                                            'Machine Python','Advance python',"Intro Python","Redchilli Python","Ishq Python"]

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.780")

            elif (x=="Learn Python the Hard way"):
                self.bookid_var.set("BKID5000")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")

            elif (x=="Python Programming"):
                self.bookid_var.set("BKID3000")
                self.booktitle_var.set("Python")
                self.author_var.set("Jimmy")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.300")

            elif (x=="Secrete Rahshy"):
                self.bookid_var.set("BKID3010")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Anderson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.280")

            elif (x=="Python CookBook"):
                self.bookid_var.set("BKID3020")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Tim")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.190")

            elif (x=="Intro to Machine Learning"):
                self.bookid_var.set("BKID3040")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Seifert")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1050")

            elif (x=="Fluent Python"):
                self.bookid_var.set("BKID3050")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Kalam")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.450")

            elif (x=="Programming Python"):
                self.bookid_var.set("BKID3060")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Karl")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.560")

            elif (x=="The Algorithm"):
                self.bookid_var.set("BKID3070")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Peter")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.342")

            elif (x=="The technique Python"):
                self.bookid_var.set("BKID4000")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Shantanu")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.450")

            elif (x=="Machine technology"):
                self.bookid_var.set("BKID4020")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Dr Hari singh")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1060")

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=31,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=0,pady=0)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        # # ===================================Button Frame======================

        framebutton=Frame(self.root,bd=8,relief=RIDGE,padx=10,pady=3,bg="powder blue")
        framebutton.place(x=0,y=480,width=1360,height=54)

        btnAddData=Button(framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,command=self.showdata,text="Show Data",font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # # =======================================Information Frame=============================

        FrameDetails=Frame(self.root,bd=8,relief=RIDGE,padx=5,bg="powder blue")
        FrameDetails.place(x=0,y=535,width=1360,height=160)

        Table_frame=Frame(FrameDetails,bd=5,relief=RIDGE,padx=5,pady=5,bg="powder blue")
        Table_frame.place(x=0,y=0,width=1330,height=145)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host='localhost',username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.member_var.get(),
                                                                                    self.prn_var.get(),
                                                                                    self.id_var.get(),
                                                                                    self.firstname_var.get(),
                                                                                    self.lastname_var.get(),
                                                                                    self.address1_var.get(),
                                                                                    self.address2_var.get(),
                                                                                    self.postcode_var.get(),
                                                                                    self.mobile_var.get(),
                                                                                    self.bookid_var.get(),
                                                                                    self.booktitle_var.get(),
                                                                                    self.author_var.get(),
                                                                                    self.dateborrowed_var.get(),
                                                                                    self.datedue_var.get(),
                                                                                    self.daysonbook_var.get(),
                                                                                    self.latereturnfine_var.get(),
                                                                                    self.dateoverdue_var.get(),
                                                                                    self.finalprice_var.get()
                                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host='localhost',username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookId=%s,Booktitle=%s,Author=%s,Databorrowed=%s,Datedue=%s,Dayasofbook=%s,Latereturnfine=%s,Dateoverdue=%s,Finalprice=%s where PNR_NO=%s",(
                                                                                    self.member_var.get(),
                                                                                    self.id_var.get(),
                                                                                    self.firstname_var.get(),
                                                                                    self.lastname_var.get(),
                                                                                    self.address1_var.get(),
                                                                                    self.address2_var.get(),
                                                                                    self.postcode_var.get(),
                                                                                    self.mobile_var.get(),
                                                                                    self.bookid_var.get(),
                                                                                    self.booktitle_var.get(),
                                                                                    self.author_var.get(),
                                                                                    self.dateborrowed_var.get(),
                                                                                    self.datedue_var.get(),
                                                                                    self.daysonbook_var.get(),
                                                                                    self.latereturnfine_var.get(),
                                                                                    self.dateoverdue_var.get(),
                                                                                    self.finalprice_var.get(),
                                                                                    self.prn_var.get()
                                                                                    ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")
        

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def showdata(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do You want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PNR_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")

        






        
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()