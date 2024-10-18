from tkinter import *
from PIL import Image,ImageTk  #pip install pillow
from customer_withbuttons import Cust_Win
from room import Roombooking
from Details import DetailsRoom


class HotelManagementSystem:
        def __init__(self,root):
                    self.root=root
                    self.root.title("Hospital Management System")
                    self.root.geometry("1550x800+0+0")

                    #============================1st image===============================#


                    img1=Image.open(r"C:\Users\SANJANA V PATIL\Downloads\1633410403702hotel-images\hotel images\hotel1.png")
                    img1=img1.resize((1550,140),Image.LANCZOS)
                    self.photoimg1=ImageTk.PhotoImage(img1)


                    Iblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
                    Iblimg.place(x=0,y=0,width=1550,height=140)

                     #============================logo===============================#
                    
                    img2=Image.open(r"C:\Users\SANJANA V PATIL\Downloads\1633410403702hotel-images\hotel images\logohotel.png")
                    img2=img2.resize((230,140),Image.LANCZOS)
                    self.photoimg2=ImageTk.PhotoImage(img2)


                    Iblimg1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
                    Iblimg1.place(x=0,y=0,width=230,height=140)

                    #============================title===============================#
                    lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM" , font=("times new roman", 40,"bold"),bg="black",fg="gold", bd=4,relief=RIDGE)
                    lbl_title.place(x=0,y=140,width=1550,height=50)


                    #============================main frame===============================#
                    main_frame=Frame(self.root,bd=4,relief=RIDGE)
                    main_frame.place(x=0,y=190,width=1550,height=620)

                    #============================menu===============================#
                    lbl_menu=Label(main_frame,text="MENU" , font=("times new roman", 20,"bold"),bg="black",fg="gold", bd=4,relief=RIDGE)
                    lbl_menu.place(x=0,y=0,width=230,height=40)


                    #============================button frame===============================#
                    btn_frame=Frame(self.root,bd=4,relief=RIDGE)
                    btn_frame.place(x=0,y=200,width=228,height=190)


                    cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
                    cust_btn.grid(row=0,column=0,pady=5)
                    

                    room_btn=Button(btn_frame,text="ROOMS",command=self.roombooking,width=22, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
                    room_btn.grid(row=1,column=0,pady=5)

                    details_btn=Button(btn_frame,text="DETAILS",command=self.detailsroom,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
                    details_btn.grid(row=2,column=0,pady=5)
        
                    #report_btn=Button(btn_frame,text="REPORT",width=22, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
                    #report_btn.grid(row=3,column=0,pady=1)

                    logout_btn=Button(btn_frame,text="LOG OUT",command=self.logout,width=22, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
                    logout_btn.grid(row=3,column=0,pady=5)

                    #============================right side image==============================#

                    img3=Image.open(r"C:\Users\SANJANA V PATIL\Downloads\1633410403702hotel-images\hotel images\slide3.jpg")
                    img3=img3.resize((1310,590),Image.LANCZOS)
                    self.photoimg3=ImageTk.PhotoImage(img3)


                    Iblimg2=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
                    Iblimg2.place(x=225,y=0,width=1310,height=590)
                    


                    #============================down images==============================#

                    img4=Image.open(r"C:\Users\SANJANA V PATIL\Downloads\1633410403702hotel-images\hotel images\myh.jpg")
                    img4=img4.resize((230,210),Image.LANCZOS)
                    self.photoimg4=ImageTk.PhotoImage(img4)


                    Iblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
                    Iblimg4.place(x=0,y=225,width=230,height=210)


                    img5=Image.open(r"C:\Users\SANJANA V PATIL\Downloads\1633410403702hotel-images\hotel images\khana.jpg")
                    img5=img5.resize((230,190),Image.LANCZOS)
                    self.photoimg5=ImageTk.PhotoImage(img5)


                    Iblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
                    Iblimg5.place(x=0,y=420,width=230,height=190)


        def cust_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Cust_Win(self.new_window)

        def roombooking(self):
                self.new_window=Toplevel(self.root)
                self.app=Roombooking(self.new_window)

        def detailsroom(self):
                self.new_window=Toplevel(self.root)
                self.app=DetailsRoom(self.new_window)



        def logout(self):
                self.root.destroy()


if __name__=="__main__":
        root=Tk()
        obj=HotelManagementSystem(root)
        root.mainloop()