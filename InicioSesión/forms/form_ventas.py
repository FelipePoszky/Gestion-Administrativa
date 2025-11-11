from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from tkinter import scrolledtext as tkst
from ttkwidgets.autocomplete import AutocompleteCombobox

import util.generic as utl
import util.variables
from datetime import date
from time import strftime
import sqlite3
import os


class ventas:

    #state = 1

    def lector_barras():

        print("Clicked")

# ------------------------------------>>> [    FUNCIONES IR A OTRAS VENTANAS    ] <<<---------------------------------------- #
    def GoMenuPrincipal(self):
        
        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()

    def GoMenuInventario(self):
        from forms.form_inventario import inventario
        self.window.destroy()
        inventario()
    
    def GoMenuCompras(self):
        from forms.form_compras import compras
        self.window.destroy()
        compras()

    def GoMenuReportes(self):
        from forms.form_reportes import reportes
        self.window.destroy()
        reportes()

# ------------------------------------>>> [    FUNCION MOSTRAR STOCK PRODUCTO    ] <<<---------------------------------------- #
    def mostrar_stock(self):

        self.entry4.configure(state="normal")
        self.entry5.configure(state="normal")

        self.labelProducto.place(
            x = 45, y = 250,
            width = 108,
            height = 27)

        self.labelStock.place(
            x = 44, y = 362,
            width = 84,
            height = 27)
        
        self.labelPrecio.place(
            x = 45, y = 474,
            width = 87,
            height = 27
        )
        
        self.b11.place(
            x = 299, y = 441,
            width = 107,
            height = 32)

        self.product_name = self.entry0.get()
        find_qty = "SELECT Cantidad, Unid_Medida, Nombre, Precio FROM producto WHERE Código_Barra LIKE '%"+self.product_name+"%' OR Nombre LIKE'%"+self.product_name+"%'"
        self.cursor.execute(find_qty)
        DatosProd = self.cursor.fetchall()

        for results in DatosProd:

            stock = results[0]
            self.unid = results[1]
            self.name = results[2]
            precio = results[3]

        self.qty.set('{} {}'.format(stock, self.unid))
        self.price.set('${} x {}'.format(precio, self.unid))
        self.text.set('{}'.format(self.name))

