from tkinter import PhotoImage, Canvas
from tkinter import *
from PIL import ImageTk, Image

import customtkinter
import user
from database import app
from user import user
from login import login


class start:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail Paradise Management System")
        self.root.geometry("550x630")
        self.root.resizable(width=False, height=False)

        img1 = ImageTk.PhotoImage(Image.open("Abacada.png"))
        cercaImg = Label(self.root, image=img1)
        cercaImg.image = img1  # Keep a reference

        cercaImg.grid(row=0, column=0, columnspan=2,pady=20,padx=20)

        self.admin = customtkinter.CTkButton(master=self.root,
                                             width=160,
                                             height=50,
                                             border_width=2,
                                             corner_radius=20,
                                             pady=20,
                                             text="Administrator",
                                             command=self.call_admin)
        self.admin.grid(row=1, column=1)

        self.login = customtkinter.CTkButton(master=self.root,
                                             width=160,
                                             height=50,
                                             border_width=2,
                                             corner_radius=20, pady=20,
                                             text="Login/Register",
                                             command=self.call_login)
        self.login.grid(row=1, column=0)

    def call_admin(self):
        root = customtkinter.CTk()
        self.admin = app(root)
        root.mainloop()

    def call_login(self):
        root = customtkinter.CTk()
        self.admin = login(root, 0)
        root.mainloop()


if __name__ == '__main__':
    root = customtkinter.CTk()
    application = start(root)
    root.mainloop()
