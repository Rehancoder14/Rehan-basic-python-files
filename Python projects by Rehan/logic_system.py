from tkinter import*
from PIL import ImageTk
class login:
    def __init__(self,window) :
        self.window = window
        self.window.title("LOGIN PAGE BY REHAN")
        self.window.geometry("800x500+0+0")
        # file = "C:\\Users\user\\Documents\\wallpaper\\hackwall.jpg"
        file1 = "C:\\Users\\user\\Documents\\wallpaper\\username.png"
        file2 = "C:\\Users\\user\\Documents\\wallpaper\\password.png"
        # self.bg_icon = ImageTk.PhotoImage(file)
        self.user_icon=PhotoImage(file1)
        self.pass_icon = PhotoImage(file2)

        window_title= Label(self.window, text="LOGIN PAGE",font = ("algerian",38,"bold"),bg = "yellow", fg ="red")
        window_title.place(x =0, y =0,relwidth=1)
        bg_lbl= Label(self.window, image = self.bg_icon).pack()

window = Tk()
obj = login(window)
window.mainloop()