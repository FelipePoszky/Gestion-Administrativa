from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import BOLD
from tkcalendar import *

from forms.form_inventario import inventario
from forms.form_ventas import ventas
from forms.form_reportes import reportes
from forms.form_nuevoProducto import nuevo

import util.generic as utl
import util.variables as variables
import os
import sqlite3
from ttkwidgets.autocomplete import AutocompleteCombobox
from datetime import date
from time import strftime

class compras:

    def btn_clicked(self):
    
        print("Button Info")


    def GoMenuPrincipal(self):
        
        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()
    
    def GoMenuInventario(self):
        self.window.destroy()
        inventario()

    def GoMenuVentas(self):
        self.window.destroy()
        ventas()

    def GoMenuReportes(self):
        self.window.destroy()
        reportes()

    def nuevoProducto(self):
        nuevo(self)


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

        self.canvas = Canvas(
            self.window,
            bg = "#8c8c8c",
            height = 625,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/background.png")
        background = self.canvas.create_image(
            630, 312.5,
            image=background_img)

        
    # -------------     Botones Barra Navegador     -----------------------

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img7.png")
        b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuPrincipal,
            cursor = "hand2",
            relief = "flat")

        b7.place(
            x = 118, y = 10,
            width = 116,
            height = 46)

        img8 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img8.png")
        b8 = Button(
            image = img8,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuVentas,
            cursor = "hand2",
            relief = "flat")

        b8.place(
            x = 253, y = 10,
            width = 116,
            height = 46)

        img9 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img9.png")
        b9 = Button(
            image = img9,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuInventario,
            cursor = "hand2",
            relief = "flat")

        b9.place(
            x = 388, y = 10,
            width = 150,
            height = 46)

        img10 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img10.png")
        b10 = Button(
            image = img10,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuReportes,
            cursor = "hand2",
            relief = "flat")

        b10.place(
            x = 720, y = 10,
            width = 145,
            height = 46)

    #----------------   Entradas Datos Generales Compra   ----------------

        self.ident_comp = StringVar()
        self.identificadores = []
        self.format = StringVar()
        self.fecha = StringVar()

        query = "SELECT Id FROM compra ORDER BY Id DESC"
        self.cursor.execute(query)
        resultado = self.cursor.fetchone()
        for id in resultado:
            if id is None:
                self.ident_comp.set("1")
            else:
                self.identificadores.append(int(id))
                self.ident_comp.set(str(int(id) + 1))

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img_textBox4.png")
        self.entry0_bg = self.canvas.create_image(
            950, 160,
            image = entry0_img)

        self.entry0 = Entry(
            bd = 0,
            disabledbackground = "#656565",
            disabledforeground = "#d9d9d9",
            textvariable=self.ident_comp,
            bg = "#d9d9d9",         # color cuando el 'estado' es 'normal', cuando este 'disabled' = '656565'
            highlightthickness = 0)

        self.entry0.place(
            x = 835, y = 148,
            width = 222.0,
            height = 25)

        query = "SELECT Razon_Social FROM proveedor"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        proveedores = [fila[0] for fila in resultados]

        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img_textBox4.png")
        self.entry1_bg = self.canvas.create_image(
            950, 198,
            image = entry1_img)

        self.ident_prov = AutocompleteCombobox(
            completevalues=proveedores,
        )

        self.ident_prov.place(
            x = 835, y = 186,
            width = 222.0,
            height = 25)

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img_textBox4.png")
        self.entry2_bg = self.canvas.create_image(
            950, 237,
            image = entry2_img)

        self.entry2 = EntryWithPlaceholder(
            bd = 0,
            disabledbackground = "#656565",
            disabledforeground = "#d9d9d9",
            placeholder="Voucher / Factura / Boleta",
            textvariable=self.format,
            bg = "#d9d9d9",           # color cuando el estado es 'normal', cuando este 'disabled' = '656565'
            highlightthickness = 0)

        self.entry2.place(
            x = 835, y = 225,
            width = 222.0,
            height = 25)

        self.fecha.set(str(date.today()))

        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img_textBox4.png")
        self.entry3_bg = self.canvas.create_image(
            950, 276,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            disabledbackground = "#656565",
            disabledforeground = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable=self.fecha,
            bg = "#d9d9d9",         # color cuando el estado es 'normal', cuando este 'disabled' = '656565'
            highlightthickness = 0,
            state = "readonly"
            )
        
        self.entry3.place(
            x = 835, y = 264,
            width = 222.0,
            height = 25)

    #   -------------------     Boton General     ------------------------

        imgCal = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/ButtonCalendar.png")
        self.calend = Button(
            image = imgCal,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_calendario,
            cursor = "hand2",
            relief = "flat"
        )
        self.calend.place(
            x = 1076, y = 262,
            width = 31,
            height = 30)

        imgInfo = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/ButtonInfo.png")
        self.info = Button(
            image = imgInfo,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            cursor = "hand2",
            relief = "flat"
        )
        self.info.place(
            x = 1198, y = 88,
            width = 35,
            height = 35)

    #--------------------------------->  [ Parche ]  <------------------------------------>

        parche = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/Parche.png")
        self.label_parche = Label(
            image = parche,
            bg = "#656565",
            bd = 0,
            highlightthickness = 0)

        self.label_parche.place(
            x = 663, y = 300,
            width = 574,
            height = 229)

        sticker = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/Sticker.png")
        self.label_sticker = Label(
            image = sticker,
            bg = "#8c8c8c",
            bd = 0,
            highlightthickness = 0)

        self.label_sticker.place(
            x = 192, y = 214)

        # -------[ Boton Ingresar Datos ]-------

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/Ingresar_datos.png")
        self.b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.añadirWidgets,
            cursor = "hand2",
            relief = "flat")

        self.b2.place(
            x = 827, y = 310,
            width = 247,
            height = 43)

        # --------------------------> [ Entrys de poductos ] <-------------------------->

        self.cant_prod = StringVar()
        self.precio_prod = StringVar()

        query = "SELECT Nombre FROM producto"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        variables.products_list = [fila[0] for fila in resultados]

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img_textBox4.png")
        entry4_bg = self.canvas.create_image(
            950, 387,
            image = entry4_img)

        self.ident_prod = AutocompleteCombobox(
            completevalues = variables.products_list
            )

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img_textBox5.png")
        entry5_bg = self.canvas.create_image(
            950, 426,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            textvariable = self.cant_prod,
            highlightthickness = 0)
        

        entry6_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img_textBox6.png")
        entry6_bg = self.canvas.create_image(
            950, 465,
            image = entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            textvariable = self.precio_prod,
            highlightthickness = 0)

        # --------------------------------> [ Botones Ingresar Productos ] <---------------------------->
 
        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img0.png")
        self.b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.editar_producto,
            cursor = "hand2",
            relief = "flat")


        img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img1.png")
        self.b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiar_entrys,
            cursor = "hand2",
            relief = "flat")

        
        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img3.png")
        self.b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.añadir_producto,
            cursor = "hand2",
            relief = "flat")
            

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img4.png")
        self.b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.nuevoProducto,
            cursor = "hand2",
            relief = "flat")

        marco = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/Marco.png")
        self.label_marco = Label(
            image = marco,
            bg = '#8c8c8c',
            bd = 0,
            highlightthickness = 0)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/Reanudar.png")
        self.b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.remover_productos,
            cursor = "hand2",
            relief = "flat")

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/Finalizar.png")
        self.b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.confirmar_compra,
            cursor = "hand2",
            relief = "flat")
    
        img11 = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/img5.png")
        self.b7 = Button(
            image = img11,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            cursor = "hand2",
            relief = "flat")

        self.window.resizable(False, False)
        self.window.mainloop()


    def abrir_calendario(self):
        
        self.calendario = Toplevel(self.window)
        self.calendario.title("Calendario")
        self.calendario.geometry("300x300")

        self.date = Calendar(self.calendario, select_mode='day', date_pattern='y-mm-dd')
        self.date.pack(side="top", fill="both", expand=True)
        self.aceptar = Button(self.calendario, text="Aceptar", command=self.aceptar_fecha)
        self.aceptar.pack(side="bottom")

    
    def aceptar_fecha(self):
        print(self.date.get_date())
        # year / month / day
        self.calendario.destroy()
        date = StringVar(value=self.date.get_date())
        self.entry3.config(textvariable=date)
        #self.entry1.insert(0, self.date.get_date())
        self.entry3.config(state="readonly", readonlybackground="#d9d9d9")


    def limpiar_entrys(self):
        self.ident_prod.delete(0, END)
        self.precio_prod.set("")
        self.cant_prod.set("")

    
    def añadirWidgets(self):

        if self.ident_comp.get() == "" or self.ident_prov.get() == "" or self.format.get() == "" or self.format.get() == "Voucher / Factura / Boleta" or self.fecha.get() == "":
            messagebox.showerror("Oops!", "Por favor completa todos los campos.", parent=self.window)
            return

        for id in self.identificadores:
            if self.ident_comp.get() == str(id):
                messagebox.showerror("Error", "El identificador de compra ya existe. Por favor, ingresa uno diferente.", parent=self.window)
                return
        
        self.mydb = sqlite3.connect("BD_Veguita")
        self.cursor = self.mydb.cursor()

        proveedor = self.ident_prov.get()
        self.ident_prov.place_forget()
        self.ident_prov = Entry(
            self.window,
            textvariable=StringVar(value=proveedor),
            bd=0,
            disabledforeground="#d9d9d9",
            disabledbackground="#656565",
            highlightthickness=0,
            state="disabled"  # Deshabilitar el Entry
        )
        # Cambiar la imagen del entry, para asimilar que está deshabilitado
        img_dir = os.getcwd()
        self.entry0_img = PhotoImage(file=f"{img_dir}/Imagenes/M. Compras/img_textBox0.png")
        self.entry1_img = PhotoImage(file=f"{img_dir}/Imagenes/M. Compras/img_textBox1.png")
        self.entry2_img = PhotoImage(file=f"{img_dir}/Imagenes/M. Compras/img_textBox2.png")
        self.entry3_img = PhotoImage(file=f"{img_dir}/Imagenes/M. Compras/img_textBox3.png")

        # Eliminar la imagen anterior
        self.canvas.delete(self.entry0_bg)
        self.canvas.delete(self.entry1_bg)
        self.canvas.delete(self.entry2_bg)
        self.canvas.delete(self.entry3_bg)

        # Crear una nueva imagen en el canvas
        self.entry0_bg = self.canvas.create_image(
            950, 160,
            image=self.entry0_img
        )
        self.entry1_bg = self.canvas.create_image(
            950, 198,
            image=self.entry1_img
        )
        self.entry2_bg = self.canvas.create_image(
            950, 237,
            image=self.entry2_img
        )
        self.entry3_bg = self.canvas.create_image(
            950, 276,
            image=self.entry3_img
        )

        # Configurar el Entry
        self.entry0.configure(state = 'disabled')
        self.entry2.configure(state = 'disabled')
        self.entry3.configure(state = 'disabled')

        self.calend.place_forget()
        self.label_parche.place_forget()
        self.b2.place_forget()

        # --------------------------> [ Ubicar Nuevos Widgets. Entrys/Botones ] <--------------------------
        self.ident_prov.place(
            x = 835, y = 186,
            width = 222.0, height = 25)

        self.ident_prod.place(
            x = 835, y = 375,
            width = 222.0,
            height = 25)

        self.entry5.place(
            x = 835, y = 414,
            width = 222.0,
            height = 25)

        self.entry6.place(
            x = 835, y = 453,
            width = 222.0,
            height = 25)

        self.b0.place(
            x = 1081, y = 526,
            width = 150,
            height = 49)

        self.b1.place(
            x = 665, y = 526,
            width = 153,
            height = 49)

        self.b3.place(
            x = 826, y = 526,
            width = 248,
            height = 49)

        self.b4.place(
            x = 1121, y = 370,
            width = 103,
            height = 40)
        
        self.label_marco.place(
            x = 10, y = 543.5,
            width = 597,
            height = 60)
        
        self.b5.place(
            x = 95, y = 550,
            width = 125,
            height = 41)

        self.b6.place(
            x = 393, y = 550,
            width = 125,
            height = 41)

        self.b7.place(
            x = 1080, y = 372,
            width = 34,
            height = 35)
        
        # --------------------------> [ Tabla Productos ] <----------------------------------
        self.tabla = ttk.Treeview(self.window, columns=(1, 2, 3, 4), show="headings")

        self.tabla.heading(1, text="Proveedor")            
        self.tabla.heading(2, text="Producto")
        self.tabla.heading(3, text="Cantidad")
        self.tabla.heading(4, text="Precio")
        self.tabla.column(1, width=100, anchor=W)
        self.tabla.column(2, width=80, anchor=W)
        self.tabla.column(3, width=15, anchor=CENTER)
        self.tabla.column(4, width=20, anchor=CENTER)

        # Configuración Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#464646", fieldbackground="#464646", foreground="white", rowheight=32, font=("Inter", 9))
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 11, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])
        
        self.tabla.place(x=17, y=82, width=584, height=391)
        # Agregar columna Proveedor como padre
        self.columna_prov = self.tabla.insert(parent='', index='end', values=(self.ident_prov.get(), '', '', ''))
        self.tabla.item(self.columna_prov, open=True)

        self.dash_total = PhotoImage(file = f"{img_dir}/Imagenes/M. Compras/total.png")
        total_compra = Label(
            image = self.dash_total,
            bg = '#8c8c8c',
            bd = 0,
            highlightthickness = 0)

        total_compra.place(
            x = 17, y = 482,
            width = 584,
            height = 45)

        self.contador = 0
        self.total_variable = StringVar()
        self.total_variable.set(self.contador)
        self.valor_total = Label(textvariable=self.total_variable, bg="#1D1D1D", fg="white", font=("Inter", 13, BOLD))
        self.valor_total.place(x=511, y=492.5)


