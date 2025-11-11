import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
import sqlite3
import util.variables as variables
import datetime
import os

class app:

    def registrarse(self):
        from forms.form_registroUsuario import registro
        self.window.destroy()
        registro()

    def __init__(self):

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")

        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()

        # Crear tablas si es primera vez que se ejecuta
        self.cursor.execute("CREATE TABLE IF NOT EXISTS compra (Precio INTEGER NOT NULL, Fecha DATE DEFAULT NULL, Cantidad INTEGER NOT NULL, Formato VARCHAR(15) NOT NULL, Producto_Código_Barra varchar(15) NOT NULL, proveedor_Rut varchar(11) NOT NULL, Id int NOT NULL, PRIMARY KEY(Producto_Código_Barra,proveedor_Rut,Id), CONSTRAINT fk_Compra_proveedor1 FOREIGN KEY(proveedor_Rut) REFERENCES proveedor(Rut), CONSTRAINT fk_Compra_Producto1 FOREIGN KEY(Producto_Código_Barra) REFERENCES producto(Código_Barra))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS producto (Código_Barra varchar(15) NOT NULL, Código_Básico varchar(15) DEFAULT NULL, Nombre varchar(20) NOT NULL, Precio int NOT NULL, Costo int NOT NULL, Margen int DEFAULT NULL, Categoria varchar(20) DEFAULT NULL, Cantidad int NOT NULL, Unid_Medida varchar(10) NOT NULL, PRIMARY KEY(Código_Barra))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS proveedor (Rut varchar(11) NOT NULL, Razon_Social varchar(40) NOT NULL, Num_Contacto varchar(10) DEFAULT NULL, Contacto varchar(45) DEFAULT NULL, Giro varchar(40), Direccion varchar(45), PRIMARY KEY (Rut))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuario (Rut varchar(10) NOT NULL, Nombre varchar(30) NOT NULL, Tipo_Usuario varchar(20) NOT NULL, Num_Contacto varchar(11) DEFAULT NULL, Contraseña varchar(30) NOT NULL, Usuario varchar(45) NOT NULL, Ultima_Conexión DATETIME DEFAULT NULL, Imagen TEXT, PRIMARY KEY (Rut))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS veguita (Razon_Social VARCHAR(45) NOT NULL, Giro VARCHAR(45) NOT NULL, Direccion VARCHAR(45) NOT NULL, Rut VARCHAR(15) NOT NULL, Boleta_Inicio int NOT NULL, Boleta_Fin int NOT NULL, Ultima_Boleta_Realizada int NOT NULL, PRIMARY KEY (Rut))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS venta ( Num_Boleta int NOT NULL, Cantidad int NOT NULL, Precio int NOT NULL, Fecha date DEFAULT NULL, usuario_Rut varchar(10) NOT NULL, Producto_Código_Barra varchar(15) NOT NULL, PRIMARY KEY (Num_Boleta, usuario_Rut, Producto_Código_Barra), CONSTRAINT fk_Venta_Producto FOREIGN KEY (Producto_Código_Barra) REFERENCES producto (Código_Barra), CONSTRAINT fk_Venta_usuario FOREIGN KEY (usuario_Rut) REFERENCES usuario (Rut))")

        self.mydb.commit()

        self.window = tk.Tk()

        self.window.geometry("800x500")
        self.window.configure(bg = "#8c8c8c")
        utl.centrar_ventana(self.window, 800, 500)
        
        canvas = tk.Canvas(
            self.window,
            bg = "#8c8c8c",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

        background_img = utl.leer_imagen(os.path.join(project_root, "Imagenes", "Login", "background.png"), (800, 500))
        img0 = utl.leer_imagen(os.path.join(project_root, "Imagenes", "Login", "img0.png"), (352, 50))
        img1 = utl.leer_imagen(os.path.join(project_root, "Imagenes", "Login", "img1.png"), (117, 25))
        entry0_img = utl.leer_imagen(os.path.join(project_root, "Imagenes", "Login", "img_textBox0.png"), (352, 33))
        entry1_img = utl.leer_imagen(os.path.join(project_root, "Imagenes", "Login", "img_textBox1.png"), (352, 33))
        
        background = canvas.create_image(
            395, 250,
            image=background_img)
        

        b0 = tk.Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.verificar,
            relief = "flat",
            cursor="hand2")

        b0.place(
            x = 404, y = 355,
            width = 350,
            height = 48)
        
        b0.bind("<Return>", (lambda event: self.verificar()))

        b1 = tk.Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.registrarse,
            relief = "flat",
            cursor="hand2")

        b1.place(
            x = 522, y = 414,
            width = 115,
            height = 23)

        entry0_bg = canvas.create_image(
            578, 288,
            image = entry0_img)

        self.contra = tk.Entry(
            bd = 0,
            bg = "#262626",
            font =("Times", 14), 
            fg = "white",
            highlightthickness = 0)
        
        self.contra.config(show = "*")

        self.contra.place(
            x = 413, y = 272,
            width = 320.0,
            height = 33)

        entry1_bg = canvas.create_image(
            578, 206,
            image = entry1_img)

        self.usuario = tk.Entry(
            bd = 0,
            bg = "#262626",
            font=("Bold", 13),
            fg= "white",
            highlightthickness = 0)

        self.usuario.place(
            x = 413, y = 190,
            width = 320.0,
            height = 33)

        #---------------------------->>> [DATOS DE CUENTA DE PRUEBA PARA REPOSITORIO] >>>-------------------------------------------------
        self.usuario.insert(0, 'Admin')
        self.contra.insert(0, '123456')


        self.window.resizable(False, False)
        self.window.mainloop()


    def verificar(self):


        usu = self.usuario.get()
        password = self.contra.get()

        verif_usu = 'SELECT * FROM usuario WHERE Usuario = ? AND Contraseña = ?'
        self.cursor.execute(verif_usu, (usu, password))
        results = self.cursor.fetchall()

        if results:
            
            variables.logged_user = results[0][0]  # Guarda el Rut del usuario logueado
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(variables.logged_user)
            self.cursor.execute(
                "UPDATE usuario SET Ultima_Conexión = ? WHERE Rut = ?",
                (now, results[0][0])
            )
            self.mydb.commit()
            self.window.destroy()
            MasterPanel()
            
        else:
            messagebox.showerror(message="Usuario no identificado", title="Mensaje")