# ------------------------------------>>> [    FUNCION AÑADIR PRODUCTO A BOLETA    ] <<<---------------------------------------- #
    def añadirProducto(self):

        self.Scrolledtext1.configure(state="normal")
        strr = self.Scrolledtext1.get('2.0', END)
        if strr.find('Total')==-1:
            self.product_name = self.entry0.get()

            if(self.product_name!=""):
                product_qty = self.entry4.get()
                find_mrp = "SELECT Precio, Cantidad FROM producto WHERE Código_Barra LIKE '%"+self.product_name+"%' OR Nombre LIKE '%"+self.product_name+"%'"
                self.cursor.execute(find_mrp)
                results = self.cursor.fetchall()
                stock = results[0][1]
                mrp = results[0][0]

                if product_qty.isdigit()==True:

                    if (stock-int(product_qty))>=0:

                        sp = mrp*int(product_qty)
                        existing = None
                        for it in self.cart.items:
                            if it.product_name == self.product_name:
                                existing = it
                                break
                        if existing:
                            # preguntar si se reemplaza la línea
                            resp = messagebox.askyesno("Producto ya agregado",
                                                       f"El producto '{self.product_name}' ya está en la boleta.\n¿Desea reemplazar la línea con Cantidad={product_qty} y Precio={mrp*int(product_qty)}?",
                                                       parent=self.window)
                            if resp:
                                existing.qty = int(product_qty)
                                print(mrp)
                                existing.price = self.verificarDescuento('agregar', mrp) if self.entry5.get() != '' and self.entry5.get().isdigit() else mrp
                                # reconstruir la vista y total
                                self.render_cart()
                            else:
                                # no reemplaza, no hace nada
                                pass
                        else:
                            precio = self.verificarDescuento('agregar', mrp) if self.entry5.get() != '' and self.entry5.get().isdigit() else mrp
                            item = Item(self.product_name, precio, int(product_qty), self.unid)
                            self.cart.add_item(item)
                            # actualizar vista
                            self.render_cart()

                    else:
                        self.Scrolledtext1.configure(state="disabled")
                        messagebox.showerror("Oops!", "Fuera de stock. Verifica la Cantidad.", parent=self.window)
                else:
                    self.Scrolledtext1.configure(state="disabled")
                    messagebox.showerror("Oops!", "Cantidad Invalida", parent=self.window)
            else:
                self.Scrolledtext1.configure(state="disabled")
                messagebox.showerror("Oops!", "Ingresa un producto", parent=self.window)
        else:
            self.Scrolledtext1.delete('1.0', END)
            new_li = []
            li = strr.split("\n")
            for i in range(len(li)):
                if len(li[i])!=0:
                    if li[i].find('Total')==-1:
                        new_li.append(li[i])
                    else:
                        break
            for j in range(len(new_li)-1):
                self.Scrolledtext1.insert('insert', new_li[j])
                self.Scrolledtext1.insert('insert','\n')
            self.product_name = self.entryCod.get()
            
            if(self.product_name!=""):

                product_qty = self.entryCantidad.get()
                find_mrp = "SELECT Precio, Cantidad, Código_Barra FROM producto WHERE Nombre LIKE '%"+self.product_name+"%' OR Código_Barra LIKE '%"+self.product_name+"%'"
                self.cursor.execute(find_mrp)
                results = self.cursor.fetchall()
                stock = results[0][1]
                mrp = results[0][0]
                if product_qty.isdigit()==True:

                    if (stock-int(product_qty))>=0:

                        sp = results[0][0]*int(product_qty)
                        existing = None
                        for it in self.cart.items:
                            if it.product_name == self.product_name:
                                existing = it
                                break
                        if existing:
                            resp = messagebox.askyesno("Producto ya agregado",
                                                       f"El producto '{self.product_name}' ya está en la boleta.\n¿Desea reemplazar la línea con Cantidad={product_qty} y Precio={mrp*int(product_qty)}?",
                                                       parent=self.window)
                            if resp:
                                existing.qty = int(product_qty)
                                existing.price = mrp
                                self.render_cart()
                            else:
                                pass
                        else:
                            item = Item(self.product_name, mrp, int(product_qty), self.unid)
                            self.cart.add_item(item)
                            self.render_cart()
                    else:
                        messagebox.showerror("Oops!", "Fuera de stock. Verifica la Cantidad.", parent=self.window)
                else:
                    messagebox.showerror("Oops!", "Cantidad Invalida.", parent=self.window)
            else:
                messagebox.showerror("Oops!", "Ingresa un producto.", parent=self.window)


# ------------------------------------>>> [    FUNCION RENDERIZAR BOLETA    ] <<<---------------------------------------- #
    def render_cart(self):

        self.Scrolledtext1.configure(state="normal")
        self.Scrolledtext1.delete('1.0', END)
        self.Scrolledtext1.insert('insert', "\n")
        total = 0
        for it in self.cart.items:
            sp = it.price * it.qty
            # Linea de la Boleta Con los datos del producto
            bill_text = "\t{}\t\t\t\t {} {}\t\t ${}\n".format(it.product_name, it.qty, it.unid, sp)
            self.Scrolledtext1.insert('insert', bill_text)
            total += sp
        self.Scrolledtext1.configure(state="disabled")
        self.sumas = total
        self.totalBol.set("${}".format(total))
        # limpiar semiTotal y recomponer si tu flujo lo necesita
        self.cart.semiTotal = [it.price * it.qty for it in self.cart.items]
        #limpiar campos
        self.limpiarSeleccion()

# ------------------------------------>>> [    FUNCION GENERAR TOTAL EN BOLETA    ] <<<---------------------------------------- #
    def generarTotal(self):

        if self.cart.isEmpty():
            messagebox.showerror("Oops!", "Añade un producto.", parent=self.window)
        else:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                self.Scrolledtext1.configure(state="normal")
                divider = "\n\n\n"+("─"*51)
                self.Scrolledtext1.insert('insert', divider)
                total = "\n    Total\t\t\t\t\t$ {}".format(self.cart.total())
                self.Scrolledtext1.insert('insert', total)
                divider2 = "\n"+("─"*51)
                self.Scrolledtext1.insert('insert', divider2)
                self.Scrolledtext1.configure(state="disabled")
                
            else:
                return
    #state = 1

# ------------------------------------>>> [    FUNCION LIMPIAR BOLETA    ] <<<---------------------------------------- #
    def limpiarBoleta(self):

        self.sumas = 0
        self.totalBol.set("")

        self.Scrolledtext1.configure(state="normal")
        self.Scrolledtext1.delete(1.0, END)
        self.Scrolledtext1.configure(state="disabled")

        self.cart.remove_items()
        self.state = 1

