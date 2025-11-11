from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import customtkinter

from forms.form_inventario import inventario
from forms.form_ventas import ventas

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import calendar
import datetime
import threading
import util.generic as utl
import os
import sqlite3
import numpy as np

class reportes:

    def GoMenuPrincipal(self):
        
        from forms.form_master import MasterPanel
        self._safe_close_and_open(lambda: MasterPanel())

    
    def GoMenuInventario(self):

        self._safe_close_and_open(lambda: inventario())

    def GoMenuVentas(self):
        
        self._safe_close_and_open(lambda: ventas())

    def GoMenuCompras(self):
    
        from forms.form_compras import compras as _compras
        self._safe_close_and_open(lambda: _compras())
    

# ---------------------------- >>> [ INICIO DE LA CLASE PRINCIPAL ] >>>------------------------------------------------- #
    def __init__(self):

        img_dir = os.getcwd()
        self._after_ids = []  # Lista para almacenar los IDs de after
        self._canvases = []
        self._figures = []

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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Reportes/Background.png")
        background = self.canvas.create_image(
            630, 312.5,
            image=background_img)

    # >>>>>>>>>>>>>>>>>>>>>>> [ Botones Barra Navegador ] <<<<<<<<<<<<<<<<<<<<<<<<

        img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Reportes/Button.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuPrincipal,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 116, y = 11,
            width = 119,
            height = 45)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Reportes/Button (1).png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuVentas,
            cursor = "hand2",
            relief = "flat")

        b2.place(
            x = 252, y = 11,
            width = 119,
            height = 45)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Reportes/Button (2).png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuInventario,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 387, y = 11,
            width = 150,
            height = 45)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Reportes/Button (3).png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.GoMenuCompras,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 555, y = 11,
            width = 147,
            height = 45)

    ####################################################    [CONTENIDO]    ##########################################################

        # ------[ Ventana Scrolleable ]------
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.window, fg_color="#8c8c8c",)
        self.scrollable_frame.pack(fill=BOTH, expand=True, pady=(65, 0))


        # >>>> Contenedor Para 4 Frames en Fila <<<<
        row_frame = Frame(self.scrollable_frame, bg="#8c8c8c")
        row_frame.pack(pady=10, padx=3, fill=X)

        # >>>>>>>>>>>>>>>>>>>>>>>>> [ Recuadro Resumen Total Ventas ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_totalventas = Frame(row_frame, relief="flat", bg="#8c8c8c", width=298, height=96)
        self.frame_totalventas.grid(row=0, column=0, padx=7, sticky="nsew")

        self.img5 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash.png")
        bg_totalventas = Label(self.frame_totalventas, image=self.img5, bg="#8c8c8c")
        bg_totalventas.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg_totalventas = bg_totalventas  # Guarda referencia si la necesitas

        self.frame_totalventas.grid_propagate(False)

        bg_totalventas.bind("<Enter>", lambda e: bg_totalventas.config(cursor="hand2"))
        bg_totalventas.bind("<Leave>", lambda e: bg_totalventas.config(cursor=""))
        #bg_totalventas.bind("<Button-1>", self.push_totalVentas)


        # >>>>>>>>>>>>>>>>>>>>>>>> [ Recuadro Total Ganancias ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_totalGanancias = Frame(row_frame, bg="#8c8c8c", width=291, height=92)
        self.frame_totalGanancias.grid(row=0, column=1, padx=7, sticky="nsew")


        self.img6 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (1).png")
        bg_totalGanancias = Label(self.frame_totalGanancias, image=self.img6, bg="#8c8c8c")
        bg_totalGanancias.pack(expand=True, fill="both")

        self.frame_totalGanancias.grid_propagate(False)

        # >>>>>>>>>>>>>>>>>>>>>>> [ Frame Valor Stock Total ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_ValorStock = Frame(row_frame, bg="#8c8c8c", width=291, height=92)
        self.frame_ValorStock.grid(row=0, column=2, padx=7, sticky="nsew")

        self.img7 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (2).png")
        bg_ValorStock = Label(self.frame_ValorStock, image=self.img7, bg="#8c8c8c")
        bg_ValorStock.pack(expand=True, fill="both")

        self.frame_ValorStock.grid_propagate(False)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>> [ Frame Plus ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_plus = Frame(row_frame, bg="#8c8c8c", width=291, height=92)
        self.frame_plus.grid(row=0, column=3, padx=7, sticky="nsew")

        self.img8 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (3).png")
        bg_plus = Label(self.frame_plus, image=self.img8, bg="#8c8c8c")
        bg_plus.pack(expand=True, fill="both")

        self.frame_plus.grid_propagate(False)

        for i in range(4):
            row_frame.grid_columnconfigure(i, weight=1)


        # >>>>> Contenedor Para 3 Frames Segunda Fila <<<<<
        second_row = Frame(self.scrollable_frame, bg="#8c8c8c")
        second_row.pack(pady=10, padx=3, fill=X)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>> [ Frame Grafica Ventas ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_graficaVentas = Frame(second_row, bg="#8c8c8c", width=391, height=334)
        self.frame_graficaVentas.grid(row=0, column=0, padx=7, sticky="nsew")

        self.img9 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (4).png")
        bg_graficaVentas = Label(self.frame_graficaVentas, image=self.img9, bg="#8c8c8c")
        bg_graficaVentas.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_graficaVentas.grid_propagate(False)

        # >>>>>>>>>>>>>>>>>>>>>>>>> [ Frame Grafica ventas/compras ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_graficaIntercambio = Frame(second_row, bg="#8c8c8c", width=391, height=326)
        self.frame_graficaIntercambio.grid(row=0, column=1, padx=7, sticky="nsew")

        self.img10 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (5).png")
        bg_graficaIntercambio = Label(self.frame_graficaIntercambio, image=self.img10, bg="#8c8c8c")
        bg_graficaIntercambio.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_graficaIntercambio.grid_propagate(False)


        # >>>>>>>>>>>>>>>>>>>>>>>>> [ Frame Grafica Productos Top ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_graficaTop = Frame(second_row, bg="#8c8c8c", width=391, height=326)
        self.frame_graficaTop.grid(row=0, column=2, padx=7, sticky="nsew")

        self.img11 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (6).png")
        bg_graficaTop = Label(self.frame_graficaTop, image=self.img11, bg="#8c8c8c")
        bg_graficaTop.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_graficaTop.grid_propagate(False)

        for i in range(3):
            second_row.grid_columnconfigure(i, weight=1)

        # >>>>> Contenedor Para 3 Frames de la 3era. Fila <<<<<
        third_row = Frame(self.scrollable_frame, bg="#8c8c8c")
        third_row.pack(pady=10, padx=3, fill=X)


        # >>>>>>>>>>>>>>>>>>>>>>> [ Frame Grafica Ganancias ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_graficaGanancias = Frame(third_row, bg="#8c8c8c", width=391, height=334)
        self.frame_graficaGanancias.grid(row=0, column=0, padx=7, sticky="nsew")

        self.img12 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (7).png")
        bg_graficaGanancias = Label(self.frame_graficaGanancias, image=self.img12, bg="#8c8c8c")
        bg_graficaGanancias.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_graficaGanancias.grid_propagate(False)

        # >>>>>>>>>>>>>>>>>>>>>>>> [ Frame Grafica Top Proveedores ] <<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_graficaProveedores = Frame(third_row, bg="#8c8c8c", width=391, height=326)
        self.frame_graficaProveedores.grid(row=0, column=1, padx=7, sticky="nsew")

        self.img13 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (8).png")
        bg_graficaProveedores = Label(self.frame_graficaProveedores, image=self.img13, bg="#8c8c8c")
        bg_graficaProveedores.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_graficaProveedores.grid_propagate(False)

        # >>>>>>>>>>>>>>>>>>>>>> [ Frame Tabla Stock ] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.frame_tablaStock = Frame(third_row, bg="#8c8c8c", width=391, height=326)
        self.frame_tablaStock.grid(row=0, column=2, padx=7, sticky="nsew")

        self.img14 = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Dash (9).png")
        bg_tablaStock = Label(self.frame_tablaStock, image=self.img14, bg="#8c8c8c")
        bg_tablaStock.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_tablaStock.grid_propagate(False)

        for i in range(3):
            third_row.grid_columnconfigure(i, weight=1)

        # >>>>> Imagenes Estados <<<<<
        
        self.est_critico = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Critico.png")
        self.est_bajo = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Bajo.png")
        self.est_medio = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Medio.png")
        self.est_bueno = PhotoImage(file=f"{img_dir}/Imagenes/M. Reportes/Bueno.png")
        
        # >>>> Hilos <<<< 

        threading.Thread(target=self.generar_reportes, daemon=True).start()
        
        self.window.resizable(False, False)
        self.window.mainloop()

#################################################################################################################################

    def generar_reportes(self):

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()

        # Datos Gráficas
        meses_info = self.obtener_ultimos_12_meses()
        meses_nombres = self.nombres_meses(meses_info)

        # 1. [Recuadro Resumen: Venta Mensual | Ganancia Mensual | Valor Stock]
        ultimo_mes, porcentaje, color = self.dash_totalVentas()
        reporte_ventas_resumen_id = self.window.after(0, lambda: self.reporte_resumen_ventas(ultimo_mes, porcentaje, color))
        self._after_ids.append(reporte_ventas_resumen_id)

        beneficio_bruto, margen_completo, color = self.dash_totalGanancias(ultimo_mes)
        reporte_ganancias_resumen_id = self.window.after(0, lambda: self.reporte_resumen_ganancias(beneficio_bruto, margen_completo, color))
        self._after_ids.append(reporte_ganancias_resumen_id)

        valorStock_venta, num_productos = self.dash_valorStock()
        reporte_inversion_resumen_id = self.window.after(0, lambda: self.reporte_resumen_inversion(valorStock_venta, num_productos))
        self._after_ids.append(reporte_inversion_resumen_id)

        # 2. [Recuadro Grafica: Ventas Mensuales | Compras / Ventas | Top 8 Productos]
        ventas_mensuales = self.obtener_ventas_mensuales(meses_info)
        reporte_ventas_id = self.window.after(0, lambda: self.reporte_ventas(ventas_mensuales, meses_nombres))
        self._after_ids.append(reporte_ventas_id)

        compras_mensuales = self.obtener_compras_mensuales(meses_info)
        reporte_compraventas_id = self.window.after(0, lambda: self.reporte_compraventas(compras_mensuales, ventas_mensuales, meses_nombres))
        self._after_ids.append(reporte_compraventas_id)

        nombres_productos, cantidades_productos = self.obtener_top8_productos_mes()
        reporte_productos_id = self.window.after(0, lambda: self.reporte_productos(nombres_productos, cantidades_productos))
        self._after_ids.append(reporte_productos_id)

        # 3. [Recuadro Grafica: Ganancias Mensuales | Top 8 Proveedores | Tabla Stock Bajo]
        ventas, cogs, beneficio, margen = self.obtener_ganancias_mensuales(meses_info)
        reporte_ganancias_id = self.window.after(0, lambda: self.reporte_ganancias(ventas, cogs, beneficio, margen, meses_nombres))
        self._after_ids.append(reporte_ganancias_id)

        nombres_proveedores, totales = self.obtener_top8_proveedores_anio()
        reporte_proveedores_id = self.window.after(0, lambda: self.reporte_proveedores(nombres_proveedores, totales))
        self._after_ids.append(reporte_proveedores_id)

        self.reporte_stock(num_productos)

        self.mydb.close()

########################################################################################################################

    def reporte_resumen_ventas(self, ultimo_mes, porcentaje, color):

        # >>>>> [ Recuadro Resumen ] <<<<<
        self.totalmes = Label(self.frame_totalventas, text=f"$ {ultimo_mes:,.0f}", bg="#464646", fg="white", font=("Helvetica", 16, "bold"))
        self.totalmes.place(x=75, y=35)

        self.label_porcentaje = Label(self.frame_totalventas, text=porcentaje, bg="#464646", fg=color, font=("Helvetica", 9))
        self.label_porcentaje.place(x=75, y=15)

        # >>>>> [ Recuadro Grafica ] <<<<<
        totalmes_grafica = Label(self.frame_graficaVentas, text=f"$ {ultimo_mes:,.0f}", bg="#464646", fg="white", font=("Helvetica", 17, "bold"))
        totalmes_grafica.place(x=17, y=37)

        Porcentaje_grafica = Label(self.frame_graficaVentas, text=porcentaje, bg="#464646", fg=color, font=("Helvetica", 9))
        Porcentaje_grafica.place(x=17, y=70)


    def reporte_resumen_ganancias(self, beneficio_bruto, margen_completo, color):

        # >>>>> [ Recuadro Resumen ] <<<<<
        label_beneficio = Label(self.frame_totalGanancias, text=f"$ {beneficio_bruto:,.0f}", bg="#464646", fg="white", font=("Helvetica", 16, "bold"))
        label_beneficio.place(x=78, y=35)

        sub_margen = Label(self.frame_totalGanancias, text=margen_completo, bg="#464646", fg=color, font=("Helvetica", 9))
        sub_margen.place(x=78, y=15)
        
        # >>>>> [ Recuadro Grafica ] <<<<<
        saldo_ganancias = Label(self.frame_graficaGanancias, text=f"$ {beneficio_bruto:,.0f}", bg="#464646", fg="white", font=("Helvetica", 17, "bold"))
        saldo_ganancias.place(x=17, y=37)

        sub_ganancias = Label(self.frame_graficaGanancias, text=f"{margen_completo} de beneficio", bg="#464646", fg=color, font=("Helvetica", 9))
        sub_ganancias.place(x=17, y=70)
    

    def reporte_resumen_inversion(self, valorStock_venta, num_productos):

        # >>>>> [ Recuadro Resumen ] <<<<<
        valor_stock = Label(self.frame_ValorStock, text=f"$ {valorStock_venta:,.0f}", bg="#464646", fg="white", font=("Helvetica", 16, "bold"))
        valor_stock.place(x=88, y=35)

        productos_stock = Label(self.frame_ValorStock, text=f"{num_productos} Productos", bg="#464646", fg="#7fff7f" if num_productos > 0 else "#ff4f4f", font=("Helvetica", 9))
        productos_stock.place(x=88, y=15)


                    # Graficos [1. Ventas Mensuales | 2. Total Compras/Ventas | 3. Top 8 Productos]
    def reporte_ventas(self, ventas_mensuales, meses_nombres, ):

        grafica_ventas = self.grafica_ventas_mensuales(ventas_mensuales, meses_nombres)

        # >>>>> [ Gráfica Ventas Mensuales ] <<<<<
        # Embebe la gráfica ventas mensuales en Tkinter
        canvas = FigureCanvasTkAgg(grafica_ventas, master=self.frame_graficaVentas)
        canvas.draw()
        canvas.get_tk_widget().place(x=13, y=135, width=371, height=190)
        self._canvases.append(canvas)
        self._figures.append(grafica_ventas)


    def reporte_compraventas(self, compras_mensuales, ventas_mensuales, meses_nombres, ):

        grafica_intercambio = self.grafica_compraventa_mensuales(compras_mensuales, ventas_mensuales, meses_nombres)
        
        # >>>>> [ Gráfica Compra/ventas Mensuales ] <<<<<
        # Embebe la gráfica en Tkinter
        canvas2 = FigureCanvasTkAgg(grafica_intercambio, master=self.frame_graficaIntercambio)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=13, y=135, width=371, height=190)
        self._canvases.append(canvas2)
        self._figures.append(grafica_intercambio)

    def reporte_productos(self, nombres_productos, cantidades_productos, ):
        
        grafica_productos, num_productos = self.grafica_top8_productos(nombres_productos, cantidades_productos)

        # >>>>> [ Gráfica Top 8 Productos ] <<<<<
        # Embebe la gráfica en Tkinter
        canvas3 = FigureCanvasTkAgg(grafica_productos, master=self.frame_graficaTop)
        canvas3.draw()
        canvas3.get_tk_widget().place(x=10, y=127, width=377, height=195)
        self._canvases.append(canvas3)
        self._figures.append(grafica_productos)

        # >>>> Recuadro Grafica Productos <<<< 
        numero_productos = Label(self.frame_graficaTop, text=f"{num_productos} Productos", bg="#464646", fg="white", font=("Arial", 17, 'bold'))
        numero_productos.place(x=19, y=37)

        sub_productos = Label(self.frame_graficaTop, text="Por Volumen de Ventas", bg="#464646", fg="#7fff7f", font=("Helvetica", 9))
        sub_productos.place(x=19, y=70)


                # Graficos [4. Ganancias Mensuales | 5. Top 8 Proveedores | 6. Tabla Stock Bajo]
    def reporte_ganancias(self, ventas_mensuales, cogs, beneficio_bruto, margen, meses_nombres, ):

        grafica_ganancias = self.grafica_ganancias_mensuales(ventas_mensuales, cogs, beneficio_bruto, margen, meses_nombres)

        # >>>>> [ Gráfica Ganancias Mensuales ] <<<<<
        # Embebe la gráfica en Tkinter
        canvas4 = FigureCanvasTkAgg(grafica_ganancias, master=self.frame_graficaGanancias)
        canvas4.draw()
        canvas4.get_tk_widget().place(x=10, y=134, width=374, height=190)
        self._canvases.append(canvas4)
        self._figures.append(grafica_ganancias)

    def reporte_proveedores(self, nombres_proveedores, totales):

        grafica_proveedor, num_proveedores = self.grafica_top8_proveedores(nombres_proveedores, totales)

        # >>>>> [ Gráfica Top 8 Proveedores ] <<<<<
        # Embebe la gráfica en Tkinter
        canvas5 = FigureCanvasTkAgg(grafica_proveedor, master=self.frame_graficaProveedores)
        canvas5.draw()
        canvas5.get_tk_widget().place(x=13, y=135, width=363, height=190)
        self._canvases.append(canvas5)
        self._figures.append(grafica_proveedor)

        # >>>> Recuadro Grafica Proveedores <<<<
        numero_proveedores = Label(self.frame_graficaProveedores, text=f"{num_proveedores} Proveedores", bg="#464646", fg="white", font=("Arial", 17, 'bold'))
        numero_proveedores.place(x=19, y=37)

        sub_proveedores = Label(self.frame_graficaProveedores, text="Por Volumen de Compras", bg="#464646", fg="#7fff7f", font=("Helvetica", 9))
        sub_proveedores.place(x=19, y=70)


    def reporte_stock(self, num_productos, ):

        # >>>>> [ Recuadro Tabla Stock ] <<<<<
        numero_productos= Label(self.frame_tablaStock, text=f"{num_productos} Productos", bg="#464646", fg="white", font=("Arial", 17, 'bold'))
        numero_productos.place(x=18, y=37)

        sub_productos = Label(self.frame_tablaStock, text="Estado del Inventario", bg="#464646", fg="#7fff7f", font=("Helvetica", 9))
        sub_productos.place(x=18, y=70)

        self.tabla_stock_bajo()    


############################################### ///// Gráficas \\\\\ ####################################################
        

    def grafica_ventas_mensuales(self, ventas_mensuales, nombre_meses):
        
        # Crear figura matplotlib
        fig, ax = plt.subplots(figsize=(7, 2.5), dpi=100, facecolor='#464646')
        
        #ax.set_title("Ventas mensuales")
        ax.set_facecolor('#464646')
        #ax.set_ylabel("Total $")
        #ax.set_xlabel("Mes")
        ax.grid(True, axis='y', alpha=0.7)
        ax.tick_params(labelsize=7, colors='white')
        fig.autofmt_xdate()
        ax.plot(nombre_meses, ventas_mensuales, color='#73fbfd', marker='o')

        return fig

    def grafica_compraventa_mensuales(self, compras_mensuales, ventas_mensuales, nombre_meses):

        # Crear figura matplotlib
        fig2, ax2 = plt.subplots(figsize=(7, 2.5), dpi=100, facecolor='#464646')
        ax2.set_facecolor('#464646')
        ax2.grid(True, axis='y', alpha=0.7)
        ax2.tick_params(labelsize=7, colors='white')
        fig2.autofmt_xdate()

        # Posiciones para barras agrupadas
        x = np.arange(len(nombre_meses))
        width = 0.35

        # Barras de ventas y compras
        bars1 = ax2.bar(x - width/2, ventas_mensuales, width, color='#73fbfd')
        bars2 = ax2.bar(x + width/2, compras_mensuales, width, color='#f29d38')

        ax2.set_xticks(x)
        ax2.set_xticklabels(nombre_meses)

        return fig2
        
    def grafica_top8_productos(self, nombres_productos, cantidades_productos):
        
        # Filtrar productos con cantidad > 0
        self.nombres_filtrados = [n for n, c in zip(nombres_productos, cantidades_productos) if c > 0]
        cantidades_filtradas = [c for c in cantidades_productos if c > 0]

        if sum(cantidades_filtradas) == 0:
            # No hay datos, muestra un gráfico vacío o mensaje
            fig3, ax3 = plt.subplots(figsize=(4, 2.5), dpi=100, facecolor='#464646')
            ax3.set_facecolor('#464646')
            ax3.text(0.5, 0.5, "Sin datos\nde ventas", color="white", fontsize=14, ha='center', va='center')
            ax3.axis('off')
        else:
            fig3, ax3 = plt.subplots(figsize=(4, 2.5), dpi=100, facecolor='#464646')
            ax3.set_facecolor('#464646')
            fig3.subplots_adjust(left=0.05, right=0.45)  # Puedes ajustar estos valores

            wedges, _, autotexts = ax3.pie(
                cantidades_filtradas,
                labels=None,
                autopct=lambda pct: f"{int(round(pct/100*sum(cantidades_filtradas)))}",
                startangle=90,
                pctdistance=0.85,
                textprops={'color':"white", 'fontsize':8},
                wedgeprops=dict(width=0.4, edgecolor='#464646')
            )
            centre_circle = plt.Circle((0,0),0.60,fc='#464646')
            fig3.gca().add_artist(centre_circle)
            ax3.axis('equal')
            ax3.legend(wedges, self.nombres_filtrados, loc="center left", bbox_to_anchor=(1.25, 0.5), frameon=False, fontsize=8, labelcolor="#fafafa", labelspacing=0.7)

        return fig3, len(self.nombres_filtrados)


    def grafica_ganancias_mensuales(self, ventas, cogs, beneficio, margen, nombre_meses):

        # Crear figura matplotlib
        fig4, ax4 = plt.subplots(figsize=(7, 2.5), dpi=100, facecolor='#464646')
        ax4.set_facecolor('#464646')
        ax4.grid(True, axis='y', alpha=0.7)
        ax4.tick_params(labelsize=7, colors='white')
        fig4.autofmt_xdate()

        x = np.arange(len(nombre_meses))
        width = 0.25

        # Barras
        ax4.bar(x - width, ventas, width, label='Ingresos', color="#73fbfd")
        ax4.bar(x, cogs, width, label='COGS', color="#f29d38")
        ax4.bar(x + width, beneficio, width, label='Beneficio Bruto', color="#c17eff")

        # Línea de margen de beneficio
        ax5 = ax4.twinx()
        ax5.plot(x, margen, color="#7cff6b", marker='o', label='Profit Margin %')
        #ax5.set_ylabel('Profit Margin %', color='#ff4f4f')
        ax5.tick_params(axis='y', labelcolor='white', labelsize=7)

        # --- Añade esto para mostrar el eje derecho en porcentaje ---
        ax5.set_ylabel('Profit Margin %', color='white', fontsize=9)
        ax5.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0f}%'.format(y)))

        # Ejes y leyendas
        ax4.set_xticks(x)
        ax4.set_xticklabels(nombre_meses)
        #ax4.legend(loc='upper left', fontsize=8)
        #ax5.legend(loc='upper right', fontsize=8)

        return fig4

    def grafica_top8_proveedores(self, nombres_proveedores, totales):

        # Filtrar proveedores con total > 0
        if sum(totales) == 0:
            # No hay datos, muestra un gráfico vacío o mensaje
            fig5, ax5 = plt.subplots(figsize=(4, 2.5), dpi=100, facecolor='#464646')
            ax5.set_facecolor('#464646')
            ax5.text(0.5, 0.5, "Sin datos\nde compras", color="white", fontsize=14, ha='center', va='center')
            ax5.axis('off')
        else:
            fig5, ax5 = plt.subplots(figsize=(4, 2.5), dpi=100, facecolor='#464646')
            ax5.set_facecolor('#464646')
            fig5.subplots_adjust(left=0.05, right=0.45)  # Puedes ajustar estos valores
            wedges, texts, autotexts = ax5.pie(
                totales,
                labels=None,
                autopct=lambda pct: f"${int(round(pct/100*sum(totales)))}",
                startangle=90,
                pctdistance=0.85,
                textprops={'color':"white", 'fontsize':8},
                wedgeprops=dict(width=0.4, edgecolor='#464646')
            )
            centre_circle = plt.Circle((0,0),0.60,fc='#464646')
            fig5.gca().add_artist(centre_circle)
            ax5.axis('equal')
            ax5.legend(wedges, nombres_proveedores, loc="center left", bbox_to_anchor=(1.25, 0.5), frameon=False, fontsize=8, labelcolor="#fafafa", labelspacing=0.7)

        return fig5, len(nombres_proveedores)


    def tabla_stock_bajo(self):

        tabla = ttk.Treeview(self.frame_tablaStock, columns=("Stock", "Código", "Producto"), show='tree headings')

        tabla.heading("#0", text="Estado")  # Columna de árbol, aquí va la imagen
        tabla.heading("Stock", text="Stock")
        tabla.heading("Código", text="Código")
        tabla.heading("Producto", text="Producto")

        tabla.column("#0", width=30, anchor=W)
        tabla.column("Stock", width=3, anchor=CENTER)
        tabla.column("Código", width=10, anchor=CENTER)
        tabla.column("Producto", width=70, anchor=CENTER)

        query = "SELECT Nombre, Código_Básico, Cantidad FROM producto ORDER BY Cantidad ASC"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()

        for row in resultados:
            nombre, codigo, stock = row
            if stock <= 5:
                
                img = self.est_critico
            elif stock <= 15:
                
                img = self.est_bajo
            elif stock <= 25:
                
                img = self.est_medio
            else:
               
                img = self.est_bueno
            tabla.insert("", "end", image=img, text="", values=(stock, codigo, nombre))


        # Configure Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#343434", fieldbackground="#343434", foreground="white", rowheight=35, font=("Inter", 9))
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])

        tabla.place(x=20, y=102, width=356, height=212)


