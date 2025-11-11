from tkinter import *
from tkinter import messagebox, filedialog

import os
import util.generic as utl
import sqlite3


class DatosLocal:

    def volverInicio(self):

        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()

    def abrirDatosProveedores(self):

        from forms.form_datosProveedores import DatosProveedores
        self.window.destroy()
        DatosProveedores()

    def abrirDatosUsuarios(self):

        from forms.form_datosUsuarios import DatosUsuarios
        self.window.destroy()
        DatosUsuarios()

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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/background.png")
        background = canvas.create_image(
            630, 312.5,
            image=background_img)

        #--------------------------------------->>> [Botones] >>>-------------------------------------------------

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img0.png")
        self.b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.guardar_datos,
            cursor = "hand2",
            relief = "flat")


        img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.cambiar_logo,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 927, y = 547,
            width = 290,
            height = 41)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img2.png")
        self.b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.editar_datos,
            cursor = "hand2",
            relief = "flat")

        self.b2.place(
            x = 203, y = 547,
            width = 594,
            height = 41)
        
        # <<< Botones navegacion >>>
        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrirDatosProveedores,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 251, y = 13,
            width = 165,
            height = 46)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrirDatosUsuarios,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 434, y = 13,
            width = 149,
            height = 46)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.volverInicio,
            cursor = "hand2",
            relief = "flat")

        b5.place(
            x = 1191, y = 5,
            width = 59,
            height = 58)

        #--------------------------------------->>> [Datos de Entradas] >>>-------------------------------------------------

        self.razon_social = StringVar()
        self.giro = StringVar()
        self.direccion = StringVar()
        self.rut = StringVar()
        self.bol_in = StringVar()
        self.bol_fin = StringVar()
        self.ultima_bol = StringVar()

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        db_path = os.path.join(project_root, "BD_Veguita")
        
        self.mydb = sqlite3.connect(db_path)
        self.cursor = self.mydb.cursor()

        self.cursor.execute("SELECT Razon_Social, Giro, Direccion, Rut, Boleta_Inicio, Boleta_Fin, Ultima_Boleta_Realizada FROM veguita")
        row = self.cursor.fetchone()

        if row:
            self.razon_social.set(row[0])
            self.rs_actual = row[0]
            self.giro.set(row[1])
            self.gir_actual = row[1]
            self.direccion.set(row[2])
            self.dir_actual = row[2]
            self.rut.set(row[3])
            self.rut_actual = row[3]
            self.bol_in.set(row[4])
            self.bol_in_actual = row[4]
            self.bol_fin.set(row[5])
            self.bol_fin_actual = row[5]
            self.ultima_bol.set(row[6])
            self.ultima_bol_actual = row[6]

        #--------------------------------------->>> [Entradas] >>>-------------------------------------------------

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img_textBox6.png")
        entry0_bg = canvas.create_image(
            500, 141,
            image = entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.razon_social,
            state = "readonly",
            highlightthickness = 0)

        self.entry0.place(
            x = 215, y = 127,
            width = 565.0,
            height = 28)

        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img_textBox5.png")
        entry1_bg = canvas.create_image(
            500, 190,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.giro,
            state = "readonly",
            highlightthickness = 0)

        self.entry1.place(
            x = 215, y = 176,
            width = 565.0,
            height = 28)

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img_textBox4.png")
        entry2_bg = canvas.create_image(
            500, 239,
            image = entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.direccion,
            state = "readonly",
            highlightthickness = 0)

        self.entry2.place(
            x = 215, y = 225,
            width = 565.0,
            height = 28)


        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img_textBox3.png")
        entry3_bg = canvas.create_image(
            500, 288,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.rut,
            state = "readonly",
            highlightthickness = 0)

        self.entry3.place(
            x = 215, y = 274,
            width = 565.0,
            height = 28)


        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img_textBox2.png")
        entry4_bg = canvas.create_image(
            500, 417,
            image = entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.bol_in,
            state = "readonly",
            highlightthickness = 0)

        self.entry4.place(
            x = 215, y = 403,
            width = 565.0,
            height = 28)
        

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img_textBox1.png")
        entry5_bg = canvas.create_image(
            500, 466,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.bol_fin,
            state = "readonly",
            highlightthickness = 0)

        self.entry5.place(
            x = 215, y = 452,
            width = 565.0,
            height = 28)

        entry6_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Datos/img_textBox0.png")
        entry6_bg = canvas.create_image(
            500, 515,
            image = entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            textvariable = self.ultima_bol,
            state = "readonly",
            highlightthickness = 0)

        self.entry6.place(
            x = 215, y = 501,
            width = 565.0,
            height = 28)

        # --------------------------------------[Logo]-------------------------------------------
        logoImg = PhotoImage(file=f"{img_dir}/Imagenes/M. Datos/Logo.png")
        self.logo = canvas.create_image(
            1070, 331,
            image=logoImg)
        
        #self.logo = Label(self.window, image=logoImg)
        #self.logo.place(x=962, y=142, width=221, height=372)


        self.window.resizable(False, False)
        self.window.mainloop()


    def cambiar_logo(self):

        nuevo_logo = filedialog.askopenfilename(title="Seleccionar nuevo logo", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
        if nuevo_logo:
            self.logo = PhotoImage(file=nuevo_logo)
            self.canvas.itemconfig(self.logo_bg, image=self.logo)
            self.canvas.image = self.logo  # Mantener una referencia de la imagen


    def editar_datos(self):

        self.b0.place(
            x = 203, y = 547,
            width = 594,
            height = 41)
    
        self.b2.place_forget()
        
        self.entry0.configure(state="normal")
        self.entry1.configure(state="normal")
        self.entry2.configure(state="normal")
        self.entry3.configure(state="normal")
        self.entry4.configure(state="normal")
        self.entry5.configure(state="normal")
        self.entry6.configure(state="normal")

    def guardar_datos(self):

        if self.razon_social.get() == self.rs_actual and self.giro.get() == self.gir_actual and self.direccion.get() == self.dir_actual and self.rut.get() == self.rut_actual and self.bol_in.get() == self.bol_in_actual and self.bol_fin.get() == self.bol_fin_actual and self.ultima_bol.get() == self.ultima_bol_actual:
            messagebox.showwarning("Advertencia", "No se realizaron cambios en los datos.")
            return
        
        else:
            if self.cursor.rowcount > 0:
                respuesta = messagebox.askyesno("Confirmar Cambios", "¿Estás seguro de que deseas confirmar los cambios?", parent=self.window)
                if respuesta:
                    query = ("UPDATE veguita SET Razon_Social = ?, Giro = ?, Direccion = ?, Rut = ?, Boleta_Inicio = ?, Boleta_Fin = ?, Ultima_Boleta_Realizada = ?")
                    self.cursor.execute(query, (self.razon_social.get(), self.giro.get(), self.direccion.get(), self.rut.get(), self.bol_in.get(), self.bol_fin.get(), self.ultima_bol.get()))

                    #lógica para procesar los datos actualizados
                    self.mydb.commit()
                    messagebox.showinfo("Éxito", "Los datos han sido Modificados correctamente.")
                    self.b2.place(
                        x = 203, y = 547,
                        width = 594,
                        height = 41)
                    self.b0.place_forget()
            else:
                messagebox.showwarning("Advertencia", "No se realizaron cambios en los datos.")