# ------------------------------------>>> [    FUNCION LIMPIAR SELECCION PRODUCTO    ] <<<---------------------------------------- #
    def limpiarSeleccion(self):

        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

        self.entry4.configure(state="readonly")
        self.entry5.configure(state="readonly")

        self.labelProducto.place_forget()
        self.labelStock.place_forget()
        self.labelPrecio.place_forget()
        self.marcoDesc.place_forget()
        self.desc_label.place_forget()

        try:
            self.qty.set('')
            self.text.set('')
            self.price.set('')
            self.desc.set('')

        except AttributeError:
            pass

# ------------------------------------>>> [    FUNCION REMOVER PRODUCTO DE BOLETA   ] <<<---------------------------------------- #
    def removerProducto(self):

        producto_encontrado = False

        if(self.cart.isEmpty()!=True):
            for item in self.cart.items:
                if item.product_name == self.entry0.get():
                    producto_encontrado = True
                    break

            if producto_encontrado:
                resultado = messagebox.askyesno("Remover Producto", "¿Estás seguro de remover el producto seleccionado?", parent=self.window)
                if resultado:
                    self.Scrolledtext1.configure(state="normal")
                    strr = self.Scrolledtext1.get('1.0', END)
                    if strr.find('Total')==-1:
                        try:
                            productoRemovido = self.entry0.get()
                            self.cart.remove_item(productoRemovido)
                        except IndexError:
                            messagebox.showerror("Oops!", "La Tabla esta vacia.", parent=self.window)
                        else:
                            self.Scrolledtext1.configure(state="normal")
                            lines = strr.splitlines()
                            filtered_lines = []
                            for line in lines:
                                if productoRemovido not in line:
                                    filtered_lines.append(line)

                            self.Scrolledtext1.delete('1.0', END)
                            self.Scrolledtext1.insert('1.0', '\n'.join(filtered_lines))
                            self.Scrolledtext1.configure(state="disabled")

                            self.totalBol.set("${}".format(self.cart.total()))

                            if(self.cart.isEmpty()):
                                self.sumas = 0
                                self.totalBol.set("${}".format(self.sumas))

            else:
                messagebox.showerror("Oops!", "El producto no está en la boleta.", parent=self.window)


# ------------------------------------>>> [    FUNCION VERIFICAR DESCUENTO    ] <<<---------------------------------------- #

    def verificarDescuento(self, procede, precio):

        if self.entry5.get()=='' or self.entry5.get().isdigit()==False:
            messagebox.showerror("Oops!", "Ingrese un valor de descuento válido.", parent=self.window)
            return
        
        if int(self.entry5.get())<0 or int(self.entry5.get())>100:
            messagebox.showerror("Oops!", "Ingrese un valor de descuento entre 0 y 100.", parent=self.window)
            return

        cant = self.entry4.get()
        if cant=='' or cant.isdigit()==False:
            messagebox.showerror("Oops!", "Ingrese una cantidad válida antes de aplicar el descuento.", parent=self.window)
            return

        if procede == 'boton':
            producto = self.entry0.get()
            find_price = "SELECT Precio FROM producto WHERE Código_Barra LIKE '%"+producto+"%' OR Nombre LIKE '%"+producto+"%'"
            self.cursor.execute(find_price)
            result = self.cursor.fetchone()
            if result:
                precio = result[0]
            else:
                self.price.set("No encontrado")

            self.marcoDesc.place(
                x = 147, y = 511,
                width = 155, height = 33
            )
            self.desc_label.place(
                x = 173, y = 515)
        
            valor_original = precio * int(cant)
            descuento = int(self.entry5.get())
            valor_descuento = valor_original * (descuento / 100)
            valor_final = round(valor_original - valor_descuento)
            self.desc.set("Total: ${}".format(valor_final))

        else:
            descuento = int(self.entry5.get())
            valor_descuento = precio * (descuento / 100)
            valor_final = round(precio - valor_descuento)
            
            return valor_final
        
