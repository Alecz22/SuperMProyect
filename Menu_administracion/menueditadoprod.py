import sqlite3
from Menu_administracion.arbolcdepopcprod import Prods
from dal import db 
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from bll import *
from bll.productos import listarp

class menu_editadoprod(tk.Toplevel):
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

        GLabel_135=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_135["font"] = ft
        GLabel_135["fg"] = "#333333"
        GLabel_135["justify"] = "center"
        GLabel_135["text"] = "--------Editado de Productos-------"
        GLabel_135.place(x=10,y=20,width=272,height=30)

        GButton_337=tk.Button(self)
        GButton_337["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_337["font"] = ft
        GButton_337["fg"] = "#000000"
        GButton_337["justify"] = "center"
        GButton_337["text"] = "VER LISTA DE PRODUCTOS"
        GButton_337.place(x=10,y=110,width=250,height=30)
        GButton_337["command"] = self.verprods

        GButton_134=tk.Button(self)
        GButton_134["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_134["font"] = ft
        GButton_134["fg"] = "#000000"
        GButton_134["justify"] = "center"
        GButton_134["text"] = "Salir"
        GButton_134.place(x=190,y=270,width=70,height=25)
        GButton_134["command"] = self.salir

    def verprods(self):
        Prods(self.master)


    def salir(self):
        self.destroy()