########################################## ///// Datos Para Labels Corre en Segundo Plano \\\\\ ###############################################        


    # >>>>>>>>  Recuadro Total Ventas Mensuales  <<<<<<<
    def dash_totalVentas(self, ): 

        query = "SELECT SUM(Precio * Cantidad) FROM venta WHERE strftime('%Y-%m', Fecha) = strftime('%Y-%m', 'now')"
        self.cursor.execute(query)
        ventasMensuales = self.cursor.fetchone()[0] or 0
        
        # Diferencia porcentual con el mes anterior
        query_anterior = "SELECT SUM(Precio * Cantidad) FROM venta WHERE strftime('%Y-%m', Fecha) = strftime('%Y-%m', 'now', '-1 month')"
        self.cursor.execute(query_anterior)
        ventasMesAnterior = self.cursor.fetchone()[0] or 0
        
        # calcular diferencia siempre (evita UnboundLocalError)
        diferencia = ventasMensuales - ventasMesAnterior
        if ventasMesAnterior:
            diferencia_porcentual = (diferencia / ventasMesAnterior) * 100
        else:
            diferencia_porcentual = 0

        if diferencia_porcentual > 0:
            signo = "+"
            color = "#7fff7f"  # Verde para aumento
        else:
            signo = ""
            color = "#ff4f4f"  # Rojo para disminución o sin cambio
        
        porcentaje = f"{signo}{diferencia_porcentual:.2f}% ${diferencia} Este Mes"

        return ventasMensuales, porcentaje, color


    def dash_totalGanancias(self, ventasMensuales):

        # Encuentra el último mes con ventas
        self.cursor.execute("""
            SELECT strftime('%Y-%m', Fecha) 
            FROM venta 
            WHERE Fecha IS NOT NULL
            ORDER BY Fecha DESC LIMIT 1
        """)
        ultimo_mes = self.cursor.fetchone()
        if ultimo_mes and ultimo_mes[0]:
            mes_consulta = ultimo_mes[0]
        else:
            mes_consulta = datetime.date.today().strftime('%Y-%m')

        # Ahora usa ese mes en tu consulta de beneficio
        query_beneficio = f"""
            SELECT 
                (SELECT Precio FROM venta WHERE strftime('%Y-%m', Fecha) = '{mes_consulta}') -
                (SELECT Precio FROM compra WHERE strftime('%Y-%m', Fecha) = '{mes_consulta}')
        """
        self.cursor.execute(query_beneficio)
        row = self.cursor.fetchone()
        beneficio_bruto = row[0] if row and row[0] is not None else 0

        # Margen de ganancia Porcentual
        margen = (beneficio_bruto / ventasMensuales * 100) if ventasMensuales > 0 else 0
        signo = "+" if margen > 0 else ""
        
        margen_completo = f"{signo}{margen:.2f}% Margen"
        color = "#7fff7f" if margen > 0 else "#ff4f4f"

        return beneficio_bruto, margen_completo, color


    # >>>>>>>>>>>>>>>>>> Recuadro Valor Stock <<<<<<<<<<<<<<<<<<<<<<<
    def dash_valorStock(self, ):

        query_stock = "SELECT SUM(Precio * Cantidad) FROM producto"
        valorStock_venta = self.cursor.execute(query_stock).fetchone()[0] or 0

        # Cantidad de productos distintos
        query_productos = "SELECT COUNT(*) FROM producto WHERE Cantidad > 0"
        num_productos = self.cursor.execute(query_productos).fetchone()[0] or 0
        if num_productos > 0:
            num_productos = num_productos + 1

        return valorStock_venta, num_productos


