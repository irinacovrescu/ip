from tkinter import *
import tkinter as tk
import cIPDataBase
from tkinter import ttk
from PIL import Image, ImageTk


NUM_PHOTOS=6

class PanouControl(tk.Frame):

    def menubar(self, root):
        menubar = tk.Menu(root, bd=2)
        pageMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Meniu", menu=pageMenu)
        pageMenu.add_command(label="Profil",command=lambda: root.SettingsPage(0))
        pageMenu.add_command(label="Tranzactii",command=lambda:root.SecurityPage() )
        pageMenu.add_separator()
        pageMenu.add_cascade(label="Exit", command=exit)
        return menubar

    def __init__(self,parent,controller):
        '''Ar trebui mutata pe butonul de selectare tip de algoritm'''
        tk.Frame.__init__(self, parent)

        #create DB Object


        #buton deschidere bariera

        imageDeschide=PhotoImage(file="GUIPhotos/cont-curent.png")
        butonDeschideBariera=tk.Button(self,relief=RIDGE,image=imageDeschide,
                                       cursor="hand2",compound=CENTER,anchor=CENTER)
        butonDeschideBariera.place(relx=0.1,rely=0.2,height=82,width=160)
        butonDeschideBariera.image=imageDeschide
        mydb = cIPDataBase.myDataBase()

        labelNume1 = tk.Label(self, text=mydb.exportCurrent("Irina","root"), anchor=CENTER)
        labelNume1.place(relx=0.33, rely=0.25, height=41, width=266)
        labelNume1.config(background="white")
        labelNume1.config(font=("Courier", 20, 'bold'))


        # #buton vezi informatii
        # imageInfo=PhotoImage(file="GUIPhotos/034.png")
        # butonVeziInformatii = tk.Button(self,relief=RIDGE,image=imageInfo,anchor=CENTER,compound=CENTER,
        #                                 cursor="hand2")
        # butonVeziInformatii.place(relx=0.1, rely=0.47, height=30, width=266)
        # butonVeziInformatii.image=imageInfo
        #
        # #label cu stare curenta
        # labelStare = tk.Label(self, text="LPR functioneaza normal", anchor=CENTER,
        #                                 bg="white")
        # labelStare.place(relx=0.1, rely=0.66, height=30, width=266)
        #
        #
        # #Afisarea ultimului numar recunoscut


