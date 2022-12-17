from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
from agregadodeprods import Agregar_prod
import bll.productos as prod
from editadodeprod import Editar_prod
from registro import Registro


class Prods(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("Listado de Productos")        
        width=800
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Productos:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("producto", "cantidad", "precio", "categoria"), name="tvProductos")
        tv.column("#0", width=78)
        tv.column("producto", width=100, anchor=CENTER)
        tv.column("cantidad", width=150, anchor=CENTER)
        tv.column("precio", width=150, anchor=CENTER)
        tv.column("categoria", width=150, anchor=CENTER)
        #tv.column("rol", width=120, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("producto", text="Producto", anchor=CENTER)
        tv.heading("cantidad", text="Cantidad", anchor=CENTER)
        tv.heading("precio", text="Precio", anchor=CENTER)
        tv.heading("categoria", text="Categoria", anchor=CENTER)
        #tv.heading("rol", text="Rol", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=40,width=750,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=530,y=10,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=610,y=10,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=690,y=10,width=70,height=25)
        btn_eliminar["command"] = self.eliminar

    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvProductos")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        
        Agregar_prod(self, True)

    def editar(self): 
        Editar_prod(self, self.select_id)

    def eliminar(self):
       answer =  tkMsgBox.askokcancel(self.master.title(), "¿Está seguro que desea eliminar este producto?")   
       if answer:
           prod.eliminarp(self.select_id)
           self.refrescar()

    # https://www.youtube.com/watch?v=n0usdtoU5cE
    def refrescar(self):        
        tvProductos = self.nametowidget("tvProductos")
        for record in tvProductos.get_children():
            tvProductos.delete(record)
        productos = prod.listarp()
        for producto in productos:
            tvProductos.insert("", END, text=producto[0], values=(producto[1], producto[2], producto[3], producto[4])) 