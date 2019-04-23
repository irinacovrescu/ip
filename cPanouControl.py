from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cLogin
import cIPDataBase

NUM_PHOTOS=6

class PanouControl(tk.Frame):

    def menubar(self, root):
        menubar = tk.Menu(root, bd=2)
        pageMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Meniu", menu=pageMenu)
        pageMenu.add_command(label="Selectare algoritm",command=lambda: root.SettingsPage(0))
        pageMenu.add_command(label="Securitate",command=lambda:root.SecurityPage() )
        pageMenu.add_separator()
        pageMenu.add_cascade(label="Exit", command=quit)
        return menubar

    def __init__(self,parent,controller):
        '''Ar trebui mutata pe butonul de selectare tip de algoritm'''
        tk.Frame.__init__(self, parent)

        #create DB Object

        def info(username):
            mydb = cIPDataBase.myDataBase()
            print("IBAN : %s --- SOLD : %s --- NAME : %s --- EMAIL : %s" % mydb.showInfo(username))

        def sold(username):
            mydb = cIPDataBase.myDataBase()
            print("SOLD : %s" % mydb.showSold(username))


        #buton vezi informatii
        imageInfo=PhotoImage(file="GUIPhotos/034.png")
        butonVeziInformatii = tk.Button(self,relief=RIDGE,image=imageInfo,anchor=CENTER,compound=CENTER,
                                        cursor="hand2", command=lambda: info(cLogin.LoginFrame.user))
        butonVeziInformatii.place(relx=0.1, rely=0.27, height=40, width=266)
        butonVeziInformatii.image=imageInfo

        #buton vezi informatii
        imageInfo=PhotoImage(file="GUIPhotos/037.png")
        butonVeziInformatii = tk.Button(self,relief=RIDGE,image=imageInfo,anchor=CENTER,compound=CENTER,
                                        cursor="hand2", command=lambda: sold(cLogin.LoginFrame.user))
        butonVeziInformatii.place(relx=0.1, rely=0.47, height=40, width=240)
        butonVeziInformatii.image=imageInfo


        #buton deschidere bariera

        # imageDeschide=PhotoImage(file="GUIPhotos/033.png")
        # butonDeschideBariera=tk.Button(self,relief=RIDGE,image=imageDeschide,
        #                                cursor="hand2",compound=CENTER,anchor=CENTER)
        # butonDeschideBariera.place(relx=0.1,rely=0.27,height=30,width=266)
        # butonDeschideBariera.image=imageDeschide
        #

        #label cu stare curenta
        # labelStare = tk.Label(self, text="LPR functioneaza normal", anchor=CENTER,
        #                                 bg="white")
        # labelStare.place(relx=0.1, rely=0.66, height=30, width=266)
        #

        #Afisarea ultimului numar recunoscut


