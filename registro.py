import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
import bll.roles as rol
from datetime import date

class Registro(tk.Toplevel):
    def __init__(self, master=None, isAdmin=False, user_id=None):
        super().__init__(master)
        self.master=master
        self.user_id=user_id
        self.title("Registro de cuenta")
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
        GLabel_890["text"] = "Nombre:"
        GLabel_890.place(x=60,y=60,width=70,height=25)

        GLabel_256=tk.Label(self)
        GLabel_256["cursor"] = "trek"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "center"
        GLabel_256["text"] = "Apellido: "
        GLabel_256.place(x=60,y=20,width=70,height=25)

        GLineEdit_540=tk.Entry(self, name="txtNombre")
        GLineEdit_540["bg"] = "#ffffff"
        GLineEdit_540["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_540["font"] = ft
        GLineEdit_540["fg"] = "#333333"
        GLineEdit_540["justify"] = "center"
        GLineEdit_540["text"] = ""
        GLineEdit_540.place(x=130,y=60,width=250,height=25)

        GLineEdit_411=tk.Entry(self,name="txtApellido")
        GLineEdit_411["bg"] = "#ffffff"
        GLineEdit_411["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_411["font"] = ft
        GLineEdit_411["fg"] = "#333333"
        GLineEdit_411["justify"] = "center"
        GLineEdit_411["text"] = ""
        GLineEdit_411.place(x=130,y=20,width=250,height=25)

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

        GLineEdit_217=tk.Entry(self,name="txtCorreo")
        GLineEdit_217["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_217["font"] = ft
        GLineEdit_217["fg"] = "#333333"
        GLineEdit_217["justify"] = "center"
        GLineEdit_217["text"] = ""
        GLineEdit_217.place(x=130,y=110,width=250,height=25)

        GLabel_318=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_318["font"] = ft
        GLabel_318["fg"] = "#333333"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "Correo:"
        GLabel_318.place(x=60,y=110,width=70,height=25)

        GLabel_645=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_645["font"] = ft
        GLabel_645["fg"] = "#333333"
        GLabel_645["justify"] = "center"
        GLabel_645["text"] = "Fecha de nacimiento:"
        GLabel_645.place(x=0,y=150,width=125,height=25)

        GLabel_747=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_747["font"] = ft
        GLabel_747["fg"] = "#333333"
        GLabel_747["justify"] = "center"
        GLabel_747["text"] = "DNI:"
        GLabel_747.place(x=60,y=190,width=70,height=25)

        GLabel_438=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_438["font"] = ft
        GLabel_438["fg"] = "#333333"
        GLabel_438["justify"] = "center"
        GLabel_438["text"] = "Usuario:"
        GLabel_438.place(x=60,y=230,width=70,height=25)

        GLabel_8=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#333333"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "Contraseña:"
        GLabel_8.place(x=60,y=270,width=70,height=25)

        GLabel_590=tk.Label(self)
        GLabel_590["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_590["font"] = ft
        GLabel_590["fg"] = "#333333"
        GLabel_590["justify"] = "center"
        GLabel_590["text"] = "Confirmar contraseña:"
        GLabel_590.place(x=0,y=320,width=125,height=30)

        GLineEdit_164=tk.Entry(self,name="txtFechanacimiento")
        GLineEdit_164["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_164["font"] = ft
        GLineEdit_164["fg"] = "#333333"
        GLineEdit_164["justify"] = "center"
        GLineEdit_164["text"] = ""
        GLineEdit_164.place(x=130,y=150,width=150,height=25)

        GLineEdit_869=tk.Entry(self,name="txtDNI")
        GLineEdit_869["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_869["font"] = ft
        GLineEdit_869["fg"] = "#333333"
        GLineEdit_869["justify"] = "center"
        GLineEdit_869["text"] = ""
        GLineEdit_869.place(x=130,y=190,width=150,height=25)

        GLineEdit_890=tk.Entry(self,name="txtUsuario")
        GLineEdit_890["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_890["font"] = ft
        GLineEdit_890["fg"] = "#333333"
        GLineEdit_890["justify"] = "center"
        GLineEdit_890["text"] = ""
        GLineEdit_890.place(x=130,y=230,width=250,height=25)

        GLineEdit_635=tk.Entry(self,name="txtContrasenia",show="*")
        GLineEdit_635["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_635["font"] = ft
        GLineEdit_635["fg"] = "#333333"
        GLineEdit_635["justify"] = "center"
        GLineEdit_635["text"] = ""
        GLineEdit_635.place(x=130,y=270,width=250,height=25)

        GLineEdit_230=tk.Entry(self,name="txtConfirmarcontra",show="*")
        GLineEdit_230["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_230["font"] = ft
        GLineEdit_230["fg"] = "#333333"
        GLineEdit_230["justify"] = "center"
        GLineEdit_230["text"] = ""
        GLineEdit_230.place(x=130,y=320,width=250,height=25)

        GLabel_975 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_975["font"] = ft
        GLabel_975["fg"] = "#333333"
        GLabel_975["anchor"] = "e"
        GLabel_975["text"] = "Rol:"
        GLabel_975.place(x=10,y=350,width=122,height=30)

        roles = dict(rol.listar())
        if isAdmin:
             cb_roles = ttk.Combobox(self, state="readonly", values=list(roles.values()), name="cbRoles")
        else:
                cb_roles = ttk.Combobox(self, state="disabled", values=list(roles.values()), name="cbRoles")
                cb_roles.set(roles[4])
                cb_roles.place(x=130,y=350,width=150,height=25)

        if user_id is not None:
            usuario = user.obtener_id(user_id)
            if usuario is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:
                GLineEdit_411.insert(0, usuario[1])
                GLineEdit_540.insert(0, usuario[2])
                fecha_nac = date(int(usuario[3][:4]), int(usuario[3][5:7]), int(usuario[3][8:]))
                GLineEdit_164.insert(0, fecha_nac.strftime(r"%d/%m/%Y"))
                GLineEdit_869.insert(0, usuario[4])
                GLineEdit_217.insert(0, usuario[5])
                GLineEdit_890.insert(0, usuario[6])
                GLineEdit_890["state"] = "disabled"           
                cb_roles.set(usuario[8])



    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def aceptar(self):
        try:            
            apellido = self.get_value("txtApellido")
            nombre = self.get_value("txtNombre")            
            fecha_nac = self.get_value("txtFechanacimiento")            
            dni = self.get_value("txtDNI")
            email = self.get_value("txtCorreo")            
            usuario = self.get_value("txtUsuario")

            contrasenia = self.get_value("txtContrasenia")            
            confirmacion = self.get_value("txtConfirmarcontra")
            rol_id = self.get_index("cbRoles")

    
            if self.user_id is None:
                print("Alta de usuario")
                if not user.existe(usuario):
                    user.agregar(apellido, nombre, fecha_nac, dni, email, usuario, contrasenia, rol_id) 
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario existente")
            else:
                print("Actualizacion de usuario")
                user.actualizar(self.user_id,apellido, nombre, fecha_nac, dni, email, contrasenia,rol_id) 
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))


    def cancelar(self):
        self.destroy()

