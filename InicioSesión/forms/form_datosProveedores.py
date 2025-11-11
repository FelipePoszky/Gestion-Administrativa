from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD

import os
import util.generic as utl
import sqlite3


class DatosProveedores:

    def volverInicio(self):
        
        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()

    def abrirDatosLocal(self):

        from forms.form_datosLocal import DatosLocal
        self.window.destroy()
        DatosLocal()

    def abrirDatosUsuarios(self):

        from forms.form_datosUsuarios import DatosUsuarios
        self.window.destroy()
        DatosUsuarios()

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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/background.png")
        background = canvas.create_image(
            630, 312.5,
            image=background_img)

        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.volverInicio,
            cursor = "hand2",
            relief = "flat")

        b0.place(
            x = 1190, y = 8,
            width = 61,
            height = 56)

        img1 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.editar_proveedor,
            cursor = "hand2",
            relief = "flat")

        b1.place(
            x = 850, y = 536,
            width = 202,
            height = 47)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.eliminar_proveedor,
            cursor = "hand2",
            relief = "flat")

        b2.place(
            x = 1084, y = 536,
            width = 138,
            height = 47)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.agregar_proveedor,
            cursor = "hand2",
            relief = "flat")

        b3.place(
            x = 688, y = 536,
            width = 129,
            height = 47)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.filtrar_proveedores,
            cursor = "hand2",
            relief = "flat")

        b4.place(
            x = 1025, y = 125,
            width = 112,
            height = 48)

        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.limpiar_campos,
            cursor = "hand2",
            relief = "flat")

        b5.place(
            x = 1142, y = 125,
            width = 100,
            height = 48)

        img6 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img6.png")
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrirDatosLocal,
            cursor = "hand2",
            relief = "flat")

        b6.place(
            x = 120, y = 14,
            width = 118,
            height = 44)

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img7.png")
        b7 = Button(
            image = img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.abrirDatosUsuarios,
            cursor = "hand2",
            relief = "flat")

        b7.place(
            x = 440, y = 14,
            width = 151,
            height = 44)
        
        #----------------------------------------------------------------------------------------------------

        self.proveedor = ttk.Treeview(self.window, columns=(1,2,3,4,5), show="headings", height=4)
        
        self.proveedor.heading(1, text="Rut")
        self.proveedor.heading(2, text="R. Social")
        self.proveedor.heading(3, text="Contacto")
        self.proveedor.heading(4, text="Teléfono")
        self.proveedor.heading(5, text="Dirección")

        self.proveedor.column(1, width=50, anchor=CENTER)
        self.proveedor.column(2, width=80, anchor=W)
        self.proveedor.column(3, width=80, anchor=W)
        self.proveedor.column(4, width=50, anchor=CENTER)
        self.proveedor.column(5, width=80, anchor=W)

        query = "SELECT Rut, Razon_Social, Contacto, Num_Contacto, Direccion FROM proveedor"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for row in rows:
            self.proveedor.insert("", "end", values=row)
        
        # Configuración Treeview style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#464646", fieldbackground="#464646", foreground="white", rowheight=27)
        style.configure("Treeview.Heading", background="#262626", fieldbackground="#262626", foreground="white", font=("Inter", 10, BOLD), padding=8)
        style.map("Treeview", background=[('selected', '#101010')])
        style.map("Treeview.Heading", background=[('active', '#101010')])


        self.proveedor.place(x=17, y=102, width=580, height=501)
        #------------------------------------------------------------------------------------------------------------------------------
            #  --> Buscador
        
        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img_textBox1.png")
        entry1_bg = canvas.create_image(
            901, 147,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry1.place(
            x = 790, y = 135,
            width = 213.0,
            height = 25)
        
    # -------------> Campos de Texto para Datos de Proveedor ----------------#

        entry0_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img_textBox0.png")
        entry0_bg = canvas.create_image(
            993, 296,
            image = entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry0.place(
            x = 865, y = 284,
            width = 248.0,
            height = 25)

        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img_textBox4.png")
        entry4_bg = canvas.create_image(
            993, 339,
            image = entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry4.place(
            x = 865, y = 327,
            width = 248.0,
            height = 25)

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img_textBox2.png")
        entry2_bg = canvas.create_image(
            993, 382,
            image = entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry2.place(
            x = 865, y = 370,
            width = 248.0,
            height = 25)

        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img_textBox3.png")
        entry3_bg = canvas.create_image(
            993, 425,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry3.place(
            x = 865, y = 413,
            width = 248.0,
            height = 25)

        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Proveedores/img_textBox4.png")
        entry5_bg = canvas.create_image(
            993, 468,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

        self.entry5.place(
            x = 865, y = 456,
            width = 248.0,
            height = 25)

        self.window.resizable(False, False)
        self.window.mainloop()

    # Limpia los campos de texto
    def limpiar_campos(self):

        self.entry0.delete(0, END)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

    # Edita los datos del proveedor seleccionado
    def editar_proveedor(self):

        if not self.entry0.get() and not self.entry4.get():
            messagebox.showerror("Error", "Por favor, complete al menos los campos obligatorios: Rut y Razón Social.")
            return

        if self.rut_selec == self.entry0.get() and self.razon_selec == self.entry4.get() and self.tel_selec == self.entry3.get() and self.contac_selec == self.entry2.get() and self.dir_selec == self.entry5.get():
            # Si todos los campos son iguales, no se necesita actualizar
            return

        # Si llegamos aquí, significa que hay cambios que realizar
        respuesta = messagebox.askyesno("Confirmar", "¿Desea guardar los cambios?")
        if respuesta:

            query = "UPDATE proveedor SET Razon_Social = ?, Num_Contacto = ?, Contacto = ?, Direccion = ? WHERE Rut = ?"
            self.cursor.execute(query, (self.entry4.get(), self.entry3.get(), self.entry2.get(), self.entry5.get(), self.entry0.get()))
            self.mydb.commit()

            self.actualizar_tabla()

    def filtrar_proveedores(self):

        if not self.entry1.get():
            selected = self.proveedor.selection()
            if selected:
                item = selected[0]
                valores = self.proveedor.item(item, "values")
                self.entry0.delete(0, END)
                self.entry0.insert(0, valores[0])  # Rut
                self.rut_selec = valores[0]
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[1])  # Razon_Social
                self.razon_selec = valores[1]
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[2])  # Nombre_Contacto
                self.contac_selec = valores[2]
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[3])  # Telefono
                self.tel_selec = valores[3]
                self.entry5.delete(0, END)
                self.entry5.insert(0, valores[4])  # Direccion
                self.dir_selec = valores[4]

            return

        # Si el entry no está vacío, buscar en la tabla
        for item in self.proveedor.get_children():

            valores = self.proveedor.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry1.get() or valores[1] == self.entry1.get() or valores[2] == self.entry1.get():  # Comparar con la columna "Rut" (índice 0)

                self.entry0.delete(0, END)
                self.entry0.insert(0, valores[0])  # Rut
                self.rut_selec = valores[0]
                self.entry4.delete(0, END)
                self.entry4.insert(0, valores[1])  # Razon_Social
                self.razon_selec = valores[1]
                self.entry2.delete(0, END)
                self.entry2.insert(0, valores[2])  # Nombre_Contacto
                self.contac_selec = valores[2]
                self.entry3.delete(0, END)
                self.entry3.insert(0, valores[3])  # Telefono
                self.tel_selec = valores[3]
                self.entry5.delete(0, END)
                self.entry5.insert(0, valores[4])  # Direccion
                self.dir_selec = valores[4]

    # Agrega un Nuevo Proveedor a la Base de Datos
    def agregar_proveedor(self):

        if not self.entry0.get() or not self.entry4.get():
            messagebox.showerror("Error", "Por favor, complete al menos los campos obligatorios: Rut y Razón Social.")
            return

        rut = self.entry0.get()
        nombre_contacto = self.entry2.get()
        telefono = self.entry3.get()
        razon_social = self.entry4.get()
        direccion = self.entry5.get()

        query = f"INSERT INTO proveedor (Rut, Contacto, Num_Contacto, Razon_Social, Direccion) VALUES ('{rut}', '{nombre_contacto}', '{telefono}', '{razon_social}', '{direccion}')"
        self.cursor.execute(query)

        if self.cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Proveedor agregado exitosamente.")
            self.mydb.commit()
        else:
            messagebox.showerror("Error", "No se pudo agregar el proveedor.")

        self.actualizar_tabla()

    # Elimina el Proveedor seleccionado
    def eliminar_proveedor(self):

        for item in self.proveedor.get_children():

            valores = self.proveedor.item(item, "values")  # Obtener los valores de la fila
            if valores[0] == self.entry0.get():  # Comparar con la columna "Rut" (índice 0)
                
                respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este proveedor?")
                if respuesta:
                    query = "DELETE FROM proveedor WHERE Rut = ?"
                    self.cursor.execute(query, (self.entry0.get(),))
                    self.mydb.commit()
                    self.actualizar_tabla()
                    messagebox.showinfo("Éxito", f"Proveedor '{self.entry0.get()}' eliminado correctamente.", parent=self.window)
                return
        
    # Actualiza la tabla de proveedores
    def actualizar_tabla(self):

        query = "SELECT Rut, Razon_Social, Contacto, Num_Contacto, Direccion FROM proveedor"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        self.proveedor.delete(*self.proveedor.get_children())
        for row in rows:
            self.proveedor.insert("", "end", values=row)