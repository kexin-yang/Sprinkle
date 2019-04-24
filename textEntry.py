import sys
from tkinter import *

# cited from https://www.youtube.com/watch?v=hst3AWjxF5o
def mhello():
    mtext = ment.get()
    mlabel2 = Label(mGui,text = mtext).pack()
    return
mGui = Tk()
ment = StringVar()

mGui.geometry('450x450+500+300')
mGui.title("my youtube tkinter")
mbutton = Button(mGui, text = "OK", command = mhello, fg = "red", bg = "blue").pack()
mEntry = Entry(mGui,textvariable = ment).pack()