########################################//////// Datos Para Graficos Que Corren en Segundo Plano \\\\\\\\##############################################

    def obtener_top8_proveedores_anio(self):
        # Obtiene el año más reciente con datos
        self.cursor.execute("SELECT MAX(strftime('%Y', Fecha)) FROM compra WHERE Fecha IS NOT NULL")
        ultimo_anio = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT Fecha FROM compra WHERE strftime('%Y', Fecha) = ?", (ultimo_anio,))

        if not ultimo_anio:
            return [], []
        self.cursor.execute("""
            SELECT p.Razon_Social, SUM(c.Precio) as total_compras
            FROM compra c
            JOIN proveedor p ON c.proveedor_Rut = p.Rut
            WHERE strftime('%Y', c.Fecha) = ?
            GROUP BY p.Razon_Social
            ORDER BY total_compras DESC
            LIMIT 8
        """, (ultimo_anio,))
        datos = self.cursor.fetchall()

        nombres = [row[0] for row in datos]
        totales = [row[1] for row in datos]

        return nombres, totales


    def obtener_ganancias_mensuales(self, meses):
        # Ingresos (ventas)
        ventas = []
        for anio, mes in meses:
            self.cursor.execute("""
                SELECT Precio
                FROM venta
                WHERE strftime('%Y', Fecha) = ? AND strftime('%m', Fecha) = ?
            """, (str(anio), f"{mes:02d}"))
            row = self.cursor.fetchone()
            total = row[0] if row and row[0] is not None else 0
            try:
                total = float(total)
            except (ValueError, TypeError):
                total = 0.0
            ventas.append(total)
        
        # COGS (compras)
        cogs = []
        for anio, mes in meses:
            self.cursor.execute("""
                SELECT Precio
                FROM compra
                WHERE strftime('%Y', Fecha) = ? AND strftime('%m', Fecha) = ?
            """, (str(anio), f"{mes:02d}"))
            row = self.cursor.fetchone()
            total = row[0] if row and row[0] is not None else 0
            try:
                total = float(total)
            except (ValueError, TypeError):
                total = 0.0
            cogs.append(total)

        # Beneficio bruto y margen
        beneficio = [v - c for v, c in zip(ventas, cogs)]
        margen = [(b / v * 100) if v > 0 else 0 for b, v in zip(beneficio, ventas)]

        return ventas, cogs, beneficio, margen


    def obtener_top8_productos_mes(self):
        
        self.cursor.execute("""
            SELECT p.Nombre, SUM(v.Cantidad) as total_vendida
            FROM venta v
            JOIN producto p ON v.Producto_Código_Barra = p.Código_Barra
            WHERE strftime('%Y', v.Fecha) = strftime('%Y', 'now')
            GROUP BY p.Nombre
            ORDER BY total_vendida DESC
            LIMIT 8
        """)
        datos = self.cursor.fetchall()

        nombres = [row[0] for row in datos]
        cantidades = [row[1] for row in datos]

        return nombres, cantidades


    def obtener_ultimos_12_meses(self):
        hoy = datetime.date.today()
        meses = []
        anio = hoy.year
        mes = hoy.month
        for _ in range(12):
            meses.append((anio, mes))
            mes -= 1
            if mes == 0:
                mes = 12
                anio -= 1
        meses.reverse()  # Para que estén en orden cronológico

        return meses

    def nombres_meses(self, meses):

        return [calendar.month_abbr[m[1]] for m in meses]


    def obtener_compras_mensuales(self, meses):
    
        compras = []
        for anio, mes in meses:
            self.cursor.execute("""
                SELECT Precio
                FROM compra
                WHERE strftime('%Y', Fecha) = ? AND strftime('%m', Fecha) = ?
            """, (str(anio), f"{mes:02d}"))
            row = self.cursor.fetchone()
            total = row[0] if row and row[0] is not None else 0
            try:
                total = float(total)
            except (ValueError, TypeError):
                total = 0.0
            compras.append(total)

        return compras


    def obtener_ventas_mensuales(self, meses):

        ventas = []
        for anio, mes in meses:
            self.cursor.execute("""
                SELECT Precio
                FROM venta
                WHERE strftime('%Y', Fecha) = ? AND strftime('%m', Fecha) = ?
            """, (str(anio), f"{mes:02d}"))
            row = self.cursor.fetchone()
            total = row[0] if row and row[0] is not None else 0
            try:
                total = float(total)
            except (ValueError, TypeError):
                total = 0.0
            ventas.append(total)

        return ventas


