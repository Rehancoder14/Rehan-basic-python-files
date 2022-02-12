from os import system
from tkinter import *

class window:
    def __init__(self,root):
        self.root = root
        self.root.title("rehan")
        self.root.geometry("1000x500+180+70")
        system_lable = Label(self.root,text="Rehan",font=("algerian",40,"bold","italic"),anchor=CENTER,fg="black",bg="cyan")
        system_lable.place(x=0,y=0,relwidth=1)
    
root = Tk()
obj = window(root)
root.mainloop()