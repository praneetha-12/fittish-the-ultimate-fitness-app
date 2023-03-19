from tkinter import *
from tkinter import messagebox
def reset_entry():
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')
    
def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)
    
def bmi_index(bmi):
    if bmi < 18.5:
        p = 'You are Underweight'
    elif (bmi > 18.5) and (bmi < 24.9):
        p = 'Good going, your BMI is Normal'
    elif (bmi > 24.9) and (bmi < 29.9):
        p = 'You are Overweight'
    elif (bmi > 29.9):
        p = 'Warning! Obesity'
        
label=Label(ws, text=p , font= 40)
label.place(x= 50,y=250)
ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x300')
ws.config(bg='#ddddbb')
var = IntVar()
frame = Frame(ws,padx=25,pady=25,background='#FFFFF0')
frame.pack(expand=True)
gen_lb = Label(frame,text='Select Gender')
gen_lb.grid(row=1, column=1)
frame2 = Frame(frame)
frame2.grid(row=1, column=2, pady=5)
male_rb = Radiobutton(frame2, text = 'Male', variable = var, value = 1)
male_rb.pack(side=LEFT)
female_rb = Radiobutton(frame2, text = 'Female', variable = var, value = 2)
female_rb.pack(side=RIGHT)
height_lb = Label(frame, text="Enter Height (cm) ")
height_lb.grid(row=2, column=1)
weight_lb = Label(frame,text="Enter Weight (kg) ",)
weight_lb.grid(row=3, column=1)
height_tf = Entry(frame,)
height_tf.grid(row=2, column=2, pady=5)
weight_tf = Entry(frame,)
weight_tf.grid(row=3, column=2, pady=5)
frame3 = Frame(frame)
frame3.grid(row=6, columnspan=3, pady=10)
cal_btn = Button(frame3,text='Calculate',background='#9ae59a',command=calculate_bmi)
cal_btn.pack(side=LEFT)

def homePage():
    ws.destroy()
    
import home1
b1=Button(frame3, text='Go To Home',width=10,bg='brown',fg='white',command=homePage)
b1.pack(side=RIGHT)
ws.mainloop()
