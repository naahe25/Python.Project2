from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk    #from pillow model
from tkinter import messagebox


class Register:
    def __init__(self,root): #window name is root
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0") #size -> width,height,X-axis,Y-Axis

        #== bg image ==

        self.bg = ImageTk.PhotoImage(file =r"C:\Users\NAAHE\OneDrive\OneDrive\Naahe.Codes\Python.Project2\Login Page\Images\restaurant-interior.jpg") # r is used to convert backslash to forward slash

        bg_lbl = Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #== left image ==

        self.bg1 = ImageTk.PhotoImage(file =r"C:\Users\NAAHE\OneDrive\OneDrive\Naahe.Codes\Python.Project2\Login Page\Images\table-set-dinning-table.jpg") # r is used to convert backslash to forward slash

        bg_lbl = Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=550)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
