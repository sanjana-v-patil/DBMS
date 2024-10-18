from tkinter import*
from PIL import Image , ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220") #WidthxHeight+from where the window starts + height
        # ====================Variabls========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
#------------------TITLE--------------------------------------
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("arial",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

#--------------------------LOGO--------------------------------
        img2=Image.open(r"C:\Users\SANJANA V PATIL\Downloads\Hotel_Management_System\hotel images\logohotel.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

#--------------------LABELFRAME-------------------------------

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

#-----------------------LABEL ENTRIES------------------------
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        #entry field
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29, state='readonly')
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        # Mother name
        lblmname = Label(labelframeleft, font=("arial", 12, "bold"), text="Mother Name:", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother, font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        # Gender combobox
        label_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Choose Option", "Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Post code
        lblPostCode = Label(labelframeleft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        # Mobile number
        lblMobile = Label(labelframeleft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email,font=("arial", 13, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, font=("arial", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_Nationality["value"] = ("Choose Option", "Indian", "American", "Canadian", "British", "Australian")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # Id proof combobox
        lblIdProof = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Proof Type:", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_IdProof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof,font=("arial", 12, "bold"), width=27, state="readonly")
        combo_IdProof["value"] = ("Choose Option", "Aadhar Card", "Passport", "Voter ID", "Driver's License", "PAN Card")
        combo_IdProof.current(0)
        combo_IdProof.grid(row=8, column=1)

        # Id number
        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number,font=("arial", 13, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        txtAddress.grid(row=10, column=1)

#----------------------BUTTONS------------------------------------------------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data, font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update, font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="DELETE",command=self.mDelete, font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
#---------------------TABLE FRAME------------------------------------------------

        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Serach Sysytem",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)

#--------------------------entities---------------------------------------

        lblSearchBy = Label(table_frame, font=("arial", 12, "bold"), text="Search By:",bg="black",fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)

        self.search_var=StringVar()
        
        combo_Search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Choose Option", "Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)


        self.txt_search=StringVar()
        txtSearch = ttk.Entry(table_frame, textvariable= self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2,padx=2)

#-------------------BUTTONS---------------------------------------------
       
        btnSearch=Button(table_frame,text="Search",command=self.search,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(table_frame,text="Show All",command=self.fetch_data, font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

#------------------------------SHOW DATA TABLE-----------------------------------------------
      
       # Creating the detail_table Frame
        
        detail_table=Frame(table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860,height=350)

        #Creating the scroll bars

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        # Creating the Treeview widget

        self.Cust_Details_table=ttk.Treeview ( detail_table,columns=( "Ref","Name","Mother","Gender","Post","Mobile","Email","Nationality", "IdProof","IdNumber","Address"),
                                                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

              
         # Packing the scroll bars
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

       # Configuring the scroll bar after packing the Treeview
        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)
       
       
        self.Cust_Details_table.heading("Ref", text="Reference No")
        self.Cust_Details_table.heading("Name", text="Name")
        self.Cust_Details_table.heading("Mother", text="Mother's Name")
        self.Cust_Details_table.heading("Gender", text="Gender")
        self.Cust_Details_table.heading("Post", text="Post Code")
        self.Cust_Details_table.heading("Mobile", text="Mobile No")
        self.Cust_Details_table.heading("Email", text="Email Address")
        self.Cust_Details_table.heading("Nationality", text="Nationality")
        self.Cust_Details_table.heading("IdProof", text="ID Proof")
        self.Cust_Details_table.heading("IdNumber", text="ID Number")
        self.Cust_Details_table.heading("Address", text="Address")


        self.Cust_Details_table["show"]="headings"

        self.Cust_Details_table.column("Ref", width=100)
        self.Cust_Details_table.column("Name", width=100)
        self.Cust_Details_table.column("Mother", width=100)
        self.Cust_Details_table.column("Gender", width=100)
        self.Cust_Details_table.column("Post", width=100)
        self.Cust_Details_table.column("Mobile", width=100)
        self.Cust_Details_table.column("Email", width=100)
        self.Cust_Details_table.column("Nationality", width=100)
        self.Cust_Details_table.column("IdProof", width=100)
        self.Cust_Details_table.column("IdNumber", width=100)
        self.Cust_Details_table.column("Address", width=100)


        # Packing the Treeview widget first
        self.Cust_Details_table.pack(fill=BOTH,expand=1)
        self.Cust_Details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

# ===========adddata================
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="sanjana@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                self.var_ref.get(),
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_address.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                messagebox.showinfo("Success","Customer has been inserted",parent=self.root)
                
                
             
            except Exception as es:
                messagebox.showwarning("Warning",f" Some thing went wrong :{str(es)}",parent=self.root)
    # ===========fetch================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjana@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for i in rows:
                self.Cust_Details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # ===========getcursor================
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_table.focus()
        content=self.Cust_Details_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

   # =========Update Data==================
    def update(self):
        if self.var_mobile.get()=="" :
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjana@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                                               
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_address.get(),
                                                                                self.var_ref.get()
                                                                             ))
                                                                                                    
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("UPDATE","Customer details has been updated successfully",parent=self.root)

    # =============DeleteData===============
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you delete this Room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjana@123",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return 
         
        conn.commit()
        self.fetch_data()
        # self.clear_room()
        conn.close()
    # ========Reset data===================
    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.get(),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    # ========Search data===================


    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjana@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where " +str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for i in rows:
                self.Cust_Details_table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
