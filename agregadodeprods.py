import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.productos as prods
from datetime import date

class Agregar_prod(tk.Toplevel):
    def __init__(self, master=None, prod_id=None):
        super().__init__(master)
        self.master=master
        self.prod_id=None
        self.title("Agregado de Producto")
        width=434
        height=411
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_890=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_890["font"] = ft
        GLabel_890["fg"] = "#333333"
        GLabel_890["justify"] = "center"
        GLabel_890["text"] = "Producto:"
        GLabel_890.place(x=60,y=60,width=70,height=25)

        GLabel_256=tk.Label(self)
        GLabel_256["cursor"] = "trek"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "center"
        GLabel_256["text"] = "Cantidad: "
        GLabel_256.place(x=60,y=20,width=70,height=25)

        

        GLineEdit_540=tk.Entry(self, name="txtProducto")
        GLineEdit_540["bg"] = "#ffffff"
        GLineEdit_540["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_540["font"] = ft
        GLineEdit_540["fg"] = "#333333"
        GLineEdit_540["justify"] = "center"
        GLineEdit_540["text"] = ""
        GLineEdit_540.place(x=130,y=60,width=250,height=25)

        GLineEdit_411=tk.Entry(self,name="txtCantidad")
        GLineEdit_411["bg"] = "#ffffff"
        GLineEdit_411["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_411["font"] = ft
        GLineEdit_411["fg"] = "#333333"
        GLineEdit_411["justify"] = "center"
        GLineEdit_411["text"] = ""
        GLineEdit_411.place(x=130,y=20,width=250,height=25)

        GLineEdit_217=tk.Entry(self,name="txtPrecio")
        GLineEdit_217["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_217["font"] = ft
        GLineEdit_217["fg"] = "#333333"
        GLineEdit_217["justify"] = "center"
        GLineEdit_217["text"] = ""
        GLineEdit_217.place(x=130,y=110,width=250,height=25)

        GLineEdit_869=tk.Entry(self,name="txtCategoria")
        GLineEdit_869["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_869["font"] = ft
        GLineEdit_869["fg"] = "#333333"
        GLineEdit_869["justify"] = "center"
        GLineEdit_869["text"] = ""
        GLineEdit_869.place(x=130,y=190,width=150,height=25)




        GButton_305=tk.Button(self)
        GButton_305["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_305["font"] = ft
        GButton_305["fg"] = "#000000"
        GButton_305["justify"] = "center"
        GButton_305["text"] = "Aceptar"
        GButton_305.place(x=260,y=380,width=70,height=25)
        GButton_305["command"] = self.aceptar

        GButton_389=tk.Button(self)
        GButton_389["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_389["font"] = ft
        GButton_389["fg"] = "#000000"
        GButton_389["justify"] = "center"
        GButton_389["text"] = "Cancelar"
        GButton_389.place(x=340,y=380,width=70,height=25)
        GButton_389["command"] = self.cancelar

       

        GLabel_318=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_318["font"] = ft
        GLabel_318["fg"] = "#333333"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "Precio:"
        GLabel_318.place(x=60,y=110,width=70,height=25)


        GLabel_747=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_747["font"] = ft
        GLabel_747["fg"] = "#333333"
        GLabel_747["justify"] = "center"
        GLabel_747["text"] = "Categoria:"
        GLabel_747.place(x=60,y=190,width=70,height=25)



       

    

       
    


    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def cancelar(self):
        self.destroy()
    def aceptar(self):
        try:
            producto=self.get_value("txtProducto")
            cantidad=self.get_value("txtCantidad")
            precio=self.get_value("txtPrecio")
            categoria=self.get_value("txtCategoria")

            if self.prod_id is None:
                print("Alta de producto")
                prods.agregarp(producto,cantidad,precio,categoria )
                tkMsgBox.showinfo(self.master.title(), "Producto agregado!!!!!!")                
                try:
                        self.master.refrescar()
                except Exception as ex:
                        print(ex)
                self.destroy() 
            else:
                tkMsgBox.showerror(self.master.title(),"Hay un tipo de error") 
                self.destroy()

    
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))               
          

