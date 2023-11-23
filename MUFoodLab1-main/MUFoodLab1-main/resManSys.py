from tkinter import*
from PIL import Image, ImageTk

class RestaurantManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("1550x800+0+0")

        #==============1st Image======================
        img1 = Image.open(r"chef-service.jpg")
        img1 = img1.resize((1540,200),Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1540,height=200)

        #==============Logo======================
        logo = Image.open(r"logo.png") 
        logo = logo.resize((230,200),Image.ADAPTIVE)
        self.phologo = ImageTk.PhotoImage(logo)

        lblimg = Label(self.root,image=self.phologo,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=200)

        #==============Logo======================
        lbl_title = Label(self.root,text="MU Food Lab", font=("times new roman",40,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=200,width=1540,height=50)

        #==============Main Frame======================
        main_frame= Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=250,width=1540,height=620)

        #==============Menu======================
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #==============btn======================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=350)

        #==============customer======================
        customer_btn=Button(btn_frame,text="Customer",width=22,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        customer_btn.grid(row=0,column=0)
         

        #==============Ordering System======================
        Order_btn=Button(btn_frame,text="Order Now",width=22,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Order_btn.grid(row=1,column=0)

        #==============Reservation======================
        Reservation_btn=Button(btn_frame,text="Reservation",width=22,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Reservation_btn.grid(row=2,column=0)

        #==============Reviews Section======================
        Review_btn=Button(btn_frame,text="Reviews",width=22,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Review_btn.grid(row=3,column=0)

         #==============Dine Out Section======================
        DineOut_btn=Button(btn_frame,text="Dine Out",width=22,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        DineOut_btn.grid(row=4,column=0)

        #==============Drinks Section======================
        Drinks_btn=Button(btn_frame,text="Drinks",width=22,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        Drinks_btn.grid(row=5,column=0)


         #==============About Us======================
        About_btn=Button(btn_frame,text="About",width=22,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=5,cursor="hand1")
        About_btn.grid(row=6,column=0)

         #==============1st Image======================
        img3 = Image.open(r"banner.jpg")
        img3 = img3.resize((1310,590),Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=225,y=0,width=1310,height=450)  

         



if __name__ == "__main__":
    root=Tk()
    obj = RestaurantManagementSystem(root)
    root.mainloop()