######################################### ///// Limpieza Segura De Figures, Canvases (MatplotLib) \\\\\ ##########################################
    def cancel_after_events(self):
        print(self._after_ids)
        """Cancelar afters, destruir canvases y cerrar figuras para evitar callbacks residuales."""
        # cancelar afters que registramos explícitamente
        try:
            for after_id in list(getattr(self, "_after_ids", [])):
                try:
                    self.window.after_cancel(after_id)
                except Exception:
                    pass
        except Exception:
            pass
        self._after_ids = []

        # cancelar todos los after programados en la ventana (incluye callbacks internos)
        try:
            for aid in list(self.window.after_info() or []):
                try:
                    self.window.after_cancel(aid)
                except Exception:
                    pass
        except Exception:
            pass

        # destruir nuestros canvases y figuras matplotlib
        try:
            for c in list(getattr(self, "_canvases", [])):
                try:
                    # desconectar handlers si existen
                    try:
                        c.mpl_disconnect()
                    except Exception:
                        pass
                    try:
                        w = c.get_tk_widget()
                        w.destroy()
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        self._canvases = []

        try:
            import matplotlib.pyplot as _plt
            _plt.close('all')
        except Exception:
            pass
        self._figures = []

        # eso puede romper otras partes de la app; en su lugar forzamos limpieza ligera:
        try:
            self.window.update_idletasks()
        except Exception:
            pass

        self.scrollable_frame.destroy()

    
    def _safe_close_and_open(self, opener):
        """Cancela timers y destruye la ventana de forma segura, luego abre 'opener'."""
        try:
            self.cancel_after_events()
        except Exception:
            pass

        # esperar un poco para que Tcl libere callbacks internos, destruir en mainloop
        def _do():
            try:
                import time
                # cierre final de figuras/canvases una vez más
                try:
                    import matplotlib.pyplot as _plt
                    _plt.close('all')
                except Exception:
                    pass
                time.sleep(0.02)
            except Exception:
                pass

            try:
                self.window.destroy()
            except Exception:
                pass

            # abrir la nueva ventana después de destruir
            try:
                opener()
            except Exception:
                pass

        try:
            self.window.after(80, _do)
        except Exception:
            # fallback sin after
            _do()