# ------------------------------------>>> [    FUNCION GENERAR Y ALMACENAR VENTA    ] <<<---------------------------------------- #
    def generarVenta(self):

        if self.cart.isEmpty():
            messagebox.showerror("Oops!", "Añade un producto.", parent=self.window)
        else:
            respuesta = messagebox.askyesno("Confirmar Venta", "¿Estás seguro de que deseas confirmar la venta?", parent=self.window)
            if respuesta:
                for item in self.cart.items:
                    self.cursor.execute("SELECT Código_Barra FROM producto WHERE Nombre = ?", (item.product_name,))
                    producto_codigo = self.cursor.fetchone()[0]
                    venta_precio = item.price*item.qty
                    query = "INSERT INTO venta (Num_Boleta, usuario_Rut, Fecha, Producto_Código_Barra, Precio, Cantidad) VALUES(?, ?, ?, ?, ?, ?)"
                    self.cursor.execute(query, (self.BolPresente, self.rut, self.fecha.get(), producto_codigo, venta_precio, item.qty))
                    # Actualizar stock
                    self.cursor.execute("UPDATE producto SET Cantidad = Cantidad - ? WHERE Código_Barra = ?", (item.qty, producto_codigo))
                self.cursor.execute("UPDATE veguita SET Ultima_Boleta_Realizada = ? ", (self.BolPresente,))
                self.mydb.commit()
                messagebox.showinfo("Venta Confirmada", "La venta ha sido confirmada. \nGenerando Boleta N°{}".format(self.BolPresente) , parent=self.window)
                # Incrementar el número de boleta para la próxima venta
                self.BolPresente += 1
                # Limpiar la boleta actual
                self.limpiarBoleta()
                # Actualizar el campo de N° Boleta
                self.entry1.config(state="normal")
                self.entry1.delete(0, END)
                self.entry1.insert(0, self.BolPresente)
                self.entry1.config(state="readonly")


    #------------------------------------>>> [    INICIO VENTANA    ] <<<---------------------------------------- #

    def __init__(self):

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()

        img_dir = os.getcwd()

        self.window = Tk()

        self.window.geometry("1260x625")
        self.window.configure(bg = "#8c8c8c")
        utl.centrar_ventana(self.window, 1260, 625)

        self.fecha = StringVar()
        self.sumas = 0
        self.cart=Cart()

        canvas = Canvas(
            self.window,
            bg = "#8c8c8c",
            height = 625,
            width = 1260,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/background.png")
        background = canvas.create_image(
            630, 312.5,
            image=background_img)

        # ------------------------------------>>> [    Datos Variables    ] <<<--------------------------------- #

        # >>>>>> Producto <<<<<<
        imgProducto = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/Producto.png")
        self.labelProducto = Label(
            image = imgProducto,
            borderwidth = 0,
            highlightthickness = 0
            )


        self.text = StringVar()
        self.product_label = Label(bg='#464646', textvariable = self.text, fg='#101010', font=("Arial bold", 10))
        self.product_label.place(
            x = 149, y = 253)

        # >>>>>> Stock <<<<<<
        imgStock = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/Stock.png")
        self.labelStock = Label(
            image = imgStock,
            borderwidth = 0,
            highlightthickness = 0
            )
        
        self.qty = StringVar()
        self.qty_label = Label(bg='#464646', textvariable = self.qty, fg='#101010', font=("Arial bold", 10))
        self.qty_label.place(
            x = 123, y = 366)
        
        # >>>>>>> Precio <<<<<<
        imgPrecio = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/Precio.png")
        self.labelPrecio = Label(
            image = imgPrecio,
            borderwidth = 0,
            highlightthickness = 0
            )
        
        self.price = StringVar()
        self.price_label = Label(bg='#464646', textvariable = self.price, fg='#101010', font=("Arial bold", 10))
        self.price_label.place(
            x = 129, y = 477)
        
        # >>>>>> Verificar Desc. <<<<<<
        imgDesc = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/Descuento.png")
        self.marcoDesc = Label(
            image = imgDesc,
            borderwidth = 0,
            highlightthickness = 0
            )
        
        self.desc = StringVar()
        self.desc_label = Label(bg='#d9d9d9', textvariable = self.desc, fg='#101010', font=("Arial bold", 11))
        
        # >>>>>> Total Boleta <<<<<<
        self.totalBol = StringVar()
        self.totalLabel = Label(bg='#464646', textvariable=self.totalBol, fg='#d9d9d9', font=("Inter", 14, BOLD))
        self.totalLabel.place(
            x=1138, y=555)

        

        # >>---------------------->>> [ TABLA DE BOLETA ] <<<-------------------------->

        headers = PhotoImage(file= f"{img_dir}/Imagenes/M. Ventas/headers.png")
        self.labelHeaders = Label(
            image = headers,
            borderwidth = 0,
            highlightthickness = 0
            )
        self.labelHeaders.place(
            x = 431, y = 165,
            width = 606,
            height = 32)

        self.Scrolledtext1 = tkst.ScrolledText(borderwidth=0, bg='#D9D9D9', state="disabled", highlightthickness=0, font=("Podkova", 11))
        self.Scrolledtext1.place(x=431, y=201, width=606, height=399)

        # ------------------------------------>>> [    Entrys Automaticos    ] <<<---------------------------------------- #

        self.rut = util.variables.logged_user

        ObtenUsu = "SELECT Nombre FROM usuario WHERE Rut = ?"
        DatosUsu = self.cursor.execute(ObtenUsu, (self.rut,)).fetchone()

        nombreUsu = DatosUsu[0]

        ObtenBoleta = 'SELECT Boleta_Inicio, Boleta_Fin, Ultima_Boleta_Realizada FROM veguita'
        datos = self.cursor.execute(ObtenBoleta, ()).fetchall()
        
        for results in datos:

            BolInicial = results[0]
            BolFinal = results[1]
            self.BolPresente = results[2]
        
        if (self.BolPresente==False):
            self.BolPresente == BolInicial

        elif (self.BolPresente==BolFinal):
            messagebox.showerror(message="Ha realizado todas sus boletas, debe actualizar sus datos en Ventana datos pyme", title="Problema Boletas")

        else:
            self.BolPresente += 1


        # >>>> N° Boleta <<<<<

        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img_textBox1.png")
        entry1_bg = canvas.create_image(
            272, 111,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#656565",
            highlightthickness = 0
            )
        self.entry1.insert(0, self.BolPresente)
        self.entry1.config(state="readonly", readonlybackground="#656565", foreground="white", font=("Arial bold", 11))

        self.entry1.place(
            x = 160, y = 97,
            width = 216.0,
            height = 28)

        #  >>>> Vendedor <<<<<
        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img_textBox2.png")
        entry2_bg = canvas.create_image(
            682, 111,
            image = entry2_img)

        entry2 = Entry(
            bd = 0,
            bg = "#656565",
            highlightthickness = 0)
        
        entry2.insert(0, nombreUsu)
        entry2.config(state="readonly", readonlybackground="#656565", foreground="white", font=("Arial bold", 11))

        entry2.place(
            x = 570, y = 97,
            width = 216.0,
            height = 28)
        
        # >>>> Fecha <<<<<
        self.fecha.set(str(date.today()))

        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img_textBox3.png")
        entry3_bg = canvas.create_image(
            1075, 111,
            image = entry3_img)

        entry3 = Entry(
            bd = 0,
            bg = "#656565",
            highlightthickness = 0)

        entry3.insert(0, self.fecha.get())
        entry3.config(state="readonly", readonlybackground="#656565", foreground="white", font=("Arial bold", 11))

        entry3.place(
            x = 963, y = 97,
            width = 216.0,
            height = 28)
        
        # -------------------------- -->>> [   Entrys Ingresados Por Usuario ] <<<------------------------------------ #
        
        # x = entry + 119 , y = entry + 14

        query = "SELECT Nombre FROM producto"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        productos = [fila[0] for fila in resultados]

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img_textBox0.png")
        entry0_bg = canvas.create_image(
            168, 230,
            image = entry0_img)

        style = ttk.Style()
        style.map("TCombobox", fieldbackground=[('readonly', "#d9d9d9"), ('!disabled', "#656565")])
        style.map("TCombobox", selectbackground=[('readonly', "#d9d9d9")])

        self.entry0 = AutocompleteCombobox(
            completevalues=productos)

        self.entry0.place(
            x = 49, y = 216,
            width = 230.0,
            height = 28) # 90

        #   >>>>>> Cantidad <<<<<<

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img_textBox4.png")
        entry4_bg = canvas.create_image(
            168, 342,
            image = entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0,
            readonlybackground = "#D9D9D9",
            state="readonly")

        self.entry4.place(
            x = 49, y = 328,
            width = 230.0,
            height = 28)

        # >>> Descuentos <<<
        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img_textBox5.png")
        entry5_bg = canvas.create_image(
            168, 454,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            textvariable = '0',
            readonlybackground = "#D9D9D9",
            state="readonly",
            highlightthickness = 0)

        self.entry5.place(
            x = 49, y = 440,
            width = 230.0,
            height = 28)

        # ----------------------------------->>>>> [    Botones Accion Producto   ] <<<<<<<--.----------------------------------- #

        # >>>>>> Botones Productos <<<<<

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.mostrar_stock,
            cursor = "hand2",
            relief = "flat")

        b0.place(
            x = 340, y = 212,
            width = 66,
            height = 38)

        img12 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img12.png")
        b12 = Button(
            image = img12,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.lector_barras, # USAR LECTOR DE BARRAS
            cursor = "hand2",
            relief = "flat")

        b12.place(
            x = 301, y = 215,
            width = 34,
            height = 35)

        img11 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img11.png")
        self.b11 = Button(
            image = img11,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.verificarDescuento('boton', None), # VERIFICAR DESCUENTO
            cursor = "hand2",
            relief = "flat")


        img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.removerProducto,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 50, y = 553,
            width = 109,
            height = 46)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiarSeleccion,
            cursor = "hand2",
            relief = "flat")

        b2.place(
            x = 169, y = 553,
            width = 109,
            height = 46)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.añadirProducto,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 289, y = 553,
            width = 109,
            height = 46)
        
        # ----------------------------------->>>>>>    Botones Boleta    <<<<<---------------------------------------- #

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.generarTotal,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 1082, y = 211,
            width = 112,
            height = 46)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiarBoleta,
            cursor = "hand2",
            relief = "flat")

        b5.place(
            x = 1082, y = 384,
            width = 112,
            height = 44)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img6.png")
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.generarVenta,
            cursor = "hand2",
            relief = "flat")

        b6.place(
            x = 1082, y = 298,
            width = 112,
            height = 46)

        # ----------------->>>>>>>>>>>    BOTONES DE NAVEGACION SUPERIORES    <<<<<<<<<<<<---------------- #

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img7.png")
        b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuPrincipal,
            cursor = "hand2",
            relief = "flat")

        b7.place(
            x = 117, y = 12,
            width = 117,
            height = 46)

        img8 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img8.png")
        b8 = Button(
            image = img8,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuInventario,
            cursor = "hand2",
            relief = "flat")

        b8.place(
            x = 389, y = 12,
            width = 146,
            height = 46)

        img9 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img9.png")
        b9 = Button(
            image = img9,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuCompras,
            cursor = "hand2",
            relief = "flat")

        b9.place(
            x = 557, y = 12,
            width = 143,
            height = 46)

        img10 = PhotoImage(file = f"{img_dir}/Imagenes/M. Ventas/img10.png")
        b10 = Button(
            image = img10,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuReportes,
            cursor = "hand2",
            relief = "flat")

        b10.place(
            x = 722, y = 12,
            width = 140,
            height = 46)

        self.window.resizable(False, False)
        self.window.mainloop()

