from tkinter import*

class Fish_on:
    def __init__(self,root):
        self.root = root
        self.root.title("Review")
        self.root.geometry("915x440+190+80")

        #==============Title======================
        lbl_title = Label(self.root,text="Fish", font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=915,height=30)

        #=============Label Frame=================
        #labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Review",font=("times new roman",10,"bold"),bg="light grey",fg="Black")
        #labelframeleft.place(x=0,y=30,width=425,height=370)

if __name__ == "__main__":
    root = Tk()
    object = Fish_details(root)
    root.mainloop()