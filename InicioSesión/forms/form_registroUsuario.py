from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD

import util.variables as variables
import util.generic as utl
import os
import sqlite3


class registro:

# -----------------------------[ Moverse entre ventanas ]------------------------- #
    def volver_login(self):

        from forms.form_login import app
        self.window.destroy()
        app()

    def ingresar_usuario(self):

        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()


    def __init__(self):

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()    
        
        img_dir = os.getcwd()
        self.admin = False

        self.window = Tk()

        self.window.geometry("800x500")
        self.window.configure(bg = "#8c8c8c")
        utl.centrar_ventana(self.window, 800, 500)
        
        canvas = Canvas(
            self.window,
            bg = "#8c8c8c",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        self.cursor.execute("SELECT COUNT(*) FROM usuario")
        resultado = self.cursor.fetchone()[0]

        if resultado > 0:   # Si ya hay usuarios registrados, mostrar el fondo para registro de usuario normal
            background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/background.png")
            self.background = canvas.create_image(
                400, 250,
                image=background_img)
            
        else:               # Si no hay usuarios registrados, mostrar el fondo para registro de administrador
            background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/background_admin.png")
            self.background = canvas.create_image(
                400, 250,
                image=background_img)
            
            self.admin = True
        
        # x = +165, y = +16
        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/TextBox.png")
        entry0_bg = canvas.create_image(
            582, 81,
            image = entry0_img)
    
        self.entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            font =("Inter", 12), 
            fg = "#262626",
            highlightthickness = 0)
        
        self.entry0.place(
            x = 421, y = 66,
            width = 310,
            height = 31)
        
        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/TextBox.png")
        entry1_bg = canvas.create_image(
            582, 155,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            font =("Inter", 12), 
            fg = "#262626",
            highlightthickness = 0)

        self.entry1.place(
            x = 421, y = 141,
            width = 310,
            height = 30)
    
        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/TextBox.png")
        entry2_bg = canvas.create_image(
            582, 229,
            image = entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            font =("Inter", 12), 
            fg = "#262626",
            highlightthickness = 0)

        self.entry2.place(
            x = 421, y = 215,
            width = 310,
            height = 30)
        
        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/TextBox.png")
        entry3_bg = canvas.create_image(
            582, 303,
            image = entry3_img)
    
        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            font =("Inter", 12), 
            fg = "#262626",
            highlightthickness = 0)

        self.entry3.place(
            x = 421, y = 289,
            width = 310,
            height = 30)

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/TextBox.png")
        entry4_bg = canvas.create_image(
            582, 377,
            image = entry4_img)
        
        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            font =("Inter", 12),
            fg = "#262626",
            highlightthickness = 0)

        self.entry4.place(
            x = 421, y = 363,
            width = 310,
            height = 30)

        b0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/Button0.png")
        b0 = Button(
            image = b0_img,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.registrar,
            relief = "flat",
            cursor="hand2")
        
        b0.place(
            x = 406, y = 425,
            width = 351,
            height = 50)

        b1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Registro/Button1.png")
        b1 = Button(
            image = b1_img,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.volver_login,
            relief = "flat",
            cursor="hand2")

        b1.place(
            x = 741, y = 7,
            width = 49,
            height = 49)

        self.window.resizable(False, False)
        self.window.mainloop()

# Registrar nuevo usuario en la base de datos
    def registrar(self):

        if not self.entry0.get() or not self.entry1.get() or not self.entry2.get() or not self.entry3.get() or not self.entry4.get():
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        
        if self.admin:
            query = "INSERT INTO usuario (Rut, Nombre, Tipo_Usuario, Num_Contacto, Contraseña, Usuario) VALUES (?, ?, ?, ?, ?, ?)"
            values = (self.entry1.get(), self.entry0.get(), "Administrador", self.entry2.get(), self.entry4.get(), self.entry3.get())

        else:
            query = "INSERT INTO usuario (Rut, Nombre, Tipo_Usuario, Num_Contacto, Contraseña, Usuario) VALUES (?, ?, ?, ?, ?, ?)"
            values = (self.entry1.get(), self.entry0.get(), "Usuario", self.entry2.get(), self.entry4.get(), self.entry3.get())
        
        self.cursor.execute(query, values)
        self.mydb.commit()

        variables.logged_user = self.entry0.get()
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        self.ingresar_usuario()