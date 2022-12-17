import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from Menu_administracion.menueditadoprod import menu_editadoprod
from Menu_administracion.menueditadodeus import menu_editadous
from bll import usuarios
from bll import roles

class MenuAdm(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.title("Menu Administrador")
        width=387
        height=269
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_348=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_348["font"] = ft
        GLabel_348["fg"] = "#333333"
        GLabel_348["justify"] = "center"
        GLabel_348["text"] = "------Opciones Administracion Supermarket------"
        GLabel_348.place(x=0,y=20,width=386,height=30)

        GButton_528=tk.Button(self)
        GButton_528["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_528["font"] = ft
        GButton_528["fg"] = "#000000"
        GButton_528["justify"] = "center"
        GButton_528["text"] = "Editar Usuarios"
        GButton_528.place(x=10,y=70,width=360,height=30)
        GButton_528["command"] = self.editarus

        GButton_262=tk.Button(self)
        GButton_262["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_262["font"] = ft
        GButton_262["fg"] = "#000000"
        GButton_262["justify"] = "center"
        GButton_262["text"] = "Editar Productos"
        GButton_262.place(x=10,y=120,width=360,height=30)
        GButton_262["command"] = self.editarprod

        GButton_434=tk.Button(self)
        GButton_434["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_434["font"] = ft
        GButton_434["fg"] = "#000000"
        GButton_434["justify"] = "center"
        GButton_434["text"] = "Ver Facturas de Clientes"
        GButton_434.place(x=10,y=170,width=360,height=30)
        GButton_434["command"] = self.facturas

        GButton_334=tk.Button(self)
        GButton_334["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_334["font"] = ft
        GButton_334["fg"] = "#000000"
        GButton_334["justify"] = "center"
        GButton_334["text"] = "Salir"
        GButton_334.place(x=300,y=230,width=70,height=25)
        GButton_334["command"] = self.salir

    def editarus(self):
        menu_editadous(self.master)
       


    def editarprod(self):
        menu_editadoprod(self.master)


    def facturas(self): #AGRERGAR COMANDOS
        print("command")


    def salir(self):
        self.destroy()
