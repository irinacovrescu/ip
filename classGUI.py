import tkinter as tk
import cLogin
import cPanouControl


class interfata(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
#        tk.Tk.iconbitmap(self,default='GUIPhotos/009.png')
        self.geometry("400x600")
        self.title("GoguBank")
        container=tk.Frame(self)
        container.pack(fill="both",expand=True)


        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.algorithmVal=0
        self.securityVal=0
        self.x=None
        self.y=None
        self.assign_ops=None
        self.Label=""  #pentru labelul de sub poza cu masina

        self.frames={}

        for F in (cLogin.LoginFrame,cPanouControl.PanouControl):
            frame = F(container,self)

            self.frames[F]= frame

            frame.grid(row=0, column=0,sticky="nsew")

        self.show_frame( cLogin.LoginFrame )

    def show_frame(self,cont):
 #       if cont==cPanouControl.PanouControl:
        self.geometry("800x430")
        frame=self.frames[cont]
        frame.tkraise()

        menubar = frame.menubar(self)
        self.configure(menu=menubar)





app=interfata()
app.mainloop()