#--------------------------------------->>> [ Clase Item para almacenar productos] >>>-------------------------------------------------

class Item:

    def __init__(self, name, price, qty, unid):

        self.product_name = name
        self.price = price
        self.qty = qty
        self.unid = unid
    
    def __repr__(self):
        return f"Item(producto={self.product_name}, precio={self.price}, cantidad={self.qty}, unidad={self.unid})"


#--------------------------------------->>> [ Clase Cart/Boleta para remover/añadir/calcular totales] >>>-------------------------------------------------

class Cart:
    
    def __init__(self):
        self.items = []
        self.dictionary = {}
        self.semiTotal = []

    def add_item(self, item):
        self.items.append(item)
        print("Cart: ", self.items)

    def remove_item(self, producto):

        self.items = [item for item in self.items if item.product_name != producto]
        self.semiTotal = [item.price * item.qty for item in self.items]
        print("remove_item|semiTotal: ", self.semiTotal)
        print("remove_item|items: ", self.items)


    def remove_items(self):
        self.items.clear()
        self.semiTotal.clear()

    def total(self):
        total = 0

        for i in self.items:
            semi=0
            total += i.price * i.qty
            
            semi = i.price * i.qty
            self.semiTotal.append(semi)
        print("total, semiTotal",self.semiTotal)
        print("total, total",total)
        return total

    def isEmpty(self):

        if len(self.items)==0:
            return True
        
    def allCart(self):

        for i in self.items:

            if (i.product_name in self.dictionary):
                self.dictionary[i.product_name] += i.qty

            else:
                self.dictionary.update({i.product_name:i.qty})