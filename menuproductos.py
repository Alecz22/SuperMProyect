import tkinter as tk
import tkinter.font as tkFont

class MenuProd:
    def __init__(self, root):
        
        root.title("Menu")
        width=400
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_294=tk.Button(root)
        GButton_294["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_294["font"] = ft
        GButton_294["fg"] = "#000000"
        GButton_294["justify"] = "center"
        GButton_294["text"] = "Seleccionar Productos"
        GButton_294.place(x=70,y=80,width=250,height=25)
        GButton_294["command"] = self.GButton_294_command

        GMessage_783=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_783["font"] = ft
        GMessage_783["fg"] = "#333333"
        GMessage_783["justify"] = "center"
        GMessage_783["text"] = "-------------------------------------------------------------------------------------"
        GMessage_783.place(x=0,y=50,width=400,height=25)

        GMessage_704=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_704["font"] = ft
        GMessage_704["fg"] = "#333333"
        GMessage_704["justify"] = "center"
        GMessage_704["text"] = "-------------------------------------------------------------------------------------"
        GMessage_704.place(x=0,y=110,width=400,height=25)

    def GButton_294_command(self):
        print("command")

