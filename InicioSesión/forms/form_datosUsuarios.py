from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD

import util.generic as utl
import sqlite3
import os

class DatosUsuarios:

    def volverInicio(self):
        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()
    
    def abrirDatosLocal(self):

        from forms.form_datosLocal import DatosLocal
        self.window.destroy()
        DatosLocal()
    
    def abrirDatosProveedores(self):

        from forms.form_datosProveedores import DatosProveedores
        self.window.destroy()
        DatosProveedores()

    def __init__(self):

        self.window = Tk()
        img_dir = os.getcwd()

        self.window.geometry("1260x625")
        self.window.configure(bg = "#8c8c8c")
        utl.centrar_ventana(self.window, 1260, 625)

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()

        canvas = Canvas(
            self.window,
            bg = "#8c8c8c",
            height = 625,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/background.png")
        background = canvas.create_image(
            630, 312.5,
            image=background_img)

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.editar_usuario,
            cursor = "hand2",
            relief = "flat")
        
        b0.place(
            x = 851, y = 535,
            width = 202,
            height = 47)

        img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.volverInicio,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 1193, y = 7,
            width = 55,
            height = 57)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.eliminar_usuario,
            cursor = "hand2",
            relief = "flat")

        b2.place(
            x = 1085, y = 535,
            width = 138,
            height = 47)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.agregar_usuario,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 690, y = 535,
            width = 129,
            height = 47)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.filtrar_usuarios,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 1026, y = 124,
            width = 112,
            height = 48)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiar_campos,
            cursor = "hand2",
            relief = "flat")

        b5.place(
            x = 1144, y = 124,
            width = 100,
            height = 48)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img6.png")
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrirDatosLocal,
            cursor = "hand2",
            relief = "flat")

        b6.place(
            x = 121, y = 13,
            width = 118,
            height = 45)

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img7.png")
        b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrirDatosProveedores,
            cursor = "hand2",
            relief = "flat")

        b7.place(
            x = 257, y = 13,
            width = 164,
            height = 45)

        # ----------[ TreeView ]------------------------
        self.usuarios = ttk.Treeview(self.window, columns=(1,2,3,4,5,6), show="headings", height=4)
        
        self.usuarios.heading(1, text="Rut")
        self.usuarios.heading(2, text="Nombre")
        self.usuarios.heading(3, text="Contacto")
        self.usuarios.heading(4, text="Puesto")
        self.usuarios.heading(5, text="Usuario")
        self.usuarios.heading(6, text="Contraseña")

        self.usuarios.column(1, width=40, anchor=CENTER)
        self.usuarios.column(2, width=80, anchor=W)
        self.usuarios.column(3, width=80, anchor=W)
        self.usuarios.column(4, width=40, anchor=W)
        self.usuarios.column(5, width=40, anchor=CENTER)
        self.usuarios.column(6, width=50, anchor=CENTER)

        query = "SELECT Rut, Nombre, Num_Contacto, Tipo_Usuario, Usuario, Contraseña FROM usuario"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for row in rows:
            self.usuarios.insert("", "end", values=row)

        # Configuración Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#464646", fieldbackground="#464646", foreground="white", rowheight=27)
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])

        self.usuarios.place(x=17, y=102, width=580, height=501)


        # -----------------------------------------------------------------------------------------
        # ---> Buscador

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox0.png")
        entry0_bg = canvas.create_image(
            901, 148,
            image = entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry0.place(
            x = 790, y = 136,
            width = 213.0,
            height = 25)
        # ----------------------------------------------------------------------------------------

        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox1.png")
        entry1_bg = canvas.create_image(
            970, 276,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry1.place(
            x = 841, y = 264,
            width = 248.0,
            height = 25)

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox2.png")
        entry2_bg = canvas.create_image(
            970, 319,
            image = entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry2.place(
            x = 841, y = 307,
            width = 248.0,
            height = 25)

        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox3.png")
        entry3_bg = canvas.create_image(
            970, 362,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry3.place(
            x = 841, y = 350,
            width = 248.0,
            height = 25)

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox4.png")
        entry4_bg = canvas.create_image(
            970, 405,
            image = entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry4.place(
            x = 841, y = 393,
            width = 248.0,
            height = 25)

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox5.png")
        entry5_bg = canvas.create_image(
            970, 448,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry5.place(
            x = 841, y = 436,
            width = 248.0,
            height = 25)

        entry6_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox6.png")
        entry6_bg = canvas.create_image(
            970, 491,
            image = entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry6.place(
            x = 841, y = 479,
            width = 248.0,
            height = 25)

        self.window.resizable(False, False)
        self.window.mainloop()

#  Limpiar los campos de entrada
    def limpiar_campos(self):

        self.entry0.delete(0, END)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)

# Editar usuario seleccionado
    def editar_usuario(self):

        if not self.entry1.get() or not self.entry2.get() or not self.entry5.get() or not self.entry6.get():
            messagebox.showerror("Error", "Por favor, complete los campos obligatorios: Rut, Nombre, Usuario y Contraseña.")
            return

        for item in self.usuarios.get_children():

            valores = self.usuarios.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry1.get() or valores[1] == self.entry2.get() or valores[4] == self.entry5.get():  # Comparar con la columna "Rut" (índice 0)

                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar este usuario?")
                if respuesta:

                    query = "UPDATE usuario SET Rut = ?, Nombre = ?, Num_Contacto = ?, Tipo_Usuario = ?, Usuario = ?, Contraseña = ? WHERE Rut LIKE ? OR Nombre LIKE ?"
                    self.cursor.execute(query, (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get(), self.entry1.get(), self.entry2.get()))
                    self.mydb.commit()
                    self.actualizar_tabla()

# Filtrar usuarios en la tabla
    def filtrar_usuarios(self):

        if not self.entry0.get():
            selected = self.usuarios.selection()
            if selected:
                item = selected[0]
                valores = self.usuarios.item(item, "values")
                self.entry1.delete(0, END)
                self.entry1.insert(0, valores[0])  # Rut
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[1])  # Nombre
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[2])  # Telefono
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[3])  # Puesto
                self.entry5.delete(0, END)
                self.entry5.insert(0, valores[4])  # Usuario
                self.entry6.delete(0, END)
                self.entry6.insert(0, valores[5])  # Contraseña

            return

        # Si el entry no está vacío, buscar en la tabla

        for item in self.usuarios.get_children():

            valores = self.usuarios.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry0.get() or valores[1] == self.entry0.get() or valores[2] == self.entry0.get():  # Comparar con la columna "Rut" (índice 0)

                self.entry1.delete(0, END)
                self.entry1.insert(0, valores[0])  # Rut
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[1])  # Nombre
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[2])  # Telefono
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[3])  # Puesto
                self.entry5.delete(0, END)
                self.entry5.insert(0, valores[4])  # Usuario
                self.entry6.delete(0, END)
                self.entry6.insert(0, valores[5])  # Contraseña

