from tkinter import*
from PIL import Image, ImageTk
from SetMenu import SetMenu_Now
from Customer import Customer_Info
from Salad import Salad_on
from Platter import Platter_on
from Rice import Rice_on
from Fish import Fish_on
from Special import Special_on
from Chicken import Chicken_on
from Curry import Curry_on
from Soup import Soup_on
from Drinks import Drinks_on

class RestaurantManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("1550x800+0+0")
        
        #==============Title======================
        lbl_title = Label(self.root,text="MU Food Lab", font=("times new roman",40,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1525,height=50)

        #==============Main Frame======================
        main_frame= Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=50,width=1540,height=620)

        #==============btn======================
        btn_frame=Frame(main_frame,bd=5,relief=RIDGE)
        btn_frame.place(x=0,y=0,width=180,height=465)
        
        #==============customer======================
        customer_btn=Button(btn_frame,text="Customer Info",command=self.customer_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        customer_btn.place(x=0,y=0)

        #==============Special======================
        special_btn=Button(btn_frame,text="Special",command=self.Special_on,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        special_btn.place(x=0,y=40)

        #==============SetMenu System======================
        Order_btn=Button(btn_frame,text="Set Menu",command=self.SetMenu_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Order_btn.place(x=0,y=80)

        #==============Platter======================
        Platter_btn=Button(btn_frame,text="Platter",command=self.Platter_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Platter_btn.place(x=0,y=120)
        
        

         #==============Salad Section======================
        DineOut_btn=Button(btn_frame,text="Salad",command=self.Salad_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        DineOut_btn.place(x=0,y=160)

        #==============Rice Section======================
        Drinks_btn=Button(btn_frame,text="Rice",command=self.Rice_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Drinks_btn.place(x=0,y=200)

         #==============Fish Section======================
        Review_btn=Button(btn_frame,text="Fish", command=self.Fish_details, width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Review_btn.place(x=0,y=240)

         #==============Chicken======================
        About_btn=Button(btn_frame,text="Chicken",command=self.Chicken_details, width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        About_btn.place(x=0,y=280)

        #==============Curry:======================
        Contact_btn=Button(btn_frame,text="Curry",command=self.Curry_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand2")
        Contact_btn.place(x=0,y=320)

        #==============Soup:======================
        Contact_btn=Button(btn_frame,text="Soup",command=self.Soup_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand2")
        Contact_btn.place(x=0,y=360)

        #==============Drinks:======================
        Contact_btn=Button(btn_frame,text="Drinks",command=self.Drinks_details,width=15,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand2")
        Contact_btn.place(x=0,y=410)

         #==============1st Image======================
        img3 = Image.open(r"banner.jpg")
        img3 = img3.resize((920,600),Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame,image=self.photoimg3,bd=5,relief=RIDGE)
        lblimg3.place(x=180,y=0,width=920,height=600)  

        #==============1st Image======================
        img1 = Image.open(r"offer.png")
        img1 = img1.resize((1100,145),Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=520,width=1100,height=145)

    def SetMenu_details(self):
         
        self.new_window= Toplevel(self.root)
        self.app= SetMenu_Now(self.new_window)
    
    def customer_details(self):
        self.new_window= Toplevel(self.root)
        self.app= Customer_Info(self.new_window)

    def Salad_details(self):
        self.new_window= Toplevel(self.root)
        self.app= Salad_on(self.new_window)

    def Platter_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Platter_on(self.new_window)

    def Rice_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Rice_on(self.new_window)

    def Fish_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Fish_on(self.new_window)

    def Special_on(self):
        self.new_window= Toplevel(self.root)
        self.app=Special_on(self.new_window)
    
    def Chicken_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Chicken_on(self.new_window)

    def Curry_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Curry_on(self.new_window)

    def Soup_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Soup_on(self.new_window)
    
    def Drinks_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Drinks_on(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj = RestaurantManagementSystem(root)
    root.mainloop()