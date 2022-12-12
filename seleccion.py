import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

class Menuseleccion(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("SELECCION DE PRODUCTOS ")
        width=583
        height=488
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GListBox_131=tk.Listbox(self)
        GListBox_131["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_131["font"] = ft
        GListBox_131["fg"] = "#333333"
        GListBox_131["justify"] = "center"
        GListBox_131.place(x=40,y=50,width=349,height=138)

        GButton_584=tk.Button(self)
        GButton_584["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_584["font"] = ft
        GButton_584["fg"] = "#000000"
        GButton_584["justify"] = "center"
        GButton_584["text"] = "AGREGAR"
        GButton_584.place(x=230,y=230,width=70,height=25)
        GButton_584["command"] = self.agregar

        GButton_714=tk.Button(self)
        GButton_714["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_714["font"] = ft
        GButton_714["fg"] = "#000000"
        GButton_714["justify"] = "center"
        GButton_714["text"] = "ELIMINAR"
        GButton_714.place(x=320,y=230,width=70,height=25)
        GButton_714["command"] = self.sacar

        GLineEdit_837=tk.Entry(self)
        GLineEdit_837["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_837["font"] = ft
        GLineEdit_837["fg"] = "#333333"
        GLineEdit_837["justify"] = "center"
        GLineEdit_837["text"] = ""
        GLineEdit_837.place(x=0,y=20,width=400,height=25)

        GButton_343=tk.Button(self)
        GButton_343["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_343["font"] = ft
        GButton_343["fg"] = "#000000"
        GButton_343["justify"] = "center"
        GButton_343["text"] = "BUSCAR"
        GButton_343.place(x=410,y=20,width=70,height=25)
        GButton_343["command"] = self.busqueda

        GLineEdit_240=tk.Entry(self)
        GLineEdit_240["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_240["font"] = ft
        GLineEdit_240["fg"] = "#333333"
        GLineEdit_240["justify"] = "center"
        GLineEdit_240["text"] = ""
        GLineEdit_240.place(x=40,y=230,width=70,height=25)

        GLineEdit_239=tk.Entry(self)
        GLineEdit_239["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_239["font"] = ft
        GLineEdit_239["fg"] = "#333333"
        GLineEdit_239["justify"] = "center"
        GLineEdit_239["text"] = ""
        GLineEdit_239.place(x=130,y=230,width=70,height=25)

        GMessage_9=tk.Message(self)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_9["font"] = ft
        GMessage_9["fg"] = "#333333"
        GMessage_9["justify"] = "center"
        GMessage_9["text"] = "ID"
        GMessage_9.place(x=30,y=200,width=80,height=25)

        GMessage_989=tk.Message(self)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_989["font"] = ft
        GMessage_989["fg"] = "#333333"
        GMessage_989["justify"] = "center"
        GMessage_989["text"] = "CANTIDAD"
        GMessage_989.place(x=120,y=200,width=80,height=25)

        GListBox_546=tk.Listbox(self)
        GListBox_546["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_546["font"] = ft
        GListBox_546["fg"] = "#333333"
        GListBox_546["justify"] = "center"
        GListBox_546.place(x=40,y=270,width=351,height=126)

        GButton_574=tk.Button(self)
        GButton_574["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_574["font"] = ft
        GButton_574["fg"] = "#000000"
        GButton_574["justify"] = "center"
        GButton_574["text"] = "CONFIRMAR COMPRA"
        GButton_574.place(x=430,y=430,width=125,height=35)
        GButton_574["command"] = self.confirmacion

    def agregar(self):
        print("command")


    def sacar(self):
        print("command")


    def busqueda(self):
        print("command")


    def confirmacion(self):
        print("command")

