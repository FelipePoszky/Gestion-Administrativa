from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD

from ttkwidgets.autocomplete import AutocompleteCombobox

import util.generic as utl
import os
import sqlite3

class gestionCompras:

#---------------------------->>> [FUNCIONES DE LLAMADO A OTRAS VENTANAS] >>>-------------------------------------------------
    def volver_inicio(self):
        from forms.form_inventario import inventario
        self.window.destroy()
        inventario()

    def abrir_gestion_productos(self):
        from forms.form_gestionProductos import gestionProductos
        self.window.destroy()
        gestionProductos()

    def abrir_gestion_ventas(self):
        from forms.form_gestionVentas import gestionVentas
        self.window.destroy()
        gestionVentas()

#---------------------------->>> [FUNCIONES DE LA VENTANA] >>>-------------------------------------------------
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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/background.png")
        background = canvas.create_image(
            630, 312.5,
            image=background_img)


        img0 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.volver_inicio,
            cursor = "hand2",
            relief = "flat")

        b0.place(
            x = 1192, y = 7,
            width = 57,
            height = 57)

        img1 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.editar_compra,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 697, y = 550,
            width = 202,
            height = 47)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.eliminar_compra,
            cursor = "hand2",
            relief = "flat")

        b2.place(
            x = 1086, y = 550,
            width = 138,
            height = 47)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.filtrar_compras,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 1027, y = 111,
            width = 108,
            height = 48)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiar_campos,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 1143, y = 111,
            width = 98,
            height = 48)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_gestion_ventas,
            cursor = "hand2",
            relief = "flat")

        b5.place(
            x = 454, y = 10,
            width = 137,
            height = 47)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img6.png")
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_gestion_productos,
            cursor = "hand2",
            relief = "flat")

        b6.place(
            x = 111, y = 10,
            width = 151,
            height = 47)

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/Button.png")
        self.b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_calendario,
            cursor = "hand2",
            relief = "flat")
        
        self.b7.place(
            x = 1134, y = 290,
            width = 31,
            height = 30)

        # ---------------------------------------------------------------------------------------------------------

        # Create a frame to hold the Treeview and scrollbar
        self.frame_treeview = Frame(self.window)
        self.frame_treeview.place(x=17, y=102, height=501, width=605)

        # Scrollbar
        self.scrollCompras = Scrollbar(self.frame_treeview)
        self.scrollCompras.pack(side=LEFT, fill=Y)

        # Tabla Gestion Compras
        self.compras = ttk.Treeview(self.frame_treeview, columns=(1,2,3,4,5,6,7), show="headings", height=4, yscrollcommand=self.scrollCompras.set)
        self.scrollCompras.config(command=self.compras.yview)

        self.compras.heading(1, text="Fecha")
        self.compras.heading(2, text="ID")
        self.compras.heading(3, text="Formato")
        self.compras.heading(4, text="Proveedor")
        self.compras.heading(5, text="Producto")
        self.compras.heading(6, text="Cantidad")
        self.compras.heading(7, text="Costo")
        
        
        self.compras.column(1, width=25, anchor=CENTER)
        self.compras.column(2, width=4, anchor=CENTER)
        self.compras.column(3, width=20, anchor=W)
        self.compras.column(4, width=85, anchor=W)
        self.compras.column(5, width=85, anchor=W)
        self.compras.column(6, width=20, anchor=CENTER)
        self.compras.column(7, width=20, anchor=CENTER)

        #self.productos.bind('<Double 1>', self.getrowProductos)
        self.actualizar_tabla()

        # Configure Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#464646", fieldbackground="#464646", foreground="white", rowheight=27)
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])

        self.compras.place(x=17, y=0, width=588, height=501)

        # ---------------------------------------------------------------------------------------------------------

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox0.png")
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

        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox1.png")
        entry1_bg = canvas.create_image(
            987, 226,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry1.place(
            x = 858, y = 214,
            width = 248.0,
            height = 25)

        self.proveedores = StringVar()

        query = "SELECT Razon_Social FROM proveedor"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        self.listado = [fila[0] for fila in resultados]

        self.proveedores = ''

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox2.png")
        entry2_bg = canvas.create_image(
            987, 265,
            image = entry2_img)

        self.entry2 = AutocompleteCombobox(
            completevalues=self.proveedores,

        )

        self.entry2.place(
            x = 858, y = 253,
            width = 255,
            height = 25)

        self.fecha_compra = StringVar()
        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox3.png")
        entry3_bg = canvas.create_image(
            987, 304,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.fecha_compra,
            state = "readonly",
            highlightthickness = 0)

        self.entry3.place(
            x = 858, y = 292,
            width = 248.0,
            height = 25)

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox4.png")
        entry4_bg = canvas.create_image(
            987, 343,
            image = entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry4.place(
            x = 858, y = 331,
            width = 248.0,
            height = 25)

        query = "SELECT Nombre FROM producto"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        self.products_list = [fila[0] for fila in resultados]

        self.productos = StringVar()
        self.productos = ''

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox5.png")
        entry5_bg = canvas.create_image(
            987, 421,
            image = entry5_img)

        self.entry5 = AutocompleteCombobox(
            completevalues = self.productos
            )

        self.entry5.place(
            x = 858, y = 409,
            width = 255,
            height = 25)

        entry6_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox6.png")
        entry6_bg = canvas.create_image(
            987, 460,
            image = entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry6.place(
            x = 858, y = 448,
            width = 248.0,
            height = 25)

        entry7_img = PhotoImage(file = f"{img_dir}/Imagenes/G. Compras/img_textBox7.png")
        entry7_bg = canvas.create_image(
            987, 499,
            image = entry7_img)

        self.entry7 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",
            highlightthickness = 0)

        self.entry7.place(
            x = 858, y = 487,
            width = 248.0,
            height = 25)

        self.busqueda_id = None
        self.busqueda_producto = None
        self.busqueda_prov = None
        self.busqueda_fecha = None
        self.busqueda_formato = None
        self.busqueda_cantidad = None
        self.busqueda_precio = None

        self.window.resizable(False, False)
        self.window.mainloop()
    
    def limpiar_campos(self):

        self.entry0.delete(0, END)
        self.entry1.delete(0, END)
        self.entry1.config(state='readonly')
        self.entry2.delete(0, END)
        self.entry3.config(state='normal')
        self.entry3.delete(0, END)
        self.entry3.config(state='readonly')
        self.entry4.delete(0, END)
        self.entry4.config(state='readonly')
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry6.config(state='readonly')
        self.entry7.delete(0, END)
        self.entry7.config(state='readonly')

        self.proveedores = []
        self.productos = []
        self.entry2.set_completion_list(self.proveedores)
        self.entry5.set_completion_list(self.productos)
        self.busqueda_id = None
        self.busqueda_producto = None


    def editar_compra(self):

        if self.busqueda_id and self.busqueda_producto:

            if self.entry1.get() == self.busqueda_id and self.entry2.get() == self.busqueda_prov and self.entry3.get() == self.busqueda_fecha and self.entry4.get() == self.busqueda_formato and self.entry5.get() == self.busqueda_producto and self.entry6.get() == self.busqueda_cantidad and self.entry7.get() == self.busqueda_precio:
                messagebox.showinfo("Información", "No se han realizado cambios en la compra.", parent=self.window)
                return

            else:
                if self.entry1.get() == '' or self.entry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '' or self.entry5.get() == '' or self.entry6.get() == '' or self.entry7.get() == '':
                    messagebox.showerror("Error", "Por favor, complete todos los campos para editar la compra.", parent=self.window)
                    return

                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar esta compra?")
                if respuesta:

                    self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (self.busqueda_producto,))
                    row_old = self.cursor.fetchone()
                    old_codigo = row_old[0] if row_old else None

                    self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (self.entry5.get(),))
                    row_new = self.cursor.fetchone()
                    new_codigo = row_new[0] if row_new else None

                    costo_nuevo = self.entry7.get().replace("$", "")

                    query = "SELECT Rut FROM proveedor WHERE Razon_Social = ?"
                    self.cursor.execute(query, (self.entry2.get(),))
                    rut_prov = self.cursor.fetchone()

                    if new_codigo is None:
                        messagebox.showerror("Error", f"No se encontró el producto '{self.entry5.get()}' en la BD.", parent=self.window)
                        return
                    
                    query = "UPDATE compra SET Id = ?, proveedor_Rut = ?, Fecha = ?, Producto_Código_Barra = ?, Cantidad = ?, Precio = ?, Formato = ? WHERE Id LIKE ? AND Producto_Código_Barra LIKE ?"
                    self.cursor.execute(query, (self.entry1.get(), rut_prov[0], self.entry3.get(), new_codigo, self.entry6.get(), costo_nuevo, self.entry4.get(), self.busqueda_id, old_codigo))

                    for item in self.compras.get_children():

                        valores = self.compras.item(item, "values")  # Obtener los valores de la fila
                        if valores[1] == self.busqueda_id:  # Comparar con la columna "Num_Boleta" (índice 1)

                            self.compras.item(item, values=(self.entry3.get(), self.entry1.get(), self.entry4.get(), self.entry2.get(), '', '', ''))
                            for hijo in self.compras.get_children(item):
                                valores_hijo = self.compras.item(hijo, "values")
                                if valores_hijo[4] == self.busqueda_producto:
                                    self.compras.item(hijo, values=('','','','                                 >>>',self.entry5.get(), self.entry6.get(), f'${costo_nuevo}'))

                    if self.entry5.get() != self.busqueda_producto:
                        respuesta = messagebox.askyesno("Confirmar", "Haz modificado el producto de la compra. \n¿Desea ajustar el Stock en el inventario de los productos involucrados?\n{} stock -{}, {} stock +{}.".format(self.busqueda_producto, self.busqueda_cantidad, self.entry5.get(), self.entry6.get()))
                        if respuesta:
                            # Disminuir stock del producto anterior
                            query = "UPDATE producto SET Cantidad = Cantidad - ? WHERE Nombre = ?"
                            self.cursor.execute(query, (self.busqueda_cantidad, self.busqueda_producto))

                            # Aumentar stock del nuevo producto
                            query = "UPDATE producto SET Cantidad = Cantidad + ? WHERE Nombre = ?"
                            self.cursor.execute(query, (self.entry6.get(), self.entry5.get()))

                    else:
                        if self.entry6.get() != self.busqueda_cantidad:
                            respuesta = messagebox.askyesno("Confirmar", "Haz modificado la cantidad de la compra. \n¿Desea ajustar el Stock en el inventario del producto?\n{} stock {}{}.".format(self.entry5.get(), '+' if int(self.entry6.get().replace('$', '')) > int(self.busqueda_cantidad) else '-', abs(int(self.entry6.get()) - int(self.busqueda_cantidad))))
                            if respuesta:
                                if int(self.entry6.get()) > int(self.busqueda_cantidad):
                                    diferencia = int(self.entry6.get()) - int(self.busqueda_cantidad)
                                    query = "UPDATE producto SET Cantidad = Cantidad + ? WHERE Nombre = ?"
                                else:
                                    diferencia = int(self.busqueda_cantidad) - int(self.entry6.get())
                                    query = "UPDATE producto SET Cantidad = Cantidad - ? WHERE Nombre = ?"
                                
                                self.cursor.execute(query, (diferencia, self.entry5.get()))

                    self.mydb.commit()
                    self.limpiar_campos()
                    return
            
        elif self.busqueda_id and not self.busqueda_producto:

            query = "SELECT Código_Barra FROM producto WHERE Nombre = ?"
            self.cursor.execute(query, (self.entry5.get(),))
            row_new = self.cursor.fetchone()

            if row_new:

                if self.entry1.get() == '' or self.entry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '' or self.entry6.get() == '' or self.entry7.get() == '':
                    messagebox.showerror("Error", "Por favor, complete todos los campos si desea editar el producto de la compra.", parent=self.window)
                    return
                
                costo_nuevo = self.entry7.get().replace("$", "")
                self.cursor.execute("SELECT Rut FROM proveedor WHERE Razon_Social = ?", (self.entry2.get(),))
                rut_prov = self.cursor.fetchone()

                for item in self.compras.get_children():
                    producto_existe = False
                    valores = self.compras.item(item, "values")  # Obtener los valores de la fila
                    if valores[1] == self.busqueda_id:  # Comparar con la columna "Num_Boleta" (índice 1)

                        for hijo in self.compras.get_children(item):

                            valores_hijo = self.compras.item(hijo, "values")
                            if valores_hijo[4] == self.entry5.get():
                                resultado = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar el producto: {}, de esta compra?".format(valores_hijo[4]))
                                if resultado:
                                    self.compras.item(item, values=(self.entry3.get(), self.entry1.get(), self.entry4.get(), self.entry2.get(), '', '', ''))
                                    self.compras.item(hijo, values=('','','','                                 >>>',self.entry5.get(), self.entry6.get(), f'${costo_nuevo}'))
                                    query = "UPDATE compra SET Id = ?, proveedor_Rut = ?, Fecha = ?, Producto_Código_Barra = ?, Cantidad = ?, Precio = ?, Formato = ? WHERE Id LIKE ? AND Producto_Código_Barra LIKE ?"
                                    self.cursor.execute(query, (self.entry1.get(), rut_prov[0], self.entry3.get(), row_new[0], self.entry6.get(), costo_nuevo, self.entry4.get(), self.busqueda_id, row_new[0]))
                                    producto_existe = True

                        if producto_existe is not True:
                            hijo = self.compras.get_children(item)
                            if hijo:
                                valores_hijo = self.compras.item(hijo[0], "values")
                                producto = valores_hijo[4]

                            respuesta = messagebox.askyesno("Confirmar", "¿Desea reemplazar este producto: {} por {} en la compra?".format(producto, self.entry5.get()))
                            if respuesta:
                                query = "SELECT Código_Barra FROM producto WHERE Nombre = ?"
                                self.cursor.execute(query, (producto,))
                                row_old = self.cursor.fetchone()
                                self.compras.item(item, values=(self.entry3.get(), self.entry1.get(), self.entry4.get(), self.entry2.get(), '', '', ''))
                                self.compras.item(hijo, values=('','','','                                 >>>',self.entry5.get(), self.entry6.get(), f'${costo_nuevo}'))
                                query = "UPDATE compra SET Id = ?, proveedor_Rut = ?, Fecha = ?, Producto_Código_Barra = ?, Cantidad = ?, Precio = ?, Formato = ? WHERE Id LIKE ? AND Producto_Código_Barra LIKE ?"
                                self.cursor.execute(query, (self.entry1.get(), rut_prov[0], self.entry3.get(), row_new[0], self.entry6.get(), costo_nuevo, self.entry4.get(), self.busqueda_id, row_old[0]))
                                
                self.mydb.commit()
                self.limpiar_campos()
                return


            elif self.entry1.get() == self.busqueda_id and self.entry2.get() == self.busqueda_prov and self.entry3.get() == self.busqueda_fecha and self.entry4.get() == self.busqueda_formato:
                messagebox.showinfo("Información", "No se han realizado cambios en la compra.", parent=self.window)
                return 

            else:
                print(f'{self.entry1.get()} : {self.busqueda_id}')
                print(f'{self.entry2.get()} : {self.busqueda_prov}')
                print(f'{self.entry3.get()} : {self.busqueda_fecha}')
                print(f'{self.entry4.get()} : {self.busqueda_formato}')
                print('camino-2')
                self.entry6.delete(0, END)
                self.entry7.delete(0, END)
                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea editar esta compra?")
                if respuesta:
                    for item in self.compras.get_children():

                        valores = self.compras.item(item, "values")  # Obtener los valores de la fila
                        if valores[1] == self.busqueda_id:  # Comparar con la columna "Num_Boleta" (índice 1)
                            self.compras.item(item, values=(self.entry3.get(), self.entry1.get(), self.entry4.get(), self.entry2.get(), '', '', ''))

                    query = "SELECT Rut FROM proveedor WHERE Razon_Social = ?"
                    self.cursor.execute(query, (self.entry2.get(),))
                    rut_prov = self.cursor.fetchone()

                    query = "UPDATE compra SET Id = ?, proveedor_Rut = ?, Fecha = ?, Formato = ? WHERE Id LIKE ?"
                    self.cursor.execute(query, (self.entry1.get(), rut_prov[0], self.entry3.get(), self.entry4.get(), self.busqueda_id))
                    self.mydb.commit()
                    print(self.cursor.rowcount)

                    self.limpiar_campos()
                    return



    def eliminar_compra(self):

        for item in self.compras.get_children():

            valores = self.compras.item(item, "values")  # Obtener los valores de la fila
            if valores[1] == self.entry1.get():  # Comparar con la columna "Id" (índice 1)
                id_compra = self.entry1.get()
                if self.entry5.get():
                    nombre_producto = self.entry5.get()
                    for hijo in self.compras.get_children(item):
                        valores_hijo = self.compras.item(hijo, "values")

                        if valores_hijo[4] == nombre_producto:
                            respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea ELIMINAR el Producto de esta Compra? \n\n> {}".format(nombre_producto))
                            if respuesta:
                                self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (nombre_producto,))
                                codigo_barra = self.cursor.fetchone()[0]
                                query = "DELETE FROM compra WHERE Id = ? AND Producto_Código_Barra = ?"
                                self.cursor.execute(query, (id_compra, codigo_barra))
                                #self.mydb.commit()
                                #self.actualizar_tabla()
                                self.limpiar_campos()
                                self.compras.delete(hijo)
                                messagebox.showinfo("Éxito", "El Producto '{}', de la Compra Id:'{}'. \nHa sido Eliminado correctamente.".format(nombre_producto, id_compra), parent=self.window)
                            return
                    messagebox.showerror("Error", "El producto especificado no se encuentra en la Compra seleccionada.", parent=self.window)
                    return
                else:
                    respuesta = messagebox.askyesno("Confirmar", "¿Está seguro que desea ELIMINAR toda la Compra?")
                    if respuesta:
                        query = "DELETE FROM compra WHERE Id = ?"
                        self.cursor.execute(query, (id_compra,))
                        #self.mydb.commit()
                        self.actualizar_tabla()
                        self.compras.delete(item)
                        self.limpiar_campos()
                        messagebox.showinfo("Éxito", "Compra con Id: '{}' Eliminada correctamente.".format(id_compra), parent=self.window)


    def filtrar_compras(self):

        self.busqueda_id = None
        self.busqueda_producto = None

        # Si entry0 está vacío y hay una selección en la tabla
        if not self.entry0.get():
            selected = self.compras.selection()
            if selected:
                self.proveedores = self.listado
                self.productos = self.products_list
                self.entry1.config(state='normal')
                self.entry2.set_completion_list(self.proveedores)
                self.entry3.config(state='normal')
                self.entry4.config(state='normal')
                self.entry5.set_completion_list(self.productos)
                self.entry6.config(state='normal')
                self.entry7.config(state='normal')
                item = selected[0]
                parent = self.compras.parent(item)
                if parent:  # Es una fila hija
                    valores_padre = self.compras.item(parent, "values")
                    valores_hijo = self.compras.item(item, "values")
                    # Llena los entrys con datos del padre y del hijo
                    self.entry1.delete(0, END)
                    self.entry1.insert(0, valores_padre[1])     # Id compra
                    self.busqueda_id = valores_padre[1]
                    self.entry2.delete(0, END)
                    self.entry2.insert(0, valores_padre[3])     # Rut Prov
                    self.busqueda_prov = valores_padre[3]
                    self.entry3.delete(0, END)
                    self.entry3.insert(0, valores_padre[0])     # Fecha
                    self.entry3.config(state='readonly')
                    self.busqueda_fecha = valores_padre[0]
                    self.entry4.delete(0, END)
                    self.entry4.insert(0, valores_padre[2])     # Formato
                    self.busqueda_formato = valores_padre[2]
                    self.entry5.delete(0, END)
                    self.entry5.insert(0, valores_hijo[4])      # Producto
                    self.busqueda_producto = valores_hijo[4]
                    self.entry6.delete(0, END)
                    self.entry6.insert(0, valores_hijo[5])      # Cantidad
                    self.busqueda_cantidad = valores_hijo[5]
                    self.entry7.delete(0, END)
                    self.entry7.insert(0, valores_hijo[6].replace('$', ''))      # Precio
                    self.busqueda_precio = valores_hijo[6].replace('$', '')

                else:  # Es una fila padre
                    valores = self.compras.item(item, "values")
                    self.entry1.delete(0, END)
                    self.entry1.insert(0, valores[1])  # Id compra
                    self.busqueda_id = valores[1]
                    self.entry2.delete(0, END)
                    self.entry2.insert(0, valores[3])  # Rut Prov
                    self.busqueda_prov = valores[3]
                    self.entry3.delete(0, END)
                    self.entry3.insert(0, valores[0])  # Fecha
                    self.entry3.config(state='readonly')
                    self.busqueda_fecha = valores[0]
                    self.entry4.delete(0, END)
                    self.entry4.insert(0, valores[2])  # Formato
                    self.busqueda_formato = valores[2]
                    self.entry5.delete(0, END)
                    self.entry5.insert(0, '')          # Cod Prod vacío
                    self.entry6.delete(0, END)
                    self.entry6.insert(0, '')          # Cantidad vacío
                    self.entry7.delete(0, END)
                    self.entry7.insert(0, '')          # Precio vacío

            return

        # Si entry0 tiene valor, busca por ID o Rut como antes
        for item in self.compras.get_children():

            valores = self.compras.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry0.get() or valores[1] == self.entry0.get():  # Comparar con la columna "Rut" (índice 0)

                self.proveedores = self.listado
                self.productos = self.products_list
                self.entry1.config(state='normal')
                self.entry2.set_completion_list(self.proveedores)
                self.entry3.config(state='normal')
                self.entry4.config(state='normal')
                self.entry5.set_completion_list(self.productos)
                self.entry6.config(state='normal')
                self.entry7.config(state='normal')

                self.entry1.delete(0, END)
                self.entry1.insert(0, valores[1])  # Id compra
                self.busqueda_id = valores[1]
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[3])  # Rut Prov
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[0])  # Fecha
                self.entry3.config(state='readonly')
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[2])  # Formato
                self.entry5.delete(0, END)
                self.entry5.insert(0, '')  # Cod Prod
                self.entry6.delete(0, END)
                self.entry6.insert(0, '')  # Cantidad
                self.entry7.delete(0, END)
                self.entry7.insert(0, '')  # Precio
                

    def actualizar_tabla(self):

        query = "SELECT c.Fecha, c.Id, c.Formato, p.Razon_Social AS proveedor, pr.Nombre AS producto, c.Cantidad, c.Precio FROM compra c JOIN proveedor p ON c.Proveedor_Rut = p.Rut JOIN producto pr ON c.Producto_Código_Barra = pr.Código_Barra ORDER BY c.Fecha DESC, c.Id DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        boleta_previa = None
        self.compras.delete(*self.compras.get_children())
        fecha_compra = None

        for idx, i in enumerate(rows):
            num_boleta = i[1]

            if boleta_previa != num_boleta:
                fecha_compra = self.compras.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3], '', '', ''))            # Inserta el producto como hijo
            # Agregar el producto a la lista de objetos de la boleta actual
            self.compras.insert(parent=fecha_compra, index='end', values=('','','','                                 >>>',i[4], i[5], '${}'.format(i[6])), tags=('detalles_venta',))
            self.compras.item(fecha_compra, open=True)

            boleta_previa = num_boleta


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