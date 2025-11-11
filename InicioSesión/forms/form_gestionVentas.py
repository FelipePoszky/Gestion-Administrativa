from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from ttkwidgets.autocomplete import AutocompleteCombobox

import util.generic as utl
import os
import sqlite3

class gestionVentas:

    def volver_inicio(self):
        from forms.form_inventario import inventario
        self.window.destroy()
        inventario()

    def abrir_gestion_productos(self):
        from forms.form_gestionProductos import gestionProductos
        self.window.destroy()
        gestionProductos()

    def abrir_gestion_compras(self):
        from forms.form_gestionCompras import gestionCompras
        self.window.destroy()
        gestionCompras()


    def __init__(self):
        
        img_dir = os.getcwd()

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")

        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()

        self.window = Tk()
        
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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/background.png")
        background = canvas.create_image(
            630, 312.5,
            image=background_img)

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.volver_inicio,
            cursor = "hand2",
            relief = "flat")

        b0.place(
            x = 1192, y = 6,
            width = 58,
            height = 56)

        img1 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.filtrar_ventas,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 1026, y = 111,
            width = 110,
            height = 48)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiar_campos,
            cursor = "hand2",
            relief = "flat")

        b2.place(
            x = 1144, y = 111,
            width = 98,
            height = 48)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_gestion_productos,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 111, y = 10,
            width = 151,
            height = 47)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_gestion_compras,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 286, y = 10,
            width = 150,
            height = 46)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.editar_venta,
            cursor = "hand2",
            relief = "flat")

        b5.place(
            x = 706, y = 529,
            width = 202,
            height = 47)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img6.png")
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.eliminar_venta,
            cursor = "hand2",
            relief = "flat")

        b6.place(
            x = 1069, y = 529,
            width = 138,
            height = 47)

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/Button.png")
        self.b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_calendario,
            cursor = "hand2",
            relief = "flat")
        
        self.b7.place(
            x = 1134, y = 288,
            width = 31,
            height = 30)

        # ------------------------------------------------------------------------------------------

        # Frame Para Sostener Barra lateral y tabla 
        self.frame_treeview = Frame(self.window)
        self.frame_treeview.place(x=17, y=102, height=501, width=605)

        # Scrollbar
        self.scrollVentas = Scrollbar(self.frame_treeview)
        self.scrollVentas.pack(side=LEFT, fill=Y)

        # Tabla Gestion  de Ventas
        self.ventas = ttk.Treeview(self.frame_treeview, columns=(1,2,3,4,5,6), show="headings", height=4, yscrollcommand=self.scrollVentas.set)
        self.scrollVentas.config(command=self.ventas.yview)

        self.ventas.heading(1, text="Fecha")
        self.ventas.heading(2, text="Boleta")
        self.ventas.heading(3, text="Vendedor")
        self.ventas.heading(4, text="Producto")
        self.ventas.heading(5, text="Cantidad")
        self.ventas.heading(6, text="Precio")

        # Configure Treeview columns
        self.ventas.column(1, width=25, anchor=CENTER)
        self.ventas.column(2, width=30, anchor=CENTER)
        self.ventas.column(3, width=80, anchor=W)
        self.ventas.column(4, width=80, anchor=W)
        self.ventas.column(5, width=20, anchor=CENTER)
        self.ventas.column(6, width=25, anchor=CENTER)

        #self.productos.bind('<Double 1>', self.getrowProductos)
        self.actualizar_tabla()

        # Configure Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#464646", fieldbackground="#464646", foreground="white", rowheight=27)
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])

        self.ventas.place(x=17, y=0, width=588, height=501)

        # ------------------------------------------------------------------------------------------

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img_textBox5.png")
        entry0_bg = canvas.create_image(
            904, 133,
            image = entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry0.place(
            x = 793, y = 121,
            width = 213.0,
            height = 25)


        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img_textBox0.png")
        entry1_bg = canvas.create_image(
            987, 224,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry1.place(
            x = 858, y = 212,
            width = 248.0,
            height = 25)
        
        query = "SELECT Nombre FROM usuario"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        self.vendedores = [fila[0] for fila in resultados]

        self.usuarios = StringVar()
        self.usuarios = ''

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img_textBox1.png")
        entry2_bg = canvas.create_image(
            987, 263,
            image = entry2_img)

        self.entry2 = AutocompleteCombobox(
            completevalues=self.usuarios,
        )

        self.entry2.place(
            x = 858, y = 251,
            width = 255,
            height = 25)
        
        self.fecha_venta = StringVar()
        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img_textBox2.png")
        entry3_bg = canvas.create_image(
            987, 302,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            textvariable=self.fecha_venta,
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry3.place(
            x = 858, y = 290,
            width = 255,
            height = 25)
        
        query = "SELECT Nombre FROM producto"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        self.products_list = [fila[0] for fila in resultados]

        self.productos = StringVar()
        self.productos = []

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img_textBox3.png")
        entry4_bg = canvas.create_image(
            987, 380,
            image = entry4_img)

        self.entry4 = AutocompleteCombobox(
            completevalues = self.productos
            )

        self.entry4.place(
            x = 858, y = 368,
            width = 248.0,
            height = 25)

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img_textBox4.png")
        entry5_bg = canvas.create_image(
            987, 419,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry5.place(
            x = 858, y = 407,
            width = 248.0,
            height = 25)
        
        entry6_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Ventas/img_textBox4.png")
        entry6_bg = canvas.create_image(
            987, 458,
            image = entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry6.place(
            x = 858, y = 446,
            width = 248.0,
            height = 25)

        self.filtro_id = None
        self.filtro_producto = None
        self.filtro_rut = None
        self.filtro_fecha = None
        self.filtro_cantidad = None
        self.filtro_precio = None

        self.window.resizable(False, False)
        self.window.mainloop()


    def limpiar_campos(self):

        self.entry1.delete(0, END)
        self.entry1.config(state='readonly')
        self.entry2.delete(0, END)
        self.entry3.config(state='normal')
        self.entry3.delete(0, END)
        self.entry3.config(state='readonly')
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry5.config(state='readonly')
        self.entry6.delete(0, END)
        self.entry6.config(state='readonly')

        self.entry2.set_completion_list(self.usuarios)
        self.entry4.set_completion_list(self.productos)
        self.filtro_id = None
        self.filtro_producto = None


    def editar_venta(self):

        if self.filtro_id and self.filtro_producto:

            if self.entry1.get() == self.filtro_id and self.entry2.get() == self.filtro_rut and self.entry3.get() == self.filtro_fecha and self.entry4.get() == self.filtro_producto and self.entry5.get() == self.filtro_cantidad and self.entry6.get() == self.filtro_precio:
                messagebox.showinfo("Información", "No se han realizado cambios.", parent=self.window)
                return
            
            else:
                if self.entry1.get() == '' or self.entry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '' or self.entry5.get() == '' or self.entry6.get() == '':
                    messagebox.showerror("Error", "Por favor, complete todos los campos para editar la venta.", parent=self.window)
                    return
                
                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar esta venta?")
                if respuesta:
                    query = "SELECT Rut FROM usuario WHERE Nombre = ?"
                    self.cursor.execute(query, (self.entry2.get(),))
                    rut_usuario = self.cursor.fetchone()

                    # Obtener códigos de barra: viejo (filtro) y nuevo (entry4)
                    # filtro_producto y entry4 contienen NOMBRES, la tabla venta usa CÓDIGO_BARRA
                    self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (self.filtro_producto,))
                    row_old = self.cursor.fetchone()
                    old_codigo = row_old[0] if row_old else None

                    self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (self.entry4.get(),))
                    row_new = self.cursor.fetchone()
                    new_codigo = row_new[0] if row_new else None

                    costo_nuevo = self.entry6.get().replace("$", "")

                    if new_codigo is None:
                        messagebox.showerror("Error", f"No se encontró el producto '{self.entry4.get()}' en la BD.", parent=self.window)
                        return

                    query = "UPDATE venta SET Num_Boleta = ?, usuario_Rut = ?, Producto_Código_Barra = ?, Cantidad = ?, Precio = ?, Fecha = ? WHERE Num_Boleta LIKE ? AND Producto_Código_Barra LIKE ?"
                    self.cursor.execute(query, (self.entry1.get(), rut_usuario[0], new_codigo, self.entry5.get(), costo_nuevo, self.entry3.get(), self.filtro_id, old_codigo))

                    for item in self.ventas.get_children():

                        valores = self.ventas.item(item, "values")  # Obtener los valores de la fila
                        if valores[1] == self.filtro_id:  # Comparar con la columna "Num_Boleta" (índice 1)

                            self.ventas.item(item, values=(self.entry3.get(), self.entry1.get(), self.entry2.get(), '', '', ''))
                            for hijo in self.ventas.get_children(item):
                                valores_hijo = self.ventas.item(hijo, "values")
                                if valores_hijo[3] == self.filtro_producto:
                                    print('filtro_producto: {} \nentry4: {}'.format(self.filtro_producto, self.entry4.get()))
                                    self.ventas.item(hijo, values=('', '', '                            - - - ->', self.entry4.get(), self.entry5.get(), f'${costo_nuevo}'))

                    if self.entry4.get() != self.filtro_producto:
                        respuesta = messagebox.askyesno("Confirmar", "Haz modificado el producto de la venta. \n¿Desea ajustar el Stock en el inventario de los productos involucrados?\n{} stock +{}, {} stock -{}.".format(self.filtro_producto, self.filtro_cantidad, self.entry4.get(), self.entry5.get()))
                        if respuesta:
                            # Aumentar stock del producto anterior
                            query = "UPDATE producto SET Cantidad = Cantidad + ? WHERE Nombre = ?"
                            self.cursor.execute(query, (self.filtro_cantidad, self.filtro_producto))
                            # Disminuir stock del nuevo producto
                            query = "UPDATE producto SET Cantidad = Cantidad - ? WHERE Nombre = ?"
                            self.cursor.execute(query, (self.entry5.get(), self.entry4.get()))

                    else:
                        if self.entry5.get() != self.filtro_cantidad:
                            respuesta = messagebox.askyesno("Confirmar", "Haz modificado la cantidad del producto {}. ¿Desea modificar el Stock en el inventario del producto?".format(self.filtro_producto))
                            if respuesta:    
                                if int(self.entry5.get()) < int(self.filtro_cantidad):
                                    diferencia_cantidad = int(self.filtro_cantidad) -  int(self.entry5.get())
                                    query = "UPDATE producto SET Cantidad = Cantidad + ? WHERE Nombre = ?"
                                else:
                                    diferencia_cantidad = int(self.entry5.get()) - int(self.filtro_cantidad)
                                    query = "UPDATE producto SET Cantidad = Cantidad - ? WHERE Nombre = ?"
                                self.cursor.execute(query, (diferencia_cantidad, self.entry4.get()))
                    
                    self.mydb.commit()
                    self.limpiar_campos()

                    return


        elif self.filtro_id and not self.filtro_producto:

            query = "SELECT Código_Barra FROM producto WHERE Nombre = ?"
            self.cursor.execute(query, (self.entry4.get(),))
            row_new = self.cursor.fetchone()
            #print(row_new[0])

            if row_new:

                if self.entry1.get() == '' or self.entry2.get() == '' or self.entry3.get() == '' or self.entry5.get() == '' or self.entry6.get() == '':
                    messagebox.showerror("Error", "Por favor, complete todos los campos si quiere editar un producto de la venta.", parent=self.window)
                    return
            
                costo_nuevo = self.entry6.get().replace("$", "")
                query = "SELECT Rut FROM usuario WHERE Nombre = ?"
                self.cursor.execute(query, (self.entry2.get(),))
                rut_usuario = self.cursor.fetchone()
                
                for item in self.ventas.get_children():
                    producto_existe = False
                    valores = self.ventas.item(item, "values")  # Obtener los valores de la fila
                    if valores[1] == self.filtro_id:  # Comparar con la columna "Num_Boleta" (índice 1)
                        
                        for hijo in self.ventas.get_children(item):

                            valores_hijo = self.ventas.item(hijo, "values")
                            if valores_hijo[3] == self.entry4.get():
                                resultado = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar el producto: {}, de esta venta?".format(valores_hijo[3]))
                                if resultado:
                                    self.ventas.item(item, values=(self.entry3.get(), self.entry1.get(), self.entry2.get(), '', '', ''))
                                    self.ventas.item(hijo, values=('', '', '                            - - - ->', self.entry4.get(), self.entry5.get(), f'${costo_nuevo}'))
                                    query = "UPDATE venta SET Num_Boleta = ?, usuario_Rut = ?, Producto_Código_Barra = ?, Cantidad = ?, Precio = ?, Fecha = ? WHERE Num_Boleta LIKE ? AND Producto_Código_Barra LIKE ?"
                                    self.cursor.execute(query, (self.entry1.get(), rut_usuario[0], row_new[0], self.entry5.get(), costo_nuevo, self.entry3.get(), self.filtro_id, row_new[0]))
                                    producto_existe = True

                        if producto_existe is not True:
                            hijo = self.ventas.get_children(item)
                            if hijo:
                                valores_hijo = self.ventas.item(hijo[0], "values")
                                producto = valores_hijo[3]

                            respuesta = messagebox.askyesno("Confirmar", "¿Desea reemplazar este producto: {} por {} en la venta?".format(producto, self.entry4.get()))
                            if respuesta:
                                query = "SELECT Código_Barra FROM producto WHERE Nombre = ?"
                                self.cursor.execute(query, (producto,))
                                row_old = self.cursor.fetchone()

                                self.ventas.item(hijo[0], values=('', '', '                            - - - ->', self.entry4.get(), self.entry5.get(), f'${costo_nuevo}'))
                                query = "UPDATE venta SET Num_Boleta = ?, usuario_Rut = ?, Producto_Código_Barra = ?, Cantidad = ?, Precio = ?, Fecha = ? WHERE Num_Boleta LIKE ? AND Producto_Código_Barra LIKE ?"
                                self.cursor.execute(query, (self.entry1.get(), rut_usuario[0], row_new[0], self.entry5.get(), costo_nuevo, self.entry3.get(), self.filtro_id, row_old[0]))
                                print(self.cursor.rowcount)

                self.mydb.commit()
                self.limpiar_campos()
                return


            elif self.entry1.get() == self.filtro_id and self.entry2.get() == self.filtro_rut and self.entry3.get() == self.filtro_fecha:
                print('TESTEAR')
                messagebox.showinfo("Información", "No se han realizado cambios.", parent=self.window)
                return

            else:
                self.entry5.delete(0, END)
                self.entry6.delete(0, END)
                print('camino-2')
                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar esta venta?")
                if respuesta:

                    for item in self.ventas.get_children():

                        valores = self.ventas.item(item, "values")  # Obtener los valores de la fila
                        if valores[1] == self.filtro_id:  # Comparar con la columna "Num_Boleta" (índice 1)

                            self.ventas.item(item, values=(self.entry3.get(), self.entry1.get(), self.entry2.get(), '', '', ''))

                    query = "SELECT Rut FROM usuario WHERE Nombre = ?"
                    self.cursor.execute(query, (self.entry2.get(),))
                    resultado = self.cursor.fetchone()

                    query = "UPDATE venta SET Num_Boleta = ?, usuario_Rut = ?, Fecha = ? WHERE Num_Boleta LIKE ?"
                    self.cursor.execute(query, (self.entry1.get(), resultado[0], self.entry3.get(), self.filtro_id))
                    
                    self.mydb.commit()
                    print(self.cursor.rowcount)
                    self.limpiar_campos()
                    return


    def eliminar_venta(self):

        for item in self.ventas.get_children():

            valores = self.ventas.item(item, "values")  # Obtener los valores de la fila
            if valores[1] == self.entry1.get():  # Comparar con la columna "Boleta" (índice 1)
                boleta = self.entry1.get()
                if self.entry4.get():
                    nombre_producto = self.entry4.get()
                    for hijo in self.ventas.get_children(item):
                        valores_hijo = self.ventas.item(hijo, "values")

                        if valores_hijo[3] == nombre_producto:
                            respuesta = messagebox.askyesno("Confirmar", "¿Está seguro que desea ELIMINAR este Producto de la Venta?\n\n> {}".format(nombre_producto))
                            if respuesta:
                                self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (nombre_producto,))
                                codigo_barra = self.cursor.fetchone()[0]
                                query = "DELETE FROM venta WHERE Num_Boleta = ? AND Producto_Código_Barra = ?"
                                self.cursor.execute(query, (boleta, codigo_barra))
                                self.mydb.commit()
                                self.ventas.delete(hijo)
                                self.limpiar_campos()
                                messagebox.showinfo("Éxito", "El Producto '{}' de la Venta con Boleta: {}. \nHa sido Eliminado correctamente.".format(nombre_producto, boleta), parent=self.window)
                            return
                    messagebox.showerror("Error", "El producto especificado no se encuentra en la Venta seleccionada.", parent=self.window)
                    return
                else:
                    respuesta = messagebox.askyesno("Confirmar", "¿Está seguro que desea ELIMINAR toda la Venta?")
                    if respuesta:
                        query = "DELETE FROM venta WHERE Num_Boleta = ?"
                        self.cursor.execute(query, (boleta,))
                        self.mydb.commit()
                        self.ventas.delete(item)
                        self.limpiar_campos()
                        messagebox.showinfo("Éxito", "Venta con Boleta '{}' Eliminada correctamente.".format(boleta), parent=self.window)
                    return


    def filtrar_ventas(self):

        self.filtro_id = None
        self.filtro_producto = None

        # Si entry0 está vacío y hay una selección en la tabla
        if not self.entry0.get():
            selected = self.ventas.selection()

            if selected:
                item = selected[0]
                parent = self.ventas.parent(item)
                self.entry1.config(state='normal')
                self.entry2.set_completion_list(self.vendedores)
                self.entry3.config(state='normal')
                self.entry4.set_completion_list(self.products_list)
                self.entry5.config(state='normal')
                self.entry6.config(state='normal')

                if parent:  # Es una fila hija
                    valores_padre = self.ventas.item(parent, "values")
                    valores_hijo = self.ventas.item(item, "values")
                    # Llena los entrys con datos del padre y del hijo
                    self.entry1.delete(0, END)
                    self.entry1.insert(0, valores_padre[1])     # Id Boleta
                    self.filtro_id = valores_padre[1]
                    self.entry2.delete(0, END)
                    self.entry2.insert(0, valores_padre[2])     # Rut Prov
                    self.filtro_rut = valores_padre[2]
                    self.entry3.delete(0, END)
                    self.entry3.insert(0, valores_padre[0])     # Fecha
                    self.entry3.config(state='readonly')
                    self.filtro_fecha = valores_padre[0]
                    self.entry4.delete(0, END)
                    self.entry4.insert(0, valores_hijo[3])      # Producto
                    self.filtro_producto = valores_hijo[3]
                    self.entry5.delete(0, END)
                    self.entry5.insert(0, valores_hijo[4])      # Cantidad
                    self.filtro_cantidad = valores_hijo[4]
                    self.entry6.delete(0, END)
                    self.entry6.insert(0, valores_hijo[5].replace('$', ''))      # Precio
                    self.filtro_precio = valores_hijo[5].replace('$', '')

                else:  # Es una fila padre
                    valores = self.ventas.item(item, "values")
                    self.entry1.delete(0, END)
                    self.entry1.insert(0, valores[1])  # Id Boleta
                    self.filtro_id = valores[1]
                    self.entry2.delete(0, END)
                    self.entry2.insert(0, valores[2])  # Rut vendedor
                    self.filtro_rut = valores[2]
                    self.entry3.delete(0, END)
                    self.entry3.insert(0, valores[0])  # Fecha
                    self.entry3.config(state='readonly')
                    self.filtro_fecha = valores[0]
                    self.entry4.delete(0, END)
                    self.entry4.insert(0, '')          # Cod Prod vacío
                    self.entry5.delete(0, END)
                    self.entry5.insert(0, '')          # Cantidad vacío
                    self.entry6.delete(0, END)
                    self.entry6.insert(0, '')          # Precio vacío

            return

        # Si entry0 tiene texto, busca en la tabla
        for item in self.ventas.get_children():
            
            valores = self.ventas.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry0.get() or valores[1] == self.entry0.get():  # Comparar con la columna "Rut" (índice 0)

                self.entry1.config(state='normal')
                self.entry2.set_completion_list(self.vendedores)
                self.entry3.config(state='normal')
                self.entry4.set_completion_list(self.products_list)
                self.entry5.config(state='normal')
                self.entry6.config(state='normal')

                self.entry1.delete(0, END)
                self.entry1.insert(0, valores[1])  # Num Boucher
                self.filtro_id = valores[1]
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[2])  # Rut vendedor
                self.filtro_rut = valores[2]
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[0])  # Fecha
                self.entry3.config(state='readonly')
                self.filtro_fecha = valores[0]
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[3])  # Producto
                self.entry5.delete(0, END)
                self.entry5.insert(0, valores[4])  # Cantidad
                self.entry6.delete(0, END)
                self.entry6.insert(0, valores[5])  # Precio


    def actualizar_tabla(self):

        query = """SELECT v.Fecha, v.Num_Boleta, u.Nombre AS usuario, p.Nombre AS producto, v.Cantidad, v.Precio
                FROM venta v
                JOIN usuario u ON v.usuario_Rut = u.Rut
                JOIN producto p ON v.Producto_Código_Barra = p.Código_Barra
                ORDER BY v.Fecha DESC, v.Num_Boleta DESC;""" 
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        self.ventas.delete(*self.ventas.get_children())
        boucher_previo = None
        self.fecha_venta = None

        for idx, i in enumerate(rows):
            num_boleta = i[1]

            if boucher_previo != num_boleta:
                self.fecha_venta = self.ventas.insert(parent='', index='end', values=(i[0], i[1], i[2], '', '', ''))
            
            # Inserta el producto como hijo
            self.ventas.insert(parent=self.fecha_venta, index='end', values=('','','                            - - - ->',i[3], i[4], '${}'.format(i[5])), tags=('detalles_venta',))
            self.ventas.item(self.fecha_venta, open=True)

            boucher_previo = num_boleta


    def abrir_calendario(self):
        
        self.calendario = Toplevel(self.window)
        self.calendario.title("Calendario")
        self.calendario.geometry("300x300")

        self.date = Calendar(self.calendario, select_mode='day', date_pattern='y-mm-dd')
        self.date.pack(side="top", fill="both", expand=True)
        self.aceptar = Button(self.calendario, text="Aceptar", command=self.aceptar_fecha)
        self.aceptar.pack(side="bottom")

    def aceptar_fecha(self):

        # year / month / day
        self.calendario.destroy()
        date = StringVar(value=self.date.get_date())
        self.entry3.config(textvariable=date)
        #self.entry3.insert(0, date)