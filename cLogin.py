from tkinter import *
import tkinter as tk
from tkinter import ttk
import cIPDataBase
import cPanouControl
from PIL import Image, ImageTk


class LoginFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        def logIn(username,password):
            mydb = cIPDataBase.myDataBase()
            if mydb.askLogIn(username, password) is True:
                controller.show_frame(cPanouControl.PanouControl)
            else:
                print("Parola gresita sau user")





        label = ttk.Label(self)
        label.config(background="white")
        label.pack(fill=BOTH, expand=YES)

        labelNume1 = tk.Label(label, text="Gogu Bank", anchor=CENTER)
        labelNume1.place(relx=0.33, rely=0.15, height=35, width=266)
        labelNume1.config(background="white")
        labelNume1.config(font=("Courier", 27, 'bold'))

        # username
        userImage = PhotoImage(file="GUIPhotos/envelope.png")
        labelNume = Label(label, image=userImage, bg='white')
        labelNume.place(relx=0.25, rely=0.32, anchor=CENTER, relwidth='0.08', relheight='0.084')
        labelNume.image=userImage

        entryNume = Entry(label)
        entryNume.place(relx=0.5, rely=0.32, anchor=CENTER, relwidth="0.4", relheight='0.084')

        # password
        passwordImage = PhotoImage(file="GUIPhotos/lock.png")
        labelPass = Label(label, image=passwordImage, bg='white')
        labelPass.place(relx=0.25, rely=0.5, anchor=CENTER, relwidth='0.08', relheight='0.09')
        labelPass.image=passwordImage

        entryPass = Entry(label,show="*")
        entryPass.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth='0.4', relheight='0.09')

        #buton
        buttonImage = PhotoImage(file="GUIPhotos/login.png")
        logButton = Button(label, bg="white", image=buttonImage,command=lambda:logIn(entryNume.get(),entryPass.get()))
        logButton.place(rely=0.7, relx=0.5, anchor=CENTER, relwidth="0.3", relheight='0.1')
        logButton.image=buttonImage

