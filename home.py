from tkinter import *
base = Tk()
base.geometry('500x500')
base.title("Fittish Home Page")
background_image=PhotoImage(file = "bg.png")
label1 = Label( base, image = background_image)
label1.place(x = 0, y = 0)
LARGEFONT =("Verdana", 25)
labl_0 = Label(base, text="Welcome to Fittish!",width=20,font=("bold", 50))
labl_0.place(x=90,y=53)
def calbmi():
base.destroy()
import bmi
def diets():
base.destroy()
import dietshome
b1=Button(base, text="Know Your Diets",font=LARGEFONT,command=diets)
b2=Button(base, text="Calculate Your BMI", font=LARGEFONT, command=calbmi)
def logout():
base.destroy()
import start
b3=Button(base,text="Log Out", font=LARGEFONT, command=logout)
b1.place(x=100, y=350)
b2.place(x=100, y=500)
b3.place(x=100,y=650)
base.mainloop()
