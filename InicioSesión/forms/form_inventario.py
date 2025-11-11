from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from tkinter import filedialog
import util.generic as utl

from forms.form_gestionProductos import gestionProductos
from forms.form_gestionVentas import gestionVentas
from forms.form_gestionCompras import gestionCompras

import sqlite3
import datetime
from datetime import date
from time import strftime
import os


class inventario:    

# ------------------------------------>>> [    Funciones Moverse a otras Ventanas    ] <<<---------------------------------------- #
    def GoInicio(self):
        
        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()
    
    def irVentas(self):

        from forms.form_ventas import ventas
        self.window.destroy()
        ventas()
    
    def irCompras(self):

        from forms.form_compras import compras
        self.window.destroy()
        compras()

    def irReportes(self):

        from forms.form_reportes import reportes
        self.window.destroy()
        reportes()
    
    def abrir_gestion_productos(self):

        self.window.destroy()
        gestionProductos()

    def abrir_gestion_ventas(self):

        self.window.destroy()
        gestionVentas()

    def abrir_gestion_compras(self):

        self.window.destroy()
        gestionCompras()

    def abrir_nuevo_producto(self):

        from forms.form_nuevoProducto import nuevo
        nuevo(self)

    def btn_clicked(self):
        
        print("Boton sin funcion asignada / usuario debe escoger una Tabla")


# ------------------------------------>>> [    Iniciar la Ventana    ] <<<---------------------------------------- #
    def __init__(self):


        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()    
        
        img_dir = os.getcwd()

        self.window = Tk()

        self.elemento = StringVar()

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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/background.png")
        self.background = self.canvas.create_image(
            630, 312.5,
            image=background_img)
        
        self.background_cal = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/cal-background.png")
        self.img0_cal = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/cal-img0.png")
        self.entry0_cal = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/cal-img_textBox.png")


        # >>>>>>>>>>>>>>>>>>>>>>>> BOTONES BARRA NAVEGACION <<<<<<<<<<<<<<<<<<<<<<<<<<<

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoInicio,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 118, y = 11,
            width = 115,
            height = 46)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.irVentas,
            cursor = "hand2",
            relief = "flat")

        b5.place(
            x = 253, y = 11,
            width = 117,
            height = 46)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img6.png")
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.irCompras,
            cursor = "hand2",
            relief = "flat")

        b6.place(
            x = 556, y = 11,
            width = 145,
            height = 46)

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img7.png")
        b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.irReportes,
            cursor = "hand2",
            relief = "flat")

        b7.place(
            x = 720, y = 11,
            width = 145,
            height = 46)


        # >>>>>>>>>>>>>>>>>>>>>> BOTONES TABLAS <<<<<<<<<<<<<<<<<<<<<<<<<<<


        self.tarjeta_ventas = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
        self.label_tarjetaVentas = Label(self.window, image=self.tarjeta_ventas, borderwidth=0, bg="#8c8c8c")
        self.label_tarjetaVentas.place(
            x = 8, y = 282,
            width = 436,
            height = 80)

        img8 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img8.png")
        self.b8 = Button(
            image = img8,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.emerge_tablaVentas,
            cursor = "hand2",
            relief = "flat")

        self.b8.place(
            x = 48, y = 299,
            width = 147,
            height = 47)


        self.tarjeta_productos = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
        self.label_tarjetaProductos = Label(self.window, image=self.tarjeta_productos, borderwidth=0 ,bg="#8c8c8c")
        self.label_tarjetaProductos.place(
            x = 8, y = 119,
            width = 436,
            height = 80)


        img9 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img9.png")
        self.b9 = Button(
            image = img9,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.emerge_tablaProductos,
            cursor = "hand2",
            relief = "flat")

        self.b9.place(
            x = 48, y = 136,
            width = 147,
            height = 47)


        self.tarjeta_compras = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
        self.label_tarjetaCompras = Label(self.window, image=self.tarjeta_compras, borderwidth=0, bg="#8c8c8c")
        self.label_tarjetaCompras.place(
            x = 8, y = 201,
            width = 436,
            height = 80)

        img10 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img10.png")
        self.b10 = Button(
            image = img10,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.emerge_tablaCompras,
            cursor = "hand2",
            relief = "flat")

        self.b10.place(
            x = 48, y = 217,
            width = 147,
            height = 47)

        # ----------------------------------------------------------------------------------------

        sticker = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Sticker.png")
        self.label_sticker = Label(
            image = sticker,
            bg = "#8c8c8c",
            bd = 0,
            highlightthickness = 0)

        self.label_sticker.place(
            x = 713, y = 187)

        # ---------------------------------ENTRYS-------------------------------------------------


        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img_textBox0.png")
        entry0_bg = self.canvas.create_image(
            216, 520,
            image = entry0_img)

        entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0,
            textvariable = self.elemento
            )

        entry0.place(
            x = 128, y = 508,
            width = 178,
            height = 25)

        #------------------------------------ BOTONES FILTROS --------------------------------------------

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img0.png")
        self.b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            cursor = "hand2",
            relief = "flat")

        self.b0.place(
            x = 323, y = 497,
            width = 105,
            height = 47)

        img15 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img11.png")
        self.b15 = Button(
            image = img15,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_nuevo_producto,
            cursor = "hand2",
            relief = "flat")

        img11 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/ButtonUp.png")
        self.b11 = Button(
            image = img11,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.orden("up"),
            cursor = "hand2",
            relief = "flat")


        img12 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/ButtonDown.png")
        self.b12 = Button(
            image = img12,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.orden("down"),
            cursor = "hand2",
            relief = "flat")


        img13 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/ButtonCalendar.png")
        self.b13 = Button(
            image = img13,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrir_calendario,
            cursor = "hand2",
            relief = "flat")


        img14 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/ButtonInfo.png")
        self.b14 = Button(
            image = img14,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            cursor = "hand2",
            relief = "flat")
        
        self.b14.place(
            x = 394, y = 384,
            width = 35,
            height = 35)

        self.entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/TextBoxDate.png")

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",  
            highlightthickness = 0)
        
        self.entry2 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            state = "readonly",  
            highlightthickness = 0)

        self.orden_fecha = "none"
        self.current_table = "none"

        self.window.resizable(False, False)
        self.window.mainloop()


