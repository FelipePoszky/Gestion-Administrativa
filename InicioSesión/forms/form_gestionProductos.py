from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD

import os
import util.generic as utl
import sqlite3


class gestionProductos:

    def volver_inicio(self):
        from forms.form_inventario import inventario
        self.window.destroy()
        inventario()
    
    def abrir_gestion_compras(self):
        from forms.form_gestionCompras import gestionCompras
        self.window.destroy()
        gestionCompras()

    def abrir_gestion_ventas(self):
        from forms.form_gestionVentas import gestionVentas
        self.window.destroy()
        gestionVentas()

    def __init__(self):

        self.window = Tk()
        img_dir = os.getcwd()

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()


        self.window.geometry("1260x625")
        self.window.configure(bg = "#8c8c8c")
        utl.centrar_ventana(self.window, 1260, 625)

        canvas = Canvas(
            self.window,
            bg = "#8c8c8c",
            height = 625,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/background.png")
        background = canvas.create_image(
            630, 312.5,
            image=background_img)

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.editar_producto,
            cursor = "hand2",
            relief = "flat")

        b0.place(
            x = 800, y = 547,
            width = 202,
            height = 47)

        img1 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.eliminar_producto,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 1039, y = 547,
            width = 138,
            height = 47)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.agregar_producto,
            cursor = "hand2",
            relief = "flat")

        b2.place(
            x = 627, y = 547,
            width = 129,
            height = 47)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.filtrar_productos,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 833, y = 245,
            width = 109,
            height = 48)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiar_campos,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 957, y = 245,
            width = 98,
            height = 48)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_gestion_ventas,
            relief = "flat",
            cursor = "hand2")

        b5.place(
            x = 455, y = 10,
            width = 135,
            height = 46)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img6.png")
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_gestion_compras,
            cursor = "hand2",
            relief = "flat")

        b6.place(
            x = 286, y = 10,
            width = 150,
            height = 46)

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img7.png")
        b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.volver_inicio,
            cursor = "hand2",
            relief = "flat")

        b7.place(
            x = 1193, y = 5,
            width = 55,
            height = 56)

        # ---------------------------------------------------------------------------------------------------

        # Create a frame to hold the Treeview and scrollbar
        self.frame_treeview = Frame(self.window)
        self.frame_treeview.place(x=60, y=81, height=146, width=1140)

        # Scrollbar
        self.scrollProductos = Scrollbar(self.frame_treeview)
        self.scrollProductos.pack(side=RIGHT, fill=Y)

        # Tabla Gestion Productos
        self.productos = ttk.Treeview(self.frame_treeview, columns=(1,2,3,4,5,6,7), show="headings", height=4, yscrollcommand=self.scrollProductos.set)
        self.scrollProductos.config(command=self.productos.yview)

        self.productos.heading(1, text="Código Barra", anchor=CENTER)
        self.productos.heading(2, text="Código SKU", anchor=CENTER)
        self.productos.heading(3, text="Nombre", anchor=CENTER)
        self.productos.heading(4, text="Precio", anchor=CENTER)
        self.productos.heading(5, text="Cantidad", anchor=CENTER)      #Nota: Que se calcule el margen solo (que no lo tenga que poner el usuario)
        self.productos.heading(6, text="Medida", anchor=CENTER)
        self.productos.heading(7, text="Categoría", anchor=CENTER)

        self.productos.column(1,width=50, anchor=CENTER)
        self.productos.column(2,width=50, anchor=CENTER)
        self.productos.column(3,width=80, anchor=W)
        self.productos.column(4,width=30, anchor=CENTER)
        self.productos.column(5,width=20, anchor=CENTER)
        self.productos.column(6,width=20, anchor=CENTER)
        self.productos.column(7,width=50, anchor=W)

        #self.productos.bind('<Double 1>', self.getrowProductos)
        self.actualizar_tabla()
        
        # Configure Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#464646", fieldbackground="#464646", foreground="white", rowheight=27, font=("Inter", 10))
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])

        self.productos.place(x=0, y=0, width=1123, height=146)

        # ---------------------------------------------------------------------------------------------------

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox0.png")
        entry0_bg = canvas.create_image(
            624, 267,
            image = entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry0.place(
            x = 447, y = 255,
            width = 340.0,
            height = 25)


        # imagen [x=entry+129, y=entry+12]


        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox1.png")
        entry1_bg = canvas.create_image(
            382, 342,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry1.place(
            x = 253, y = 330,
            width = 248.0,
            height = 25)

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox2.png")
        entry2_bg = canvas.create_image(
            382, 381,
            image = entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry2.place(
            x = 253, y = 369,
            width = 248.0,
            height = 25)

        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox3.png")
        entry3_bg = canvas.create_image(
            382, 420,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry3.place(
            x = 253, y = 408,
            width = 248.0,
            height = 25)

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox4.png")
        entry4_bg = canvas.create_image(
            382, 459,
            image = entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry4.place(
            x = 253, y = 447,
            width = 248.0,
            height = 25)

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox5.png")
        entry5_bg = canvas.create_image(
            382, 498,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry5.place(
            x = 253, y = 486,
            width = 248.0,
            height = 25)

        entry6_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox6.png")
        entry6_bg = canvas.create_image(
            382, 537,
            image = entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry6.place(
            x = 253, y = 525,
            width = 248.0,
            height = 25)

        entry7_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Productos/img_textBox7.png")
        entry7_bg = canvas.create_image(
            382, 576,
            image = entry7_img)

        self.entry7 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry7.place(
            x = 253, y = 564,
            width = 248.0,
            height = 25)

        

        self.window.resizable(False, False)
        self.window.mainloop()


    def limpiar_campos(self):

        self.entry0.delete(0, END)
        self.entry1.delete(0, END)
        self.entry1.config(state='readonly')
        self.entry2.delete(0, END)
        self.entry2.config(state='readonly')
        self.entry3.delete(0, END)
        self.entry3.config(state='readonly')
        self.entry4.delete(0, END)
        self.entry4.config(state='readonly')
        self.entry5.delete(0, END)
        self.entry5.config(state='readonly')
        self.entry6.delete(0, END)
        self.entry6.config(state='readonly')
        self.entry7.delete(0, END)
        self.entry7.config(state='readonly')

        self.seleccion_barra = None
        self.seleccion_sku = None
        self.seleccion_nombre = None
        self.seleccion_categoria = None
        self.seleccion_medida = None
        self.seleccion_cantidad = None
        self.seleccion_precio = None

    def editar_producto(self):

        if self.entry1.get() == '' or self.entry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '' or self.entry5.get() == '' or self.entry6.get() == '' or self.entry7.get() == '':
            messagebox.showwarning("Advertencia", "Debe completar todos los campos para editar un producto") 
            return

        elif self.entry1.get() == self.seleccion_barra and self.entry2.get() == self.seleccion_sku and self.entry3.get() == self.seleccion_nombre and self.entry4.get() == self.seleccion_categoria and self.entry5.get() == self.seleccion_medida and self.entry6.get() == self.seleccion_cantidad and self.entry7.get().replace("$", "") == self.seleccion_precio:
            messagebox.showinfo("Información", "No se han realizado cambios en el producto.")
            return

        for item in self.productos.get_children():
            valores = self.productos.item(item, "values")  # Obtener los valores de la fila

            if valores[0] == self.entry1.get() or valores[1] == self.entry2.get() or valores[2] == self.entry3.get():  # Comparar con la columna "Rut" (índice 0)
                messagebox.showwarning("Advertencia", "El Valor que intenta agregar ya existe en la base de datos.")
                return

        costo_nuevo = self.entry7.get().replace("$", "")

        for item in self.productos.get_children():

            valores = self.productos.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.seleccion_barra or valores[1] == self.seleccion_sku or valores[2] == self.seleccion_nombre:  # Comparar con la columna "Rut" (índice 0)

                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar este producto?")
                if respuesta:
                    query = "UPDATE producto SET Código_Barra = ?, Código_Básico = ?, Nombre = ?, Categoria = ?, Unid_Medida = ?, Cantidad = ?, Precio = ?, Costo = ?, Margen = ? WHERE Código_Barra LIKE ? OR Código_Básico LIKE ? OR Nombre LIKE ?"
                    self.cursor.execute(query, (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get(), costo_nuevo, 0, 0, self.entry1.get(), self.entry2.get(), self.entry3.get()))

                    self.productos.item(item, values=(self.entry1.get(), self.entry2.get(), self.entry3.get(), f'${costo_nuevo}', self.entry6.get(), self.entry5.get(), self.entry4.get()))

                    self.mydb.commit()
                    self.limpiar_campos()


    def filtrar_productos(self):


        if not self.entry0.get():
            selected = self.productos.selection()
            if selected:
                self.entry1.config(state='normal')
                self.entry2.config(state='normal')
                self.entry3.config(state='normal')
                self.entry4.config(state='normal')
                self.entry5.config(state='normal')
                self.entry6.config(state='normal')
                self.entry7.config(state='normal')

                item = selected[0]
                valores = self.productos.item(item, "values")
                self.entry1.delete(0, END)
                self.entry1.insert(0, valores[0])  # Cod. Barra
                self.seleccion_barra = valores[0]
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[1])  # Cod. Basico
                self.seleccion_sku = valores[1]
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[2])  # Nombre
                self.seleccion_nombre = valores[2]
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[6])  # Categoria
                self.seleccion_categoria = valores[6]
                self.entry5.delete(0, END)
                self.entry5.insert(0, valores[5])  # Unid medida
                self.seleccion_medida = valores[5]
                self.entry6.delete(0, END)
                self.entry6.insert(0, valores[4])  # Cantidad
                self.seleccion_cantidad = valores[4]
                self.entry7.delete(0, END)
                self.entry7.insert(0, valores[3].replace("$", ""))  # Precio
                self.seleccion_precio = valores[3].replace("$", "")

            return

        # Si el entry no está vacío, buscar en la tabla

        for item in self.productos.get_children():

            valores = self.productos.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry0.get() or valores[1] == self.entry0.get() or valores[2] == self.entry0.get():  # Comparar con la columna "Rut" (índice 0)
                self.entry1.config(state='normal')
                self.entry2.config(state='normal')
                self.entry3.config(state='normal')
                self.entry4.config(state='normal')
                self.entry5.config(state='normal')
                self.entry6.config(state='normal')
                self.entry7.config(state='normal')

                self.entry1.delete(0, END)
                self.entry1.insert(0, valores[0])  # Cod. Barra
                self.seleccion_barra = valores[0]
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[1])  # Cod. Basico
                self.seleccion_sku = valores[1]
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[2])  # Nombre
                self.seleccion_nombre = valores[2]
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[6])  # Categoria
                self.seleccion_categoria = valores[6]
                self.entry5.delete(0, END)
                self.entry5.insert(0, valores[5])  # Unid medida
                self.seleccion_medida = valores[5]
                self.entry6.delete(0, END)
                self.entry6.insert(0, valores[4])  # Cantidad
                self.seleccion_cantidad = valores[4]
                self.entry7.delete(0, END)
                self.entry7.insert(0, valores[3].replace("$", ""))  # Precio
                self.seleccion_precio = valores[3].replace("$", "")

    
    def agregar_producto(self):

        if self.entry1.get() == '' or self.entry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '' or self.entry5.get() == '' or self.entry6.get() == '' or self.entry7.get() == '':
            messagebox.showwarning("Advertencia", "Debe completar todos los campos para agregar un producto") 
            return
        
        if self.seleccion_barra is not None or self.seleccion_sku is not None or self.seleccion_nombre is not None:
            if (self.entry1.get() == self.seleccion_barra) or (self.entry2.get() == self.seleccion_sku) or (self.entry3.get() == self.seleccion_nombre):
                messagebox.showwarning("Advertencia", "El producto que intenta agregar ya existe en la base de datos.")
                return


        for item in self.productos.get_children():
            valores = self.productos.item(item, "values")  # Obtener los valores de la fila

            if valores[0] == self.entry1.get() or valores[1] == self.entry2.get() or valores[2] == self.entry3.get():  # Comparar con la columna "Rut" (índice 0)
                messagebox.showwarning("Advertencia", "El producto que intenta agregar ya existe en la base de datos.")
                return

        cod_barra = self.entry1.get()
        cod_basico = self.entry2.get()
        nombre = self.entry3.get()
        categoria = self.entry4.get()
        unid_medida = self.entry5.get()
        cantidad = self.entry6.get()
        precio = self.entry7.get()

        query = "INSERT INTO producto (Código_Barra, Código_Básico, Nombre, Precio, Categoria, Cantidad, Unid_Medida, Costo, Margen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (cod_barra, cod_basico, nombre, precio, categoria, cantidad, unid_medida, 0, 0))

        if self.cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "producto agregado exitosamente.")
            #self.mydb.commit()
        else:
            messagebox.showerror("Error", "No se pudo agregar el producto.")
        self.actualizar_tabla()


    def eliminar_producto(self):

        for item in self.productos.get_children():

            valores = self.productos.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry1.get() or valores[1] == self.entry2.get() or valores[2] == self.entry3.get():  # Comparar con la columna "Rut" (índice 0)

                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea ELIMINAR el siguiente Producto?\n\n> {}".format(self.entry3.get()))
                if respuesta:
                    query = "DELETE FROM producto WHERE Código_Barra = ? OR Código_Básico = ?"
                    self.cursor.execute(query, (self.entry1.get(), self.entry2.get()))
                    #self.mydb.commit()
                    self.actualizar_tabla()
                    messagebox.showinfo("Éxito", f"Producto '{self.entry1.get()}' eliminado correctamente.", parent=self.window)
                return


    def actualizar_tabla(self):

        query = "SELECT Código_barra, Código_básico, Nombre, Precio, Cantidad, Unid_Medida, Categoria FROM producto"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        self.productos.delete(*self.productos.get_children())
        for i in rows:
            self.productos.insert('', 'end', values=(i[0], i[1], i[2], '${}'.format(i[3]), i[4], i[5], i[6]))