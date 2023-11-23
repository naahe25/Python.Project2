from tkinter import*
Window = Tk()

count = 0
def click():
    global cout
    count+=1
    print(count)

photo = PhotoImage(file='vector.png')

button = button(Window,
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