# Agregar nuevo usuario a la base de datos
    def agregar_usuario(self):

        if not self.entry1.get() or not self.entry2.get() or not self.entry5.get():
            messagebox.showerror("Error", "Por favor, complete los campos obligatorios: Rut, Nombre y Usuario.")
            return
        
        rut = self.entry1.get()
        nombre = self.entry2.get()
        telefono = self.entry3.get()
        puesto = self.entry4.get()
        usuario = self.entry5.get()
        contraseña = self.entry6.get()

        query = f"INSERT INTO usuario (Rut, Nombre, Num_Contacto, Tipo_Usuario, Usuario, Contraseña) VALUES ('{rut}', '{nombre}', '{telefono}', '{puesto}', '{usuario}', '{contraseña}')"
        self.cursor.execute(query)
        
        if self.cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Usuario agregado exitosamente.")
            self.mydb.commit()
        else:
            messagebox.showerror("Error", "No se pudo agregar el usuario.")

        self.actualizar_tabla()

# Eliminar usuario seleccionado de la base de datos
    def eliminar_usuario(self):

        for item in self.usuarios.get_children():

            valores = self.usuarios.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry1.get():  # Comparar con la columna "Rut" (índice 0)

                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este usuario?")
                if respuesta:
                    query = "DELETE FROM usuario WHERE Rut = ?"
                    self.cursor.execute(query, (self.entry1.get(),))
                    self.mydb.commit()
                    self.actualizar_tabla()
                    messagebox.showinfo("Éxito", f"Usuario '{self.entry1.get()}' eliminado correctamente.", parent=self.window)
                return

# Actualiza la treeview de usuarios
    def actualizar_tabla(self):

        query = "SELECT Rut, Nombre, Num_Contacto, Tipo_Usuario, Usuario, Contraseña FROM usuario"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        self.usuarios.delete(*self.usuarios.get_children())
        for row in rows:
            self.usuarios.insert("", "end", values=row)