import sqlite3
from Menu_administracion.arboldeopc import Users
from dal import db 
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from bll import *
from bll.usuarios import listar

class menu_editadous(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.title("Menu Administracion")
        width=278
        height=314
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        # GButton_793=tk.Button(self)
        # GButton_793["bg"] = "#f0f0f0"
        # ft = tkFont.Font(family='Times',size=10)
        # GButton_793["font"] = ft
        # GButton_793["fg"] = "#000000"
        # GButton_793["justify"] = "center"
        # GButton_793["text"] = "AGREGAR USUARIO"
        # GButton_793.place(x=10,y=60,width=250,height=30)
        # GButton_793["command"] = self.agregarus

        GLabel_135=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_135["font"] = ft
        GLabel_135["fg"] = "#333333"
        GLabel_135["justify"] = "center"
        GLabel_135["text"] = "--------Editado de Usuarios-------"
        GLabel_135.place(x=10,y=20,width=272,height=30)

        GButton_337=tk.Button(self)
        GButton_337["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_337["font"] = ft
        GButton_337["fg"] = "#000000"
        GButton_337["justify"] = "center"
        GButton_337["text"] = "VER LISTA DE USUARIOS"
        GButton_337.place(x=10,y=110,width=250,height=30)
        GButton_337["command"] = self.verus

        # GButton_540=tk.Button(self)
        # GButton_540["bg"] = "#f0f0f0"
        # ft = tkFont.Font(family='Times',size=10)
        # GButton_540["font"] = ft
        # GButton_540["fg"] = "#000000"
        # GButton_540["justify"] = "center"
        # GButton_540["text"] = "ACTUALIZAR DATO"
        # GButton_540.place(x=10,y=160,width=250,height=30)
        # GButton_540["command"] = self.actus

        # GButton_153=tk.Button(self)
        # GButton_153["bg"] = "#f0f0f0"
        # ft = tkFont.Font(family='Times',size=10)
        # GButton_153["font"] = ft
        # GButton_153["fg"] = "#000000"
        # GButton_153["justify"] = "center"
        # GButton_153["text"] = "BORRAR USUARIO"
        # GButton_153.place(x=10,y=210,width=250,height=30)
        # GButton_153["command"] = self.borrarus

        GButton_134=tk.Button(self)
        GButton_134["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_134["font"] = ft
        GButton_134["fg"] = "#000000"
        GButton_134["justify"] = "center"
        GButton_134["text"] = "Salir"
        GButton_134.place(x=190,y=270,width=70,height=25)
        GButton_134["command"] = self.salir

    # def agregarus(self):
    #     print("command")


    def verus(self):
        Users(self.master)



    # def actus(self):
    #     print("command")


    # def borrarus(self):
    #     print("command")


    def salir(self):
        self.destroy()