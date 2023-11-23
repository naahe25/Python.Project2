
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Customer_Info:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("915x440+190+80")

        #====All Variables=====

        self.name_var = StringVar()
        self.contact_var = StringVar()
        self.email_var = StringVar()
        self.card_number = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()

        

        #==============Title======================
        lbl_title = Label(self.root, text="Customer", font=("times new roman", 16, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=915, height=30)

        #=============Label Frame=================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Info",
                                    font=("times new roman", 10, "bold"), bg="light grey", fg="Black")
        labelframeleft.place(x=5, y=35, width=200, height=245)

        #======================polash==============
        # std name
        lab_std_name = Label(labelframeleft, text="Name", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_name.grid(row=0, column=0)
        entry_name = ttk.Entry(labelframeleft,textvariable = self.name_var, width=19, font=("times new roman", 10, "bold"))
        entry_name.grid(row=0, column=1, sticky=W)

        # std mobile number
        lab_std_MN = Label(labelframeleft, text="Phone", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_MN.grid(row=1, column=0)
        entry_MN = ttk.Entry(labelframeleft,textvariable = self.contact_var, width=19, font=("times new roman", 10, "bold"))
        entry_MN.grid(row=1, column=1, sticky=W)

        # std email
        lab_std_email = Label(labelframeleft, text="Email", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_email.grid(row=2, column=0)
        entry_email = ttk.Entry(labelframeleft,textvariable = self.email_var, width=19, font=("times new roman", 10, "bold"))
        entry_email.grid(row=2, column=1, sticky=W)

        # std ID
        lab_std_roll = Label(labelframeleft, text="Card No", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_roll.grid(row=3, column=0)
        entry_roll = ttk.Entry(labelframeleft,textvariable = self.card_number, width=19, font=("times new roman", 10, "bold"))
        entry_roll.grid(row=3, column=1, sticky=W)

        # gender
        lab_std_gender = Label(labelframeleft, text="Gender ", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_gender.grid(row=5, column=0)

        combo_gender = ttk.Combobox(labelframeleft,textvariable = self.gender_var, font=("arial", 10, "bold"), width=17, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=5, column=1)

        # address
        lbl_Address=Label(labelframeleft,text="Address",font=("times new roman",10,"bold"), padx=2, pady=6)
        lbl_Address.grid(row=6,column=0)
        
        self.txt_Address=Text(labelframeleft,width=19,height=4,font=("times new roman", 10, "bold"), padx=2, pady=6)
        self.txt_Address.grid(row=6,column=1,sticky="W")
        

        # buttonframe
        buttonFrame = Frame(labelframeleft, bd=2, relief=RIDGE)
        buttonFrame.place(x=0, y=200, width=200, height=30)
        # addButton
        button_add = Button(buttonFrame, text="Add",command= self.add_customers , font=("arial", 7, "bold"), bg="black", fg="gold", width=6)
        button_add.grid(row=0, column=0, padx=1)

        # updateButton
        button_update = Button(buttonFrame, command=self.update_data , text="Update", font=("arial", 7, "bold"), bg="black", fg="gold", width=6)
        button_update.grid(row=0, column=1, padx=1)

        # deleteButton
        button_delete = Button(buttonFrame,command=self.delete_data , text="Delete", font=("arial", 7, "bold"), bg="black", fg="gold", width=6)
        button_delete.grid(row=0, column=2, padx=1)

        
       

        # Clear Button
        ClearButton= Button(buttonFrame,text="Clear",command=self.clear,font=("arial", 7, "bold"), bg="black", fg="gold", width=8)
        ClearButton.grid(row=0,column=3, padx=1)
        

        # right frame
        labelframeLright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system",
                                      font=("times new roman", 15, "bold"), padx=2)
        labelframeLright.place(x=210, y=30, width=865, height=490)

        # address
        lab_search = Label(labelframeLright, text="Search By :", font=("times new roman", 14), padx=2, pady=6,
                           bg="red", fg="white")
        lab_search.grid(row=0, column=0, padx=2)

        # combo box for search
        combo_search = ttk.Combobox(labelframeLright, font=("arial", 12), width=22, state="readonly")
        combo_search["value"] = ("Mobile Number", "Card No")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        entry_ser = ttk.Entry(labelframeLright, width=22, font=("times new roman", 15, "bold"))
        entry_ser.grid(row=0, column=2, sticky=W, padx=2)

        # details frame
        details_frame = LabelFrame(labelframeLright, bd=2, font=("times new roman", 14, "bold"), padx=2)
        details_frame.place(x=0, y=50, width=710, height=355)

        # show data table
        scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)
        self.std_details_table = ttk.Treeview(details_frame, column=('Name', 'Phone', 'Email', 'Card No', 'Gender', 'Address'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.std_details_table.xview)
        scroll_y.config(command=self.std_details_table.yview)

        self.std_details_table.heading("Name", text="Name")
        self.std_details_table.heading("Phone", text="Phone")
        self.std_details_table.heading("Email", text="Email")
        self.std_details_table.heading("Card No", text="Card No")
        self.std_details_table.heading("Gender", text="Gender")
        self.std_details_table.heading("Address", text="Address")

        self.std_details_table["show"] = "headings"

        self.std_details_table.column("Name", width=100)
        self.std_details_table.column("Phone", width=100)
        self.std_details_table.column("Email", width=100)
        self.std_details_table.column("Card No", width=100)
        self.std_details_table.column("Gender", width=100)
        self.std_details_table.column("Address", width=100)
        self.std_details_table.pack(fill=BOTH, expand=1)
        self.std_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_customers(self):
        con = pymysql.connect(host="localhost",user = "root",password = "",database="customer")
        cur = con.cursor()
        cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s)",(self.name_var.get(),
                                                                self.contact_var.get(),
                                                                self.email_var.get(),
                                                                self.card_number.get(),
                                                                self.gender_var.get(),
                                                                self.txt_Address.get('1.0',END)
                                                                     ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con = pymysql.connect(host="localhost",user = "root",password = "",database="customer")
        cur = con.cursor()
        cur.execute("select * from customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.std_details_table.delete(*self.std_details_table.get_children())
            for row in rows:
                self.std_details_table.insert('',END,values=row)
            con.commit()
        con.close()    

    def clear(self):
        self.name_var.set("")
        self.contact_var.set("")
        self.email_var.set("")
        self.card_number.set("")
        self.gender_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row = self.std_details_table.focus()
        contents = self.std_details_table.item(cursor_row)
        row = contents['values']
        self.name_var.set(row[0])
        self.contact_var.set(row[1])
        self.email_var.set(row[2])
        self.card_number.set(row[3])
        self.gender_var.set(row[4])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[5])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="customer")   
        cur = con.cursor()
        cur.execute("UPDATE customer SET name=%s, phone=%s, email=%s, card_no=%s, gender=%s, address=%s WHERE card_no=%s", (
            self.name_var.get(),
            self.contact_var.get(),
            self.email_var.get(),
            self.card_number.get(),
            self.gender_var.get(),
            self.txt_Address.get('1.0', END),
            self.card_number.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Updated")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="customer")
        cur = con.cursor()
        cur.execute("DELETE FROM customer WHERE card_no = %s", self.card_number.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Deleted")

        

if __name__ == "__main__":
    root = Tk()
    object = Customer_Info(root)
    root.mainloop()