# -------------   Funcion para Leer la Columna Precio para calcular Total   --------------------
    def actualizar_total(self):

        for item in self.tabla.get_children(self.columna_prov):
            valores = self.tabla.item(item, "values")
            if valores[3] != '':
                precio = int(valores[3].replace('$ ', ''))
                self.contador += precio
        self.total_variable.set(self.contador)
        self.contador = 0

# ------------------   Funcion Agregar Producto en Tabla Compra   -------------------- #
    def añadir_producto(self):
        
        if self.ident_prod.get() == "" or self.cant_prod.get() == "" or self.precio_prod.get() == "":
            messagebox.showerror("Error", "Por favor completa todos los campos de producto.", parent=self.window)
            return

        for item in self.tabla.get_children(self.columna_prov):
            valores = self.tabla.item(item, "values")  # Obtener los valores de la fila
            if valores[1] == self.ident_prod.get():  # Comparar con la columna "Producto" (índice 1)
                if valores[2] == self.cant_prod.get() and valores[3] == f'$ {self.precio_prod.get()}':
                    messagebox.showerror("Error", f"El producto '{self.ident_prod.get()}' ya ha sido agregado a la tabla con la misma cantidad y precio.", parent=self.window)
                    return
                else:
                    messagebox.showerror("Error", f"El producto '{self.ident_prod.get()}' ya existe en la tabla. Usa 'Editar Producto' para modificarlo.", parent=self.window)
                    return

        self.tabla.insert(self.columna_prov, index="end", values=('', self.ident_prod.get(), self.cant_prod.get(), f'$ {self.precio_prod.get()}'))
        self.actualizar_total()
        self.precio_prod.set("")
        self.cant_prod.set("")

