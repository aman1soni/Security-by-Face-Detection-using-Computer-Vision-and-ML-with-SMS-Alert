import sys
import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

top=tkinter.Tk()

top.title("System security using Face Detection")

image1 = Image.open("Images/fd.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)


top.geometry('750x500')

def create():
    os.system('create_face_datasets.py')
    
def train():
    os.system('training_model.py')
    
def demo():
    os.system('lock_unlock_face_recognition.py')

    
l1 = tkinter.Label(top,text="System security using Face Detection",font=('arial', 25,'bold'))

l1.pack()



B1=tkinter.Button(top,text="Capture Face Data",command= create,padx=50,pady=20)
B1.place(x=150, y=120)

B2=tkinter.Button(top,text="Train Face System",command= train,padx=50,pady=20)
B2.place(x=150,y=250)

B3=tkinter.Button(top,text="Run Demo",command= demo,padx=50,pady=20)  #.pack(pady=30)
B3.place(x=170,y=390)

top.update()

top.mainloop()
