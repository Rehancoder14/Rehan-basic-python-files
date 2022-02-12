from tkinter import *

class imp:
    def __init__(self,root):
        self.root = root
        self.root.title("Rehan Mahat")
        self.root.geometry("1000x900+180+70")
        self.root.resizable(False,False)

root = Tk()
obj = imp(root)
mainloop()