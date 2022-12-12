import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
from Menu_administracion.menu_administrador import MenuAdm
from registro import Registro
from seleccion import Menuseleccion
import bll.usuarios as user

class Inicio(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Inicio de Sesion")   
        width=481
        height=260
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
        GLabel_890["text"] = "Usuario:"
        GLabel_890.place(x=60,y=50,width=70,height=25)

        GLabel_256=tk.Label(self)
        GLabel_256["cursor"] = "trek"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "center"
        GLabel_256["text"] = "Contraseña: "
        GLabel_256.place(x=60,y=110,width=70,height=25)

        GLineEdit_540=tk.Entry(self,name="txtUsuario")
        GLineEdit_540["bg"] = "#ffffff"
        GLineEdit_540["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_540["font"] = ft
        GLineEdit_540["fg"] = "#333333"
        GLineEdit_540["justify"] = "center"
        GLineEdit_540["text"] = ""
        GLineEdit_540.place(x=140,y=50,width=250,height=30)

        GLineEdit_411=tk.Entry(self,name="txtContrasenia",show="*")
        GLineEdit_411["bg"] = "#ffffff"
        GLineEdit_411["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_411["font"] = ft
        GLineEdit_411["fg"] = "#333333"
        GLineEdit_411["justify"] = "center"
        GLineEdit_411["text"] = ""
        GLineEdit_411.place(x=140,y=110,width=250,height=30)

        GButton_305=tk.Button(self)
        GButton_305["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_305["font"] = ft
        GButton_305["fg"] = "#000000"
        GButton_305["justify"] = "center"
        GButton_305["text"] = "Entrar"
        GButton_305.place(x=300,y=210,width=150,height=25)
        GButton_305["command"] = self.iniciar_sesion

        # GButton_389=tk.Button(self)
        # GButton_389["bg"] = "#f0f0f0"
        # ft = tkFont.Font(family='Times',size=10)
        # GButton_389["font"] = ft
        # GButton_389["fg"] = "#000000"
        # GButton_389["justify"] = "center"
        # GButton_389["text"] = "Cancelar"
        # GButton_389.place(x=390,y=210,width=70,height=25)
        # GButton_389["command"] = self.cancelar

        GMessage_601=tk.Message(self)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_601["font"] = ft
        GMessage_601["fg"] = "#333333"
        GMessage_601["justify"] = "right"
        GMessage_601["text"] = "¿No posee una cuenta?"
        GMessage_601.place(x=10,y=210,width=250,height=50)

        GButton_559=tk.Button(self)
        GButton_559["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_559["font"] = ft
        GButton_559["fg"] = "#000000"
        GButton_559["justify"] = "center"
        GButton_559["text"] = "Registrarse"
        GButton_559.place(x=200,y=210,width=70,height=35)
        GButton_559["command"] = self.Registro

    def iniciar_sesion(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()            

            txtContrasenia = self.nametowidget("txtContrasenia")
            contrasenia = txtContrasenia.get()

            if usuario != "":
                # if user.validar(usuario, contrasenia):
                #     Menuseleccion(self.master)
                #     self.destroy()
                if user.validar(usuario, contrasenia):                    
                    usuario = user.obtener_nombre_usuario(usuario)
                    if usuario is not None:
                        if usuario[8] == "Administrador":
                            MenuAdm(self.master)
                            self.destroy()
                        elif usuario[8] == "Cliente":
                            # TODO chequear el rol del usuario para abrir el menu/ventana correspondiente
                            Menuseleccion(self.master)
                    else:
                        tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")      
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))



    #def cancelar(self):
     #   self.destroy()


    def Registro(self):
        Registro(self.master)

