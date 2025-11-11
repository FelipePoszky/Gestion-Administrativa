from tkinter import *
from tkinter import messagebox
import util.generic as utl
from forms.form_inventario import inventario
from forms.form_ventas import ventas
from forms.form_compras import compras
from forms.form_datosLocal import DatosLocal
from forms.form_reportes import reportes
from forms.form_cuenta import cuenta
import os


class MasterPanel:

    def contactanos(self):
    
        messagebox.showinfo("Contáctanos", "datos reales quitados de este repositorio")

    def __init__(self):

        img_dir = os.getcwd()

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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/background.png")
        background = canvas.create_image(
        630, 312.5,
        image=background_img)

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/img0.png")
        b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.contactanos,
        cursor = "hand2",
        relief = "flat")

        b0.place(
        x = 978, y = 402,
        width = 181,
        height = 59)

        img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/img1.png")
        b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.llamaDatosLocal,
        cursor = "hand2",
        relief = "flat")

        b1.place(
        x = 978, y = 283,
        width = 181,
        height = 58)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/img2.png")
        b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.llamaPuntoVent,
        cursor = "hand2",
        relief = "flat")

        b2.place(
        x = 254, y = 15,
        width = 114,
        height = 42)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/img3.png")
        b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.llamaInv,
        cursor = "hand2",
        relief = "flat")

        b3.place(
        x = 389, y = 15,
        width = 147,
        height = 42)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/img4.png")
        b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.llamaReportes,
        cursor = "hand2",
        relief = "flat")

        b4.place(
        x = 721, y = 15,
        width = 143,
        height = 42)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/img5.png")
        b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.llamaCompras,
        cursor = "hand2",
        relief = "flat")

        b5.place(
        x = 557, y = 15,
        width = 143,
        height = 42)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/M. Inicio/img6.png")
        b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.llamaCuenta,
        cursor = "hand2",
        relief = "flat")

        b6.place(
        x = 1186, y = 7,
        width = 53,
        height = 57)

        self.window.resizable(False, False)
        self.window.mainloop()

#---------------------------->>> [FUNCIONES DE LLAMADO A OTRAS VENTANAS] >>>-------------------------------------------------

    
    def llamaInv(self):
        
        self.window.destroy()
        inventario()

    def llamaCompras(self):

        self.window.destroy()
        compras()

    def llamaPuntoVent(self):

        self.window.destroy()
        ventas()

    def llamaDatosLocal(self):

        self.window.destroy()
        DatosLocal()
    
    def llamaReportes(self):
        
        self.window.destroy()
        reportes()  

    def llamaCuenta(self):

        self.window.destroy()
        cuenta()