# -----------------   Funcion Editar Producto en Tabla Compra   --------------------#
    def editar_producto(self):

        # Obtener el valor del producto ingresado por el usuario
        producto = self.ident_prod.get()
        # Verificar si el producto está vacío
        if not producto:
            messagebox.showerror("Error", "Por favor, ingresa un producto para buscar.", parent=self.window)
            return
        # Buscar en la tabla la fila que coincida con el producto
        for item in self.tabla.get_children(self.columna_prov):
            valores = self.tabla.item(item, "values")  # Obtener los valores de la fila
            if valores[1] == producto:  # Comparar con la columna "Producto" (índice 1)
                # Actualizar los valores de la fila
                self.tabla.item(item, values=(valores[0], producto, self.cant_prod.get(), f"$ {self.precio_prod.get()}"))
                messagebox.showinfo("Éxito", f"Producto '{producto}' actualizado correctamente.", parent=self.window)
                self.actualizar_total()
                return
        # Si no se encuentra el producto, mostrar un mensaje de error
        messagebox.showerror("Error", f"Producto '{producto}' no encontrado en la tabla.", parent=self.window)

# -------------   Funcion Eliminar Producto de Tabla   --------------------
    def remover_productos(self):

        self.ident_prod.delete(0, END)
        self.precio_prod.set("")
        self.cant_prod.set("")

        # Elimina solo los productos agregados. Mantiene fila Proveedor
        for child in self.tabla.get_children(self.columna_prov):
            self.tabla.delete(child)
        
        self.contador = 0
        self.total_variable.set(self.contador)

