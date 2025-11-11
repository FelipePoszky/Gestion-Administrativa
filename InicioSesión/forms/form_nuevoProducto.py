from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import BOLD

import util.generic as utl
import util.variables as variables
import os
import sqlite3

class nuevo:

    def __init__(self, compras_win=None):

        img_dir = os.getcwd()
        self.compras_win = compras_win

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()

        self.ventEmergente = Toplevel()

        self.ventEmergente.geometry("1109x625")
        self.ventEmergente.configure(bg = "#8c8c8c")
        utl.centrar_ventana(self.ventEmergente, 1038, 546)

        canvas = Canvas(
            self.ventEmergente,
            bg = "#8c8c8c",
            height = 546,
            width = 1038,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/Background.png")
        background = canvas.create_image(
            519, 273,
            image=background_img)

        # x = + 129, y = + 12
        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry1_bg = canvas.create_image(
            514, 196,
            image = entry1_img)

        self.entry1 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry1.place(
            x = 385, y = 184,
            width = 248.0,
            height = 25)

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry2_bg = canvas.create_image(
            514, 235,
            image = entry2_img)

        self.entry2 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry2.place(
            x = 385, y = 223,
            width = 248.0,
            height = 25)

        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry3_bg = canvas.create_image(
            514, 274,
            image = entry3_img)

        self.entry3 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry3.place(
            x = 385, y = 262,
            width = 248.0,
            height = 25)

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry4_bg = canvas.create_image(
            514, 313,
            image = entry4_img)

        self.entry4 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry4.place(
            x = 385, y = 301,
            width = 248.0,
            height = 25)

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry5_bg = canvas.create_image(
            514, 352,
            image = entry5_img)

        self.entry5 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry5.place(
            x = 385, y = 340,
            width = 248.0,
            height = 25)

        entry6_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry6_bg = canvas.create_image(
            514, 391,
            image = entry6_img)

        self.entry6 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry6.place(
            x = 385, y = 379,
            width = 248.0,
            height = 25)

        entry7_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry7_bg = canvas.create_image(
            514, 430,
            image = entry7_img)

        self.entry7 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry7.place(
            x = 385, y = 418,
            width = 248.0,
            height = 25)

        entry8_img = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/TextBox.png")
        entry8_bg = canvas.create_image(
            514, 469,
            image = entry8_img)

        self.entry8 = Entry(
            self.ventEmergente,
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry8.place(
            x = 385, y = 457,
            width = 248.0,
            height = 25)

        # ------------------------------------  Botones ---------------------->>>>>>>

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/Button.png")
        b4 = Button(
            self.ventEmergente,
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.agregar_producto,
            relief = "flat")
        b4.place(
            x = 375, y = 496,
            width = 278,
            height = 36)


        img5 = PhotoImage(file = f"{img_dir}/Imagenes/Nuevo Producto/Button (1).png")
        b5 = Button(
            self.ventEmergente,
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.lector_barra,
            relief = "flat")
        b5.place(
            x = 668, y = 181,
            width = 32,
            height = 32)

        # ------------------------>>>>>>> [ Tabla ] ------------------------------>>>>>>>>>>>>

        self.producto = ttk.Treeview(self.ventEmergente, columns=(1,2,3,4,5,6,7,8,9), show="headings", height=4)

        self.producto.heading(1, text="Cód. Barra")
        self.producto.heading(2, text="Cód. Secundario")
        self.producto.heading(3, text="Categoria")
        self.producto.heading(4, text="Nombre")
        self.producto.heading(5, text="Medida")
        self.producto.heading(6, text="Cantidad")
        self.producto.heading(7, text="Precio")
        self.producto.heading(8, text="Costo")
        self.producto.heading(9, text="Margen")

        self.producto.column(1, width=80, anchor=CENTER)
        self.producto.column(2, width=80, anchor=CENTER)
        self.producto.column(3, width=80, anchor=W)
        self.producto.column(4, width=80, anchor=W)
        self.producto.column(5, width=30, anchor=CENTER)
        self.producto.column(6, width=30, anchor=CENTER)
        self.producto.column(7, width=30, anchor=CENTER)
        self.producto.column(8, width=30, anchor=CENTER)
        self.producto.column(9, width=30, anchor=CENTER)

        # Configuración Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#343434", fieldbackground="#343434", foreground="white", rowheight=30, font=("Helvetica", 9, BOLD))
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])

        self.producto.place(x=36, y=82, width=966, height=68)

        self.ventEmergente.resizable(False, False)
        self.ventEmergente.mainloop()

# Agrega un nuevo producto a la base de datos
    def agregar_producto(self):

        cod_barra = self.entry1.get()
        cod_basico = self.entry2.get()
        nombre = self.entry3.get()
        categoria = self.entry4.get()
        unid_medida = self.entry5.get()
        cantidad = self.entry6.get()
        precio = self.entry7.get()
        costo = self.entry8.get()
        margen = float(precio) - float(costo)

        datos = [cod_barra, cod_basico, categoria, nombre, unid_medida, cantidad, f'$ {precio}', f'$ {costo}', f'$ {margen}']

        query = "INSERT INTO producto (Código_Barra, Código_Básico, Nombre, Precio, Costo, Margen, Categoria, Cantidad, Unid_Medida) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (cod_barra, cod_basico, nombre, precio, costo, margen, categoria, cantidad, unid_medida))
        
        if self.cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "producto agregado exitosamente.")
            self.mydb.commit()
            variables.products_list.insert(0, nombre)
            print(variables.products_list)

            if self.compras_win and hasattr(self.compras_win, 'ident_prod'):
                self.compras_win.ident_prod.set_completion_list(variables.products_list)

            elif self.compras_win and hasattr(self.compras_win, 'updateProductos'):
                self.compras_win.updateProductos()

        else:
            messagebox.showerror("Error", "No se pudo agregar el producto.")
        self.actualizar_tabla(datos)

# Actualiza la tabla de productos con los nuevos datos
    def actualizar_tabla(self, datos):

        self.producto.delete(*self.producto.get_children())
        self.producto.insert("", "end", values=datos)

    def lector_barra(self):
        return