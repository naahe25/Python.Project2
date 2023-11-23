from tkinter import*
Window = Tk()

photo = PhotoImage(file='vector.png')

label = Label(Window,
              text="Hello",
              font = ('Arial',40,'bold'),
              fg='blue',
              bg='yellow',
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady= 20,
              image = photo,
              compound='bottom')
label.pack()
Window.mainloop()
              
