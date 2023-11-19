from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk    #from pillow model
from tkinter import messagebox

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\NAAHE\OneDrive\OneDrive\Naahe.Codes\Python.Project2\Login Page\Images\background.jpeg")
        

        lbl_bg = Label(self.root,image= self.bg)
        lbl_bg.place(x=5,y=5,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="black")
        frame.place(x=540,y=170,width=340,height=450)

        img1 = Image.open(r"C:\Users\NAAHE\OneDrive\OneDrive\Naahe.Codes\Python.Project2\Login Page\Images\6681204.png")
        img1= img1.resize((100,100),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=653,y=175,width=100,height=100)

        get_str = Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Label
        username=lbl= Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=65,y=155)

        self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textuser.place(x=40,y=180,width=270)

        password=lbl= Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=65,y=225)

        self.textpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textpassword.place(x=40,y=250,width=270)


        #========Icon_Images=======
        
        img2 = Image.open(r"C:\Users\NAAHE\OneDrive\OneDrive\Naahe.Codes\Python.Project2\Login Page\Images\6681204.png")
        img2= img2.resize((20,20),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=583,y=326,width=22,height=22)

        img3 = Image.open(r"C:\Users\NAAHE\OneDrive\OneDrive\Naahe.Codes\Python.Project2\Login Page\Images\icon-5355895_960_720.webp")
        img3= img3.resize((20,20),Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=583,y=397,width=22,height=22)

        #====LogInButton=====

        loginbtn = Button(frame,command=self.login,text = "Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #====Regiter Button=====

        registerbtn = Button(frame,text = "New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #====Forgot Password Button=====

        forgetpasswordbtn = Button(frame,text = "Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpasswordbtn.place(x=10,y=370,width=160)

    def login(self):
        if self.textuser.get()=="" or self.textpassword.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.textuser.get()=="Naahe" and self.textpassword.get()=="Hello World!":
            messagebox.showinfo("Success!","Success ,You Are In!")
        else:
            messagebox.showerror("Invalid","Invalid Username & Password")    
            
    



if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()