# ------------------------------------>>> [    Panel de Botones | Luego de escoger Tabla   ] <<<---------------------------------------- #
    def agregar_panel_botones(self):

        img_dir = os.getcwd()


        self.frame_botones = Frame(self.window, bg="#8c8c8c", width=771, height=70)
        self.frame_botones.place(x=463, y=542.5)

        self.panel = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Panel Botones.png")

        self.label_panelbotones = Label(self.frame_botones, image=self.panel, borderwidth=0, bg="#8c8c8c")
        self.label_panelbotones.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        

        self.img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img1.png")
        b1 = Button(
            self.frame_botones,
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiarTabla,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 14, y = 8,
            width = 124,
            height = 45)

        self.img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img2.png")
        self.b2 = Button(
            self.frame_botones,
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            cursor = "hand2",
            relief = "flat")

        self.b2.place(
            x = 266, y = 8,
            width = 125,
            height = 45)

        self.img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/img3.png")
        self.b3 = Button(
            self.frame_botones,
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            cursor = "hand2",
            relief = "flat")

        self.b3.place(
            x = 558, y = 8,
            width = 124,
            height = 45)
        
    def orden(self, ordenar):

        self.orden_fecha = ordenar

        if ordenar == "up":
            self.b12.config(relief="flat")
            self.b11.config(relief="sunken")
        elif ordenar == "down":
            self.b11.config(relief="flat")
            self.b12.config(relief="sunken")
        else:
            self.b11.config(relief="flat")
            self.b12.config(relief="flat")
    
    
    def botones_fecha(self, tabla):

        if tabla == "compras" or tabla == "ventas":

            if self.current_table != "compras" and self.current_table != "ventas":
                self.b11.place(
                    x = 325, y = 457,
                    width = 46,
                    height = 34)

                self.b12.place(
                    x = 381, y = 457,
                    width = 46,
                    height = 34)

                self.b13.place(
                    x = 285, y = 458,
                    width = 31,
                    height = 30)
                # x = entry + 71
                self.entry1_bg = self.canvas.create_image(
                    201, 472,
                    image = self.entry1_img)
                # + 3
                self.entry1.place(
                    x = 127, y = 459,
                    width = 64,
                    height = 27)
                # x max. 273
                self.entry2.place(
                    x = 213, y = 459,
                    width = 64,
                    height = 27)
            else:
                self.entry1.config(state="normal")
                self.entry1.delete(0, END)
                self.entry1.config(state="readonly")
                self.entry2.config(state="normal")
                self.entry2.delete(0, END)
                self.entry2.config(state="readonly")

        else:
            if self.current_table == "compras" or self.current_table == "ventas":
                # Esconder botones y entrys de fecha
                self.orden("reanudar")
                self.b11.place_forget()
                self.b12.place_forget()
                self.b13.place_forget()
                self.canvas.delete(self.entry1_bg)
                self.entry1.config(state="normal")
                self.entry1.delete(0, END)
                self.entry1.config(state="readonly")
                self.entry1.place_forget()
                self.entry2.config(state="normal")
                self.entry2.delete(0, END)
                self.entry2.config(state="readonly")
                self.entry2.place_forget()


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [   Tabla de Compras   ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def emerge_tablaCompras(self):

        img_dir = os.getcwd()

        self.b8.config(relief = "flat")
        self.b9.config(relief = "flat")
        self.b10.config(relief = "sunken")

        if self.current_table != "compras":

            if self.current_table == "productos":
                self.Productos.destroy()
                self.scrollProductos.destroy()
                self.frame_treeview.destroy()
                self.b15.place_forget()
                self.tarjeta_productos = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
                self.label_tarjetaProductos.config(image=self.tarjeta_productos)

            elif self.current_table == "ventas":
                self.ventas.destroy()
                self.scrollVentas.destroy()
                self.frame_treeview.destroy()
                self.tarjeta_ventas = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
                self.label_tarjetaVentas.config(image=self.tarjeta_ventas)

            else:
                self.agregar_panel_botones()

            #---------------------------------------------------------------------------

            self.b0.config(command=self.searchCompras)  
            self.b3.config(command=lambda: self.descargarReporte("compras"))

            self.tarjeta_compras = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Compras.png")
            self.label_tarjetaCompras.config(image=self.tarjeta_compras)

            #---------------------------------------------------------------------------

            self.botones_fecha("compras")

            self.b2.config(command=self.abrir_gestion_compras)

            # Create a frame to hold the Treeview and scrollbar
            self.frame_treeview = Frame(self.window)
            self.frame_treeview.place(x=463, y=92, height=427, width=771)

            # Scrollbar
            self.scrollCompras = Scrollbar(self.frame_treeview)
            self.scrollCompras.pack(side=RIGHT, fill=Y)

            self.compras = ttk.Treeview(self.frame_treeview, columns=(1,2,3,4,5,6,7), show="headings", height=6, yscrollcommand=self.scrollCompras.set)
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

            queryC = "SELECT c.Fecha, c.Id, c.Formato, p.Razon_Social AS proveedor, pr.Nombre AS producto, c.Cantidad, c.Precio FROM compra c JOIN proveedor p ON c.Proveedor_Rut = p.Rut JOIN producto pr ON c.Producto_Código_Barra = pr.Código_Barra ORDER BY c.Fecha DESC, c.Id DESC"
            self.cursor.execute(queryC)
            rows = self.cursor.fetchall()
            self.updateCompras(rows)

            # Configure Treeview style
            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview", background="#343434", rowheight=30, fieldbackground="#343434", foreground="white", font=("Helvetica", 9, BOLD))
            style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
            style.map("Treeview", background=[('selected', '#101010')])
            style.map("Treeview.Heading", background=[('active', '#101010')])

            self.compras.place(x=0 ,y=0, height=427, width=754)
            self.current_table = "compras"

        else:
            print("Tabla de Compras ya está visible")


    def on_open(self, event):
        item = event.widget.focus()
        event.widget.item(item, tags=('parent_compra_open', 'parent_venta_open'))

    def on_close(self, event):
        item = event.widget.focus()
        event.widget.item(item, tags=('parent_compra','parent_venta'))


    def updateCompras(self, rows):

        self.compras.tag_configure('detalles_venta', background="#1d1d1d")  # Cambia los colores a tu gusto
        self.compras.tag_configure('parent_compra_open', background='#101010', foreground='white')
        self.compras.tag_configure('parent_compra', background='#343434', foreground='white')

        self.compras.bind('<<TreeviewOpen>>', self.on_open)
        self.compras.bind('<<TreeviewClose>>', self.on_close)

        boleta_previa = None
        self.compras.delete(*self.compras.get_children())
        objetos_boleta = []
        fecha_compra = None

        for idx, i in enumerate(rows):
            num_boleta = i[1]

            if boleta_previa != num_boleta:

                if objetos_boleta:
                    total = sum(p[6] for p in objetos_boleta)
                    self.compras.insert(parent=fecha_compra, index='end', values=('- - - - - - - -','- - - -','- - - - - - - -','- - - - - - - - - - - - - - - - -','[TOTAL]', '', '${}'.format(total)), tags=('detalles_venta',))
                    objetos_boleta = []
                # Nuevo parent para la nueva boleta
                fecha_compra = self.compras.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3]))            # Inserta el producto como hijo
            # Agregar el producto a la lista de objetos de la boleta actual
            self.compras.insert(parent=fecha_compra, index='end', values=('- - - - - - - -','- - - -','- - - - - - - -','- - - - - - - - - - - - - - - - -',i[4], i[5], '${}'.format(i[6])), tags=('detalles_venta',))
            objetos_boleta.append(i)
            boleta_previa = num_boleta

            # Al terminar el bucle, inserta el total de la última boleta (solo una vez)
        if objetos_boleta:
            total = sum(p[6] for p in objetos_boleta)
            self.compras.insert(parent=fecha_compra, index='end', values=('- - - - - - - -','- - - -','- - - - - - - -','- - - - - - - - - - - - - - - - -','[TOTAL]', '', '${}'.format(total)), tags=('detalles_venta',))


    def searchCompras(self):
        
        q4 = (self.elemento.get() or "").strip()
        desde = (self.entry1.get() or "").strip()
        hasta = (self.entry2.get() or "").strip()
        
        orden = "DESC" if self.orden_fecha == 'down' else "ASC" if self.orden_fecha == 'up' else ""
        base = """
            SELECT c.Fecha, c.Id, c.Formato, p.Razon_Social AS proveedor, pr.Nombre AS producto, c.Cantidad, c.Precio
            FROM compra c
            JOIN proveedor p ON c.Proveedor_Rut = p.Rut
            JOIN producto pr ON c.Producto_Código_Barra = pr.Código_Barra
            WHERE 1=1
        """
        params = []

        if q4:
            base += " AND (c.Id LIKE ? OR pr.Nombre LIKE ? OR p.Razon_Social LIKE ?)"
            like = f"%{q4}%"
            params.extend([like, like, like])
        
        # añadir filtro por rango de fechas
        if desde and hasta:
            base += " AND c.Fecha BETWEEN ? AND ?"
            params.extend([desde, hasta])
        elif desde:
            base += " AND c.Fecha >= ?"
            params.append(desde)
        elif hasta:
            base += " AND c.Fecha <= ?"
            params.append(hasta)

        if orden:
            base += f" ORDER BY c.Fecha {orden}"

        
        self.cursor.execute(base, params)
        rows = self.cursor.fetchall()
        self.updateCompras(rows)


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Tabla de Productos ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def emerge_tablaProductos(self):

        img_dir = os.getcwd()

        self.b8.config(relief = "flat")
        self.b9.config(relief = "sunken")
        self.b10.config(relief = "flat")

        if self.current_table != "productos":

            if self.current_table == "compras":
                self.compras.destroy()
                self.scrollCompras.destroy()
                self.frame_treeview.destroy()
                self.tarjeta_compras = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
                self.label_tarjetaCompras.config(image=self.tarjeta_compras)

            elif self.current_table == "ventas":
                self.ventas.destroy()
                self.scrollVentas.destroy()
                self.frame_treeview.destroy()
                self.tarjeta_ventas = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
                self.label_tarjetaVentas.config(image=self.tarjeta_ventas)

            else:
                self.agregar_panel_botones()

            #----------------------------------------------------------------------
            
            self.tarjeta_productos = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Productos.png")
            self.label_tarjetaProductos.config(image=self.tarjeta_productos)


            #----------------------------------------------------------------------

            self.b0.config(command=self.searchProductos)
            self.b3.config(command=lambda: self.descargarReporte("productos"))

            self.b15.place(
                x = 120, y = 455,
                width = 157,
                height = 39)

            self.b2.config(command=self.abrir_gestion_productos)

            self.botones_fecha("productos")

            # Create a frame to hold the Treeview and scrollbar
            self.frame_treeview = Frame(self.window)
            self.frame_treeview.place(x=463, y=92, height=427, width=771)

            # Scrollbar

            self.scrollProductos = Scrollbar(self.frame_treeview)
            self.scrollProductos.pack(side=RIGHT, fill=Y)

            self.Productos = ttk.Treeview(self.frame_treeview, columns=(1,2,3,4,5,6,7), show='headings', height=6, yscrollcommand=self.scrollProductos.set)
            self.scrollProductos.config(command=self.Productos.yview)
            self.Productos.pack(side=LEFT, fill=BOTH, expand=True)

            self.Productos.heading(1, text="Código Barra", anchor=CENTER)
            self.Productos.heading(2, text="Código SKU", anchor=CENTER)
            self.Productos.heading(3, text="Nombre", anchor=CENTER)
            self.Productos.heading(4, text="Precio", anchor=CENTER)
            self.Productos.heading(5, text="Cantidad", anchor=CENTER)      #Nota: Que se calcule el margen solo (que no lo tenga que poner el usuario)
            self.Productos.heading(6, text="Medida", anchor=CENTER)
            self.Productos.heading(7, text="Categoría", anchor=CENTER)

            self.Productos.column(1,width=50, anchor=CENTER)
            self.Productos.column(2,width=50, anchor=CENTER)
            self.Productos.column(3,width=80, anchor=W)
            self.Productos.column(4,width=30, anchor=CENTER)
            self.Productos.column(5,width=20, anchor=CENTER)
            self.Productos.column(6,width=20, anchor=CENTER)
            self.Productos.column(7,width=50, anchor=W)

            self.updateProductos()


            # Configure Treeview style
            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview", background="#343434", rowheight=30, fieldbackground="#343434", foreground="white", font=("Helvetica", 9, BOLD))
            style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
            style.map("Treeview", background=[('selected', '#101010')])
            style.map("Treeview.Heading", background=[('active', '#101010')])

            self.Productos.place(x=0 ,y=0, height=427, width=754)
            self.current_table = "productos"

        else:
            print("La tabla de productos ya está visible.")

    def updateProductos(self):

        query = "SELECT Código_barra, Código_básico, Nombre, Precio, Cantidad, Unid_Medida, Categoria FROM producto"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        self.Productos.delete(*self.Productos.get_children())
        for i in rows:
            self.Productos.insert('', 'end', values=(i[0], i[1], i[2], '${}'.format(i[3]), i[4], i[5], i[6]))


    def searchProductos(self):
        
        q3=self.elemento.get()

        if self.current_table == "productos":

            query = f"SELECT Código_barra, Código_básico, Nombre, Precio, Cantidad, Unid_Medida, Categoria FROM producto WHERE Código_barra LIKE '%{q3}%' OR Nombre LIKE '%{q3}%' OR Categoria LIKE '%{q3}%'"
        
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.Productos.delete(*self.Productos.get_children())
            for i in rows:
                self.Productos.insert('', 'end', values=(i[0], i[1], i[2], '${}'.format(i[3]), i[4], i[5], i[6]))



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Tabla de Ventas ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    def emerge_tablaVentas(self):

        img_dir = os.getcwd()

        self.b8.config(relief = "sunken")
        self.b9.config(relief = "flat")
        self.b10.config(relief = "flat")


        if self.current_table != "ventas":

            if self.current_table == "productos":
                self.Productos.destroy()
                self.scrollProductos.destroy()
                self.frame_treeview.destroy()
                self.b15.place_forget()
                self.tarjeta_productos = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
                self.label_tarjetaProductos.config(image=self.tarjeta_productos)


            elif self.current_table == "compras":
                self.compras.destroy()
                self.scrollCompras.destroy()
                self.frame_treeview.destroy()
                self.tarjeta_compras = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Corta.png")
                self.label_tarjetaCompras.config(image=self.tarjeta_compras)

            else:
                self.agregar_panel_botones()

            #------------------------------------------------------------
            self.b0.config(command=self.searchVentas)
            self.b3.config(command=lambda: self.descargarReporte("ventas"))

            self.tarjeta_ventas = PhotoImage(file = f"{img_dir}/Imagenes/M. Inventario/Tarjeta Ventas.png")
            self.label_tarjetaVentas.config(image=self.tarjeta_ventas)

            #------------------------------------------------------------

            self.b2.config(command=self.abrir_gestion_ventas)

            self.botones_fecha("ventas")

            # Crea Frame que contenga el Treeview y scrollbar
            self.frame_treeview = Frame(self.window)
            self.frame_treeview.place(x=463, y=92, height=427, width=771)

            # Scrollbar
            self.scrollVentas = Scrollbar(self.frame_treeview)
            self.scrollVentas.pack(side=RIGHT, fill=Y)
            
            # Treeview
            self.ventas = ttk.Treeview(self.frame_treeview, columns=(1,2,3,4,5,6), show="headings", height=6, yscrollcommand=self.scrollVentas.set)
            self.scrollVentas.config(command=self.ventas.yview)

            # Configuración Treeview headings
            self.ventas.heading(1, text="Fecha")
            self.ventas.heading(2, text="Vendedor")
            self.ventas.heading(3, text="Num. Boleta")
            self.ventas.heading(4, text="Producto")
            self.ventas.heading(5, text="Cantidad")
            self.ventas.heading(6, text="Precio")

            # Configuracion Treeview columns
            self.ventas.column(1, width=25, anchor=CENTER)
            self.ventas.column(2, width=80, anchor=W)
            self.ventas.column(3, width=30, anchor=CENTER)
            self.ventas.column(4, width=80, anchor=W)
            self.ventas.column(5, width=25, anchor=CENTER)
            self.ventas.column(6, width=25, anchor=CENTER)

            # Consulta para obtener datos de ventas
            queryV = """SELECT v.Fecha, u.Nombre AS usuario, v.Num_Boleta, p.Nombre AS producto, v.Cantidad, v.Precio
                        FROM venta v
                        JOIN usuario u ON v.usuario_Rut = u.Rut
                        JOIN producto p ON v.Producto_Código_Barra = p.Código_Barra
                        ORDER BY v.Fecha DESC,  v.Num_Boleta DESC"""
            self.cursor.execute(queryV)
            rows = self.cursor.fetchall()
            self.updateVentas(rows)

            # Configuración Treeview style
            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview", background="#343434", rowheight=30, fieldbackground="#343434", foreground="white", font=("Helvetica", 9, BOLD))
            style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
            style.map("Treeview", background=[('selected', '#101010')])
            style.map("Treeview.Heading", background=[('active', '#101010')])
            

            self.ventas.place(x=0 ,y=0, height=427, width=754)
            self.current_table = "ventas"

        else:
            print("La tabla de ventas ya está visible.")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Actualizar Tabla de Ventas ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def updateVentas(self, rows):

        self.ventas.tag_configure('detalles_venta', background="#1d1d1d")  # Cambia los colores a tu gusto

        self.ventas.tag_configure('parent_venta_open', background='#101010', foreground='white')
        self.ventas.tag_configure('parent_venta', background='#343434', foreground='white')

        self.ventas.bind('<<TreeviewOpen>>', self.on_open)
        self.ventas.bind('<<TreeviewClose>>', self.on_close)


        self.ventas.delete(*self.ventas.get_children())
        boucher_previo = None
        productos_boleta = []
        fecha_venta = None

        for idx, i in enumerate(rows):
            num_boleta = i[2]
            if boucher_previo != num_boleta:
                # Si hay productos acumulados de la boleta anterior, inserta el total
                if productos_boleta:
                    total = sum(p[5] for p in productos_boleta)
                    self.ventas.insert(parent=fecha_venta, index='end', values=('- - - - - - - -','- - - - - - - - - - - - - - - - - - - -','- - - - - - - -','[TOTAL]', '', '${}'.format(total)), tags=('detalles_venta',))
                    productos_boleta = []
                # Nuevo parent para la nueva boleta
                fecha_venta = self.ventas.insert(parent='', index='end', values=(i[0], i[1], i[2]))
            # Inserta el producto como hijo
            self.ventas.insert(parent=fecha_venta, index='end', values=('- - - - - - - -','- - - - - - - - - - - - - - - - - - - -','- - - - - - - -',i[3], i[4], '${}'.format(i[5])), tags=('detalles_venta',))
            productos_boleta.append(i)
            boucher_previo = num_boleta
            
            # Si es el último producto de la lista, inserta el total
            if idx == len(rows) - 1:
                total = sum(p[5] for p in productos_boleta)
                self.ventas.insert(parent=fecha_venta, index='end', values=('- - - - - - - -','- - - - - - - - - - - - - - - - - - - -','- - - - - - - -','[TOTAL]', '', '${}'.format(total)), tags=('detalles_venta',))

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Buscar en Tabla de Ventas ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def searchVentas(self):
        
        q4= (self.elemento.get() or "").strip()
        desde = (self.entry1.get() or "").strip()
        hasta = (self.entry2.get() or "").strip()

        orden = "DESC" if self.orden_fecha == 'down' else "ASC" if self.orden_fecha == 'up' else ""
        base = f"""
            SELECT v.Fecha, u.Nombre AS usuario, v.Num_Boleta, p.Nombre AS producto, v.Cantidad, v.Precio
            FROM venta v
            JOIN producto p ON v.Producto_Código_Barra = p.Código_Barra
            JOIN usuario u ON v.Usuario_Rut = u.Rut
            WHERE 1=1
        """
        params = []

        if q4:
            base += " AND (v.Num_Boleta LIKE ? OR p.Nombre LIKE ? OR u.Nombre LIKE ?)"
            like = f"%{q4}%"
            params.extend([like, like, like])
        # añadir filtro por rango de fechas
        if desde and hasta:
            base += " AND v.Fecha BETWEEN ? AND ?"
            params.extend([desde, hasta])
        elif desde:
            base += " AND v.Fecha >= ?"
            params.append(desde)
        elif hasta:
            base += " AND v.Fecha <= ?"
            params.append(hasta)
        if orden:
            base += f" ORDER BY v.Fecha {orden}"

        self.cursor.execute(base, params)
        rows = self.cursor.fetchall()
        self.updateVentas(rows)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Limpiar Widgets ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def limpiarTabla(self):

        if self.current_table == "ventas":
            self.b8.config(relief="flat")
            self.ventas.delete()
            self.scrollVentas.destroy()
            self.frame_treeview.destroy()
            self.tarjeta_ventas = PhotoImage(file = f"{os.getcwd()}/Imagenes/M. Inventario/Tarjeta Corta.png")
            self.label_tarjetaVentas.config(image=self.tarjeta_ventas)
            self.entry1

        elif self.current_table == "compras":
            self.b10.config(relief="flat")
            self.compras.delete()
            self.scrollCompras.destroy()
            self.frame_treeview.destroy()
            self.tarjeta_compras = PhotoImage(file = f"{os.getcwd()}/Imagenes/M. Inventario/Tarjeta Corta.png")
            self.label_tarjetaCompras.config(image=self.tarjeta_compras)

        elif self.current_table == "productos":
            self.b9.config(relief="flat")
            self.Productos.delete()
            self.scrollProductos.destroy()
            self.frame_treeview.destroy()
            self.b15.place_forget()
            self.tarjeta_productos = PhotoImage(file = f"{os.getcwd()}/Imagenes/M. Inventario/Tarjeta Corta.png")
            self.label_tarjetaProductos.config(image=self.tarjeta_productos)

        self.b0.config(command=self.btn_clicked)
        self.b3.config(command=self.btn_clicked)
        self.frame_botones.destroy()
        self.botones_fecha("productos")
        self.current_table = "none"

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Descargar Reporte Compra/Producto/Venta ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def descargarReporte(self, tabla):
        
        respuesta = messagebox.askyesno("Descargar Reporte", "¿Desea descargar el reporte en formato CSV?")
        if respuesta:
            import csv
            import re
            import pandas as pd

            def parse_boleta(val):          # convierte números de boleta formateados como "Boleta #12345" a int 12345
                try:
                    if val is None or str(val).strip() == "":
                        return ""
                    # extrae dígitos y convierte a int
                    digits = re.sub(r"\D", "", str(val))
                    return int(digits) if digits != "" else ""
                except Exception:
                    return ""

            def parse_price(val):           # convierte precios formateados como $123.45 a float 123.45
                try:
                    if val is None or str(val).strip() == "":
                        return ""
                    s = str(val)
                    s = s.replace("$", "").replace(" ", "").replace(",", "")  # quitar signos de $ y espacios, y puntos de mil (si hay) -> asumir punto decimal
                    return float(s)
                except Exception:
                    return ""
            
            def clean_placeholder(val):     # convierte valores que son solo guiones u otros placeholders a vacío
                if val is None:
                    return ""
                if not isinstance(val, str):
                    return val
                s = val.strip()
                if s == "" or re.fullmatch(r"[-\s]+", s):       # si la celda contiene solo guiones y espacios -> vacío
                    return ""
                return s              # si viene formateado como $123 -> dejar para parse_price
            
            # <<<<<<<<<<<<<<<<  Descargar Reporte de Ventas  >>>>>>>>>>>>>>>>>>>
            if tabla == "ventas":
                
                cols = ["Fecha", "Vendedor", "Num. Boleta", "Producto", "Cantidad", "Precio"]
                path = "reporte_ventas.csv"

                # Guardar datos en CSV (incluye padres y sus hijos) con boleta y precio numéricos
                with open(path, mode="w", newline="", encoding="utf-8") as file:
                    csvwriter = csv.writer(file, delimiter=",")
                    csvwriter.writerow(cols)
                    # recorrer items raíz (boletas) y sus hijos (productos)
                    for parent_id in self.ventas.get_children():
                        parent_vals = tuple(self.ventas.item(parent_id, "values") or ())
                        parent_row = list(parent_vals) + [""] * (6 - len(parent_vals))
                        
                        parent_row = [clean_placeholder(v) for v in parent_row]     # limpiar posibles placeholders en las columnas del parent
                        parent_row[2] = parse_boleta(parent_row[2])                 # convertir Num. Boleta a número si existe
                        parent_row[5] = parse_price(parent_row[5])                  # si el parent tiene precio (raro) convertir también
                        csvwriter.writerow(parent_row)
                        # escribir hijos (productos) si existen
                        for child_id in self.ventas.get_children(parent_id):
                            child_vals = tuple(self.ventas.item(child_id, "values") or ())
                            child_row = list(child_vals) + [""] * (6 - len(child_vals))
                            
                            child_row = [clean_placeholder(v) for v in child_row]   # limpiar placeholders en la fila hija para que queden celdas vacías en Excel
                            try:
                                qty = child_row[4]
                                child_row[4] = int(qty) if str(qty).isdigit() else float(str(qty).replace(",", "")) if str(qty).strip() != "" else ""
                            except Exception:
                                child_row[4] = ""
                            child_row[5] = parse_price(child_row[5])
                        
                            csvwriter.writerow(child_row)

                if not csvwriter:
                    messagebox.showinfo("Información", "No hay datos para exportar.", parent=self.window)
                    return

                # Pedir al usuario dónde guardar el archivo .xlsx
                save_path = filedialog.asksaveasfilename(
                    parent=self.window,
                    defaultextension=".xlsx",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialfile="reporte_ventas.xlsx",
                    title="Guardar reporte como..."
                )
                if not save_path:
                    return  # el usuario canceló
                
            # <<<<<<<<<<<<<<<<  Descargar Reporte de Compras  >>>>>>>>>>>>>>>>>>>
            if tabla == "compras":

                cols = ["Fecha", "ID", "Formato", "Proveedor", "Producto", "Cantidad", "Costo"]
                path = "reporte_compras.csv"

                with open(path, mode="w", newline="", encoding="utf-8") as file:
                    csvwriter = csv.writer(file, delimiter=",")
                    csvwriter.writerow(cols)
                    for row_id in self.compras.get_children():
                        vals = tuple(self.compras.item(row_id, "values") or ())
                        row = list(vals) + [""] * (7 - len(vals))
                        
                        # limpiar posibles placeholders en la fila
                        row = [clean_placeholder(v) for v in row]

                        # convertir ID y Costo a numéricos
                        row[1] = parse_boleta(row[1])
                        row[6] = parse_price(row[6])
                        csvwriter.writerow(row)

                        for child_id in self.compras.get_children(row_id):
                            child_vals = tuple(self.compras.item(child_id, "values") or ())
                            child_row = list(child_vals) + [""] * (7 - len(child_vals))
                            
                            # limpiar posibles placeholders en la fila hija
                            child_row = [clean_placeholder(v) for v in child_row]

                            # convertir Cantidad y Costo a numéricos
                            try:
                                qty = child_row[5]
                                child_row[5] = int(qty) if str(qty).isdigit() else float(str(qty).replace(",", "")) if str(qty).strip() != "" else ""
                            except Exception:
                                child_row[5] = ""
                            child_row[6] = parse_price(child_row[6])
                            csvwriter.writerow(child_row)

                if not csvwriter:
                    messagebox.showinfo("Información", "No hay datos para exportar.", parent=self.window)
                    return

                # Pedir al usuario dónde guardar el archivo .xlsx
                save_path = filedialog.asksaveasfilename(
                    parent=self.window,
                    defaultextension=".xlsx",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialfile="reporte_compras.xlsx",
                    title="Guardar reporte como..."
                )
                if not save_path:
                    return

            # <<<<<<<<<<<<<<<<  Descargar Reporte de Productos  >>>>>>>>>>>>>>>>>>>
            if tabla == "productos":

                cols = ["Código Barra", "Código SKU", "Nombre", "Precio", "Cantidad", "Medida", "Categoría"]
                path = "reporte_productos.csv"

                with open(path, mode="w", newline="", encoding="utf-8") as file:
                    csvwriter = csv.writer(file, delimiter=",")
                    csvwriter.writerow(cols)
                    for row_id in self.Productos.get_children():
                        vals = tuple(self.Productos.item(row_id, "values") or ())
                        row = list(vals) + [""] * (7 - len(vals))
                        
                        # limpiar posibles placeholders en la fila
                        row = [clean_placeholder(v) for v in row]

                        # convertir Precio y Cantidad a numéricos
                        row[3] = parse_price(row[3])
                        try:
                            qty = row[4]
                            row[4] = int(qty) if str(qty).isdigit() else float(str(qty).replace(",", "")) if str(qty).strip() != "" else ""
                        except Exception:
                            row[4] = ""
                        csvwriter.writerow(row)

                if not csvwriter:
                    messagebox.showinfo("Información", "No hay datos para exportar.", parent=self.window)
                    return

                # Pedir al usuario dónde guardar el archivo .xlsx
                save_path = filedialog.asksaveasfilename(
                    parent=self.window,
                    defaultextension=".xlsx",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialfile="reporte_productos.xlsx",
                    title="Guardar reporte como..."
                )
                if not save_path:
                    return

            # Convertir CSV a Excel
            df = pd.read_csv(path)
            df.to_excel(save_path, sheet_name="Sheet1", index=False)
            messagebox.showinfo("Reporte Descargado", f"El reporte de {tabla} ha sido guardado en:\n{save_path}", parent=self.window)            





# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Todo lo Relacionado a la Ventana Calendario ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    def abrir_calendario(self):
        
        self.calendario = Toplevel(self.window)
        self.calendario.title("Calendario")
        self.calendario.geometry("300x394")

        self.canvas_cal = Canvas(
            self.calendario,
            bg = "#8c8c8c",
            height = 394,
            width = 300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas_cal.place(x = 0, y = 0)

        self.calendar_background = self.canvas_cal.create_image(
            150, 197,
            image=self.background_cal)

        self.date = Calendar(self.calendario, select_mode='day', date_pattern='y-mm-dd')
        self.date.place(x=0, y=0, width=300, height=290)

        # estado para selección de rango
        self._range_start = None            # date objeto inicio
        self._range_end = None              # date objeto fin
        self._range_event_ids = []          # ids de calevents creados para pintar
        self._range_tags = {                 # nombres de tags
            'edge': 'range_edge_tag',
            'middle': 'range_middle_tag'
        }

        # Hover preview ids
        self._hover_ids = []                 # ids temporales para preview
        self._last_hover_date = None

        # bind: cada vez que el usuario selecciona una fecha llamamos al handler
        self.date.bind("<<CalendarSelected>>", lambda e: self._on_calendar_select())
        # bind para preview en hover (después de haber elegido la primera fecha)
        self.date.bind("<Motion>", lambda e: self._on_calendar_hover(e))
        self.date.bind("<Leave>", lambda e: self._clear_hover_events())

        # ---------------------------------------------------------

        self.fecha_desde = StringVar()
        self.fecha_hasta = StringVar()
        self._feca_target = None

        entry0_bg = self.canvas_cal.create_image(
            68, 318,
            image = self.entry0_cal)
        
        entry0_cal = Entry(
            self.calendario,
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            highlightthickness = 0,
            textvariable = self.fecha_desde,
            state = "readonly",
            cursor = "arrow"
            )

        entry0_cal.place(
            x = 18, y = 305,
            width = 75,
            height = 27)

        entry1_bg = self.canvas_cal.create_image(
            232, 318,
            image = self.entry0_cal)
        
        entry1_cal = Entry(
            self.calendario,
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            highlightthickness = 0,
            textvariable = self.fecha_hasta,
            state = "readonly",
            cursor = "arrow"
            )
        entry1_cal.place(
            x = 182, y = 305,
            width = 75,
            height = 27)

        self.aceptar = Button(
            self.calendario, 
            bg = "#d9d9d9",
            command=self.aceptar_fecha, 
            cursor="hand2", 
            image=self.img0_cal, 
            borderwidth=0, 
            highlightthickness=0,
            relief="flat")
        
        self.aceptar.place(
            x=81, y=346, width=135, height=37)

    
    def aceptar_fecha(self):
        
        desde = StringVar(value=self.fecha_desde.get())
        hasta = StringVar(value=self.fecha_hasta.get())
        # year / month / day
        self.calendario.destroy()
        self.entry1.config(textvariable=desde)
        self.entry2.config(textvariable=hasta)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< [ Selección Rango en Calendario ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def _on_calendar_select(self):
        """Maneja clicks en el calendario para seleccionar inicio/fin y pintar el rango."""
        try:
            sel = self.date.selection_get()  # devuelve datetime.date
        except Exception:
            try:
                sel_str = self.date.get_date()
                sel = datetime.datetime.strptime(sel_str, "%Y-%m-%d").date()
            except Exception:
                return
            
        # al seleccionar una fecha, limpiar preview hover
        self._clear_hover_events()

        # primer click -> guardamos inicio y pintamos solo ese día como borde (oscuro)
        if not self._range_start or (self._range_start and self._range_end):
            # si ya teníamos un rango previo, reset completo
            self._reset_range()
            self._range_start = sel
            self._range_end = None
            self._create_event_for_date(sel, tag=self._range_tags['edge'])
            self.fecha_desde.set(sel.strftime("%Y-%m-%d"))
            return

        # segundo click -> guardamos fin y pintamos todos los días entre start y end
        if self._range_start and not self._range_end:
            self._range_end = sel
            start = min(self._range_start, self._range_end)
            end = max(self._range_start, self._range_end)

            # limpiar SOLO eventos previos (no tocar _range_start/_range_end)
            self._clear_range_events()

            # marcar start y end como edge
            self._create_event_for_date(self._range_start, tag=self._range_tags['edge'])
            self._create_event_for_date(self._range_end, tag=self._range_tags['edge'])

            # marcar intermedios
            d = start
            while d <= end:
                if d != self._range_start and d != self._range_end:
                    self._create_event_for_date(d, tag=self._range_tags['middle'])
                d += datetime.timedelta(days=1)

            self.fecha_desde.set(start.strftime("%Y-%m-%d"))
            self.fecha_hasta.set(end.strftime("%Y-%m-%d"))
            return
    

    def _on_calendar_hover(self, event):
        """Preview del rango mientras se mueve el ratón. Solo activo si existe _range_start y no _range_end."""
        if not getattr(self, '_range_start', None) or getattr(self, '_range_end', None):
            return

        # identificar día bajo el cursor
        day = None
        try:
            if hasattr(self.date, "identify_day"):
                day = self.date.identify_day(event.x, event.y)
        except Exception:
            day = None

        # fallback: buscar widget bajo el cursor y leer su texto (día)
        if not day:
            try:
                w = self.calendario.winfo_containing(event.x_root, event.y_root)
                if w:
                    txt = getattr(w, "cget", lambda k: None)("text")
                    if txt and str(txt).strip().isdigit():
                        day = txt.strip()
            except Exception:
                day = None
        if not day:
            self._clear_hover_events()
            return

        # obtener año/mes mostrados
        try:
            if hasattr(self.date, "get_displayed_month"):
                year, month = self.date.get_displayed_month()
            else:
                disp = getattr(self.date, "_date", None)
                year, month = (disp.year, disp.month) if disp else (datetime.date.today().year, datetime.date.today().month)
        except Exception:
            year, month = datetime.date.today().year, datetime.date.today().month

        try:
            hover_date = datetime.date(year, month, int(day))
        except Exception:
            self._clear_hover_events()
            return

        if getattr(self, "_last_hover_date", None) == hover_date:
            return
        self._last_hover_date = hover_date

        # limpiar preview anterior
        self._clear_hover_events()

        # calcular rango entre start y hover
        start = min(self._range_start, hover_date)
        end = max(self._range_start, hover_date)

        # crear calevents temporales para preview y aplicar color ligero
        color_edge = "#0b3a66"   # borde (oscuro)
        color_preview = "#cfe8ff" # interior (claro)

        d = start
        while d <= end:
            try:
                # crear evento temporal con tag 'hover_temp'
                eid = self.date.calevent_create(d, '', 'hover_temp')
                if eid is not None:
                    self._hover_ids.append(eid)
                    # intentar configurar estilo del evento
                    try:
                        # edge
                        if d == self._range_start or d == hover_date:
                            self.date.calevent_config(eid, background=color_edge, foreground="white")
                        else:
                            self.date.calevent_config(eid, background=color_preview, foreground="black")
                    except Exception:
                        # fallback set by date
                        try:
                            if d == self._range_start or d == hover_date:
                                self.date.calevent_set(date=d, background=color_edge, foreground="white")
                            else:
                                self.date.calevent_set(date=d, background=color_preview, foreground="black")
                        except Exception:
                            pass
            except Exception:
                pass
            d += datetime.timedelta(days=1)

    def _clear_hover_events(self):
        """Eliminar los eventos temporales del hover."""
        try:
            for eid in list(getattr(self, '_hover_ids', [])):
                try:
                    self.date.calevent_remove(id=eid)
                except TypeError:
                    try:
                        self.date.calevent_remove(eid)
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        self._hover_ids = []
        self._last_hover_date = None


    def _create_event_for_date(self, d: datetime.date, tag: str):
        """Crea un calevent para la fecha d y aplica color según tag (compatible con tkcalendar)."""
        try:
            # crear el evento con tag (según API de tkcalendar)
            eid = self.date.calevent_create(d, '', tag)
            if eid is None:
                return
            # guardar id y tag
            self._range_event_ids.append((eid, tag))
        except Exception:
            return

        # colores
        color_edge = "#0099FF"   # azul oscuro para bordes
        color_middle = "#7fb3ff" # azul claro para intermedios

        # aplicar configuración al evento (calevent_config)
        try:
            if tag == self._range_tags['edge']:
                self.date.calevent_config(eid, background=color_edge, foreground="white")
            else:
                self.date.calevent_config(eid, background=color_middle, foreground="black")
            return
        except Exception:
            pass

        # fallback: intentar set por date (si API lo permite)
        try:
            if tag == self._range_tags['edge']:
                self.date.calevent_set(date=d, background=color_edge, foreground="white")
            else:
                self.date.calevent_set(date=d, background=color_middle, foreground="black")
            return
        except Exception:
            pass

        # último recurso: colorear widget del día (no siempre fiable)
        try:
            day_widgets = self._find_day_widgets()
            for w, wdate in day_widgets:
                if wdate == d:
                    if tag == self._range_tags['edge']:
                        w.config(bg=color_edge, fg="white")
                    else:
                         w.config(bg=color_middle, fg="black")
                    break
        except Exception:
            pass
    def _clear_range_events(self):
        """Eliminar únicamente los calevents creados (no resetear start/end)."""
        try:
            for eid, _ in list(self._range_event_ids):
                try:
                    self.date.calevent_remove(id=eid)
                except TypeError:
                    try:
                        self.date.calevent_remove(eid)
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        self._range_event_ids = []
        self._last_hover_date = None
    

    def _reset_range(self):
        """Eliminar eventos y resetear inicio/fin del rango."""
        self._clear_range_events()
        # intentar eliminar tags también por compatibilidad
        try:
            self.date.calevent_remove(self._range_tags['edge'])
        except Exception:
            pass
        try:
            self.date.calevent_remove(self._range_tags['middle'])
        except Exception:
            pass
        # limpiar colores directos sobre widgets
        try:
            day_widgets = self._find_day_widgets()
            for w, _ in day_widgets:
                try:
                    w.config(bg='', fg='')
                except Exception:
                    pass
        except Exception:
            pass

        self._range_start = None
        self._range_end = None