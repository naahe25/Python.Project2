from tkinter import *
from PIL import Image, ImageTk
from Order import Order_Now
from Customer import Customer_Info
from DineOut import Dine_Out
from Breakfast import Breakfast_on
from Drinks import Drinks_on
from Reviews import Reviews_on

class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("1550x800+0+0")

        #==============Title======================
        lbl_title = Label(self.root, text="MU Food Lab", font=("times new roman", 40, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1340, height=50)

        #==============Main Frame======================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=50, width=1540, height=620)

        #==============btn======================
        btn_frame = Frame(main_frame, bd=5, relief=RIDGE)
        btn_frame.place(x=0, y=0, width=180, height=425)

        #==============customer======================
        customer_btn = Button(btn_frame, text="Customer Info", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        customer_btn.place(x=0, y=0)

        #==============Special======================
        special_btn = Button(btn_frame, text="Special", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        special_btn.place(x=0, y=40)

        #==============SetMenu System======================
        Order_btn = Button(btn_frame, text="Set Menu", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Order_btn.place(x=0, y=80)

        #==============Breakfast======================
        Reservation_btn = Button(btn_frame, text="Breakfast", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Reservation_btn.place(x=0, y=120)

        #==============Dine Out Section======================
        DineOut_btn = Button(btn_frame, text="Dine Out", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        DineOut_btn.place(x=0, y=160)

        #==============Drinks Section======================
        Drinks_btn = Button(btn_frame, text="Drinks", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Drinks_btn.place(x=0, y=200)

        #==============Reviews Section======================
        Review_btn = Button(btn_frame, text="Reviews", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Review_btn.place(x=0, y=240)

        #==============About Us======================
        About_btn = Button(btn_frame, text="About", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        About_btn.place(x=0, y=280)

        #==============Contact Us:======================
        Contact_btn = Button(btn_frame, text="Contact", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand2")
        Contact_btn.place(x=0, y=320)

        #==============Contact Us:======================
        Contact_btn = Button(btn_frame, text="Contact", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand2")
        Contact_btn.place(x=0, y=370)

        #==============1st Image======================
        img3 = Image.open(r"banner.jpg")
        img3 = img3.resize((1360, 590), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=5, relief=RIDGE)
        lblimg3.place(x=180, y=0, width=1360, height=430)

        #==============1st Image======================
        img1 = Image.open(r"offer.png")
        img1 = img1.resize((1340, 155), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        self.lblimg.place(x=0, y=480, width=1340, height=155)

    def destroy_frame(self, frame):
        # Destroy the frame only if it is lblimg
        if frame == self.lblimg:
            frame.destroy()

    def order_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Order_Now(self.new_window)

    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Info(self.new_window)

    def DineOut_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Dine_Out(self.new_window)

    def Breakfast_on(self):
        self.new_window = Toplevel(self.root)
        self.app = Breakfast_on(self.new_window)

    def Drinks_on(self):
        self.new_window = Toplevel(self.root)
        self.app = Drinks_on(self.new_window)

    def Reviews_on(self):
        self.new_window = Toplevel(self.root)
        self.app = Reviews_on(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = RestaurantManagementSystem(root)
    root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from Order import Order_Now
from Customer import Customer_Info
from DineOut import Dine_Out
from Breakfast import Breakfast_on
from Drinks import Drinks_on
from Reviews import Reviews_on

class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("1550x800+0+0")

        #==============Title======================
        lbl_title = Label(self.root, text="MU Food Lab", font=("times new roman", 40, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1340, height=50)

        #==============Main Frame======================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=50, width=1540, height=620)

        #==============btn======================
        btn_frame = Frame(main_frame, bd=5, relief=RIDGE)
        btn_frame.place(x=0, y=0, width=180, height=425)

        #==============customer======================
        customer_btn = Button(btn_frame, text="Customer Info", command=lambda: (self.destroy_frame(self.lblimg), self.master.destroy()), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")


        customer_btn.place(x=0, y=0)

        #==============Special======================
        special_btn = Button(btn_frame, text="Special", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        special_btn.place(x=0, y=40)

        #==============SetMenu System======================
        Order_btn = Button(btn_frame, text="Set Menu", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Order_btn.place(x=0, y=80)

        #==============Breakfast======================
        Reservation_btn = Button(btn_frame, text="Breakfast", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Reservation_btn.place(x=0, y=120)

        #==============Dine Out Section======================
        DineOut_btn = Button(btn_frame, text="Dine Out", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        DineOut_btn.place(x=0, y=160)

        #==============Drinks Section======================
        Drinks_btn = Button(btn_frame, text="Drinks", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Drinks_btn.place(x=0, y=200)

        #==============Reviews Section======================
        Review_btn = Button(btn_frame, text="Reviews", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        Review_btn.place(x=0, y=240)

        #==============About Us======================
        About_btn = Button(btn_frame, text="About", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand1")
        About_btn.place(x=0, y=280)

        #==============Contact Us:======================
        Contact_btn = Button(btn_frame, text="Contact", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand2")
        Contact_btn.place(x=0, y=320)

        #==============Contact Us:======================
        Contact_btn = Button(btn_frame, text="Contact", command=lambda: self.destroy_frame(self.lblimg), width=15, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=5, cursor="hand2")
        Contact_btn.place(x=0, y=370)

        #==============1st Image======================
        img3 = Image.open(r"banner.jpg")
        img3 = img3.resize((1360, 590), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=5, relief=RIDGE)
        lblimg3.place(x=180, y=0, width=1360, height=430)

        #==============1st Image======================
        img1 = Image.open(r"offer.png")
        img1 = img1.resize((1340, 155), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        self.lblimg.place(x=0, y=480, width=1340, height=155)

    def destroy_frame(self, frame):
        # Destroy the frame only if it is lblimg
        if frame == self.lblimg:
            frame.destroy()

    def order_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Order_Now(self.new_window)

    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Info(self.new_window)

    def DineOut_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Dine_Out(self.new_window)

    def Breakfast_on(self):
        self.new_window = Toplevel(self.root)
        self.app = Breakfast_on(self.new_window)

    def Drinks_on(self):
        self.new_window = Toplevel(self.root)
        self.app = Drinks_on(self.new_window)

    def Reviews_on(self):
        self.new_window = Toplevel(self.root)
        self.app = Reviews_on(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = RestaurantManagementSystem(root)
    root.mainloop()