# -------------  Funcion Almacenar y Finalizar Compra   --------------------
    def confirmar_compra(self):

        # Verificar si hay productos en la tabla
        if not self.tabla.get_children(self.columna_prov):
            messagebox.showerror("Error", "No hay productos en la tabla para confirmar la compra.", parent=self.window)
            return

        # Confirmar la compra
        respuesta = messagebox.askyesno("Confirmar Compra", "¿Estás seguro de que deseas confirmar la compra?", parent=self.window)
        if respuesta:
            self.cursor.execute("SELECT RUT FROM proveedor WHERE Razon_Social = ?", (self.ident_prov.get(),))
            proveedor_rut = self.cursor.fetchone()[0]

            for item in self.tabla.get_children(self.columna_prov):
                valores = self.tabla.item(item, "values")

                self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (valores[1],))
                producto_codigo = self.cursor.fetchone()[0]
                
                query = "INSERT INTO compra (Id, Producto_Código_Barra, Proveedor_Rut, Fecha, Precio, Cantidad, Formato) VALUES(?, ?, ?, ?, ?, ?, ?)"
                self.cursor.execute(query, (self.ident_comp.get(), producto_codigo, proveedor_rut, self.entry3.get(), valores[3].replace("$ ",""), valores[2], self.format.get()))
            
                self.cursor.execute("UPDATE producto SET Cantidad = Cantidad + ? WHERE Código_Barra = ?", (valores[2], producto_codigo))

            self.mydb.commit()
            messagebox.showinfo("Compra Confirmada", "La compra ha sido confirmada.", parent=self.window)



# -------------   Clase Entry con Placeholder   --------------------
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.on_focus_out(None)  # Display placeholder initially

    def on_focus_in(self, event):
        if self.get() == self.placeholder and self['fg'] == self.placeholder_color:
            self.delete(0, END)
            self['fg'] = self.default_fg_color

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color