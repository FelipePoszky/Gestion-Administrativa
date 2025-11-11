from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter import filedialog

import util.generic as utl
import util.variables as variables
import sqlite3
import os
import shutil
import datetime

class cuenta:

    def cerrar_sesion(self):
        respuesta = messagebox.askyesno("Cerrar Sesión", "¿Estás seguro de que deseas cerrar sesión?")
        if respuesta:
            from forms.form_login import app
            self.cursor.execute("UPDATE usuario SET Ultima_Conexión = ? WHERE Rut = ?", (datetime.datetime.now(), self.user))
            self.mydb.commit()
            self.window.destroy()
            app()
    
    def volverInicio(self):
        from forms.form_master import MasterPanel
        self.window.destroy()
        MasterPanel()

    def __init__(self):

        img_dir = os.getcwd()
        self.user = variables.logged_user

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

        background_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/background.png")
        background = canvas.create_image(
        630, 312.5,
        image=background_img)


        self.cursor.execute("SELECT Imagen FROM usuario WHERE Rut = ?", (self.user,))
        img_nombre = self.cursor.fetchone()
        if img_nombre and img_nombre[0]:
            img_path = os.path.join(img_dir, "Imagenes", "Perfiles", img_nombre[0])
            if os.path.exists(img_path):
                profile_img = utl.make_circle_image(img_path)
            else:
                profile_img = utl.make_circle_image(f"{img_dir}/Imagenes/M. Cuenta/Profile.png")  # Imagen por defecto
        else:
            profile_img = utl.make_circle_image(f"{img_dir}/Imagenes/M. Cuenta/Profile.png")

       
        foto_perfil = canvas.create_image(72.5, 184.5, image=profile_img, anchor="nw")
        canvas.image = profile_img 
        
        self.canvas = canvas
        self.foto_perfil_id = foto_perfil
        self.profile_img = profile_img  # Guarda la referencia para evitar que el GC la elimine

        # ------------------------------>>>>>>>>>> BOTONES >>>>>>>--------------------------------------->>>>>>>
        img0 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Button.png")
        b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.cambiarImagen,
        cursor = "hand2",
        relief = "flat")

        b0.place(
        x = 88, y = 556,
        width = 225,
        height = 52)

        img2 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Button (1).png")
        b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.cerrar_sesion,
        cursor = "hand2",
        relief = "flat")

        b2.place(
        x = 1060, y = 560,
        width = 179,
        height = 46)

        img3 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Button (2).png")
        b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.volverInicio,
        cursor = "hand2",
        relief = "flat")

        b3.place(
        x = 1185, y = 6,
        width = 56,
        height = 56)

        img4 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Button (3).png")
        self.b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.editarDatos,
        cursor = "hand2",
        relief = "flat")

        self.b4.place(
        x = 678, y = 492,
        width = 286,
        height = 39)


        img5 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Button (4).png")
        self.b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.realizarCambios,
        cursor = "hand2",
        relief = "flat")


        # ------------------->>>>>>>>>> ENTRYS >>>>>>>--------------------------------------->>>>>>>


        entry1_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Entry.png")
        entry1_bg = canvas.create_image(
            820, 230,
            image = entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            highlightthickness = 0)

        self.entry1.place(
            x = 692, y = 218,
            width = 248.0,
            height = 25)
        
        # 43 de dif.

        entry2_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox2.png")
        entry2_bg = canvas.create_image(
            820, 275,
            image = entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            highlightthickness = 0)

        self.entry2.place(
            x = 692, y = 263,
            width = 248.0,
            height = 25)

        
        entry3_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Usuarios/img_textBox3.png")
        entry3_bg = canvas.create_image(
            820, 318,
            image = entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            highlightthickness = 0)

        self.entry3.place(
            x = 692, y = 306,
            width = 248.0,
            height = 25)


        entry4_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Entry.png")
        entry4_bg = canvas.create_image(
            820, 404,
            image = entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            highlightthickness = 0)

        self.entry4.place(
            x = 692, y = 392,
            width = 248.0,
            height = 25)
        
    
        entry5_img = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Entry.png")
        entry5_bg = canvas.create_image(
            820, 447,
            image = entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            readonlybackground = "#d9d9d9",
            highlightthickness = 0)

        self.entry5.place(
            x = 692, y = 435,
            width = 248.0,
            height = 25)


        query = "SELECT Nombre, Num_Contacto, Usuario, Contraseña FROM usuario WHERE Rut = ?"
        self.cursor.execute(query, (self.user,))
        result = self.cursor.fetchone()

        if result:
            self.nombre, self.num_contacto, self.usuario, self.contraseña = result
            self.entry1.insert(0, self.user)
            self.entry1.config(state="readonly")
            self.entry2.insert(0, self.nombre)
            self.entry2.config(state="readonly")
            self.entry3.insert(0, self.num_contacto)
            self.entry3.config(state="readonly")
            self.entry4.insert(0, self.usuario)
            self.entry4.config(state="readonly")
            self.entry5.insert(0, self.contraseña)
            self.entry5.config(show="*")
            self.entry5.config(state="readonly")

        # --------------------->>>>>>>>> MARCOS DE INFO. >>>>>>--------------------------------------->>>>>>>

        dash0 = Frame(relief="flat", bg="#8c8c8c")
        dash0.place(
        x = 415, y = 38,
        width=290, height=40)

        img6 = PhotoImage(file=f"{img_dir}/Imagenes/M. Cuenta/Dash.png")
        ultimo_access = Label(dash0, image=img6, bg="#8c8c8c")
        ultimo_access.place(x=0, y=0, relwidth=1, relheight=1)


        self.cursor.execute("SELECT Ultima_Conexión FROM usuario WHERE Rut = ?", (self.user,))
        ultimo_acceso = self.cursor.fetchone()
        print(ultimo_acceso)
        if ultimo_acceso and ultimo_acceso[0]:
            # Muestra la fecha/hora en tu interfaz
            momento = ultimo_acceso[0]
        else:
            momento = "Sin registro"
        
        acceso = Label(dash0, text=momento, bg="#222222", fg="white", font=("Helvetica", 11, "bold"))
        acceso.place(x=122, y=10)

            # ------------------------------------------------------------------------------------------

        dash1 = Frame(relief="flat", bg="#8c8c8c")
        dash1.place(
        x = 712, y = 38,
        width=233, height=40)

        img7 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Dash (1).png")
        ultima_compra = Label(dash1, image=img7, bg="#8c8c8c")

        ultima_compra.place(x = 0, y = 0, relwidth=1, relheight=1)

        query = "SELECT Fecha FROM compra ORDER BY Fecha DESC LIMIT 1"
        self.cursor.execute(query)
        ultima_compra_fecha = self.cursor.fetchone()
        if ultima_compra_fecha and ultima_compra_fecha[0]:
            momento = ultima_compra_fecha[0]
        else:
            momento = "Sin registro"

        ultima_compra_label = Label(ultima_compra, text=momento, bg="#222222", fg="white", font=("Helvetica", 11, "bold"))
        ultima_compra_label.place(x=120, y=9)

            # -----------------------------------------------------------------------------------------------

        dash2 = Frame(relief="flat", bg="#8c8c8c")
        dash2.place(
        x = 952, y = 38,
        width=231, height=40)


        img8 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Dash (2).png")
        venta = Label(dash2, image=img8, bg="#8c8c8c")

        venta.place(x = 0, y = 0, relwidth=1, relheight=1)

        query = "SELECT Num_Boleta FROM venta WHERE usuario_Rut = ? ORDER BY Fecha DESC LIMIT 1"
        self.cursor.execute(query, (self.user,))
        num_boleta = self.cursor.fetchone()
        if num_boleta:
            boleta = f'Bol. N° {num_boleta[0]}'
        else:
            boleta = "Ninguna Realizada"

        ultima_venta = Label(dash2, text=boleta, bg="#222222", fg="white", font=("Helvetica", 11, "bold"))
        ultima_venta.place(x=108, y=10)

            # --------------------------------------------------------------------------------------------------

        dash3 = Frame(relief="flat", bg="#8c8c8c")
        dash3.place(
        x = 415, y = 92,
        width=530, height=40)

        img9 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Dash (3).png")
        conexion = Label(dash3, image=img9, bg="#8c8c8c")

        conexion.place(x = 0, y = 0, relwidth=1, relheight=1)


        query = "SELECT Nombre, Ultima_Conexión FROM usuario WHERE Rut IS NOT ? ORDER BY Ultima_Conexión DESC LIMIT 1"
        self.cursor.execute(query, (self.user,))
        ultimo_usuario = self.cursor.fetchall()

        if ultimo_usuario:
            nombre_conexion = f"{ultimo_usuario[0][0]} | {ultimo_usuario[0][1]}"
        else:
            nombre_conexion = "Sin registro de otro Usuario"

        ultima_conexion = Label(conexion, text=nombre_conexion, bg="#222222", fg="white", font=("Helvetica", 11, "bold"))
        ultima_conexion.place(x=156, y=7)

            # --------------------------------------------------------------------------------------------------


        dash4 = Frame(relief="flat", bg="#8c8c8c")
        dash4.place(
        x = 952, y = 92,
        width=231, height=40)

        img10 = PhotoImage(file = f"{img_dir}/Imagenes/M. Cuenta/Dash (4).png")
        total = Label(dash4, image=img10, bg="#8c8c8c")

        total.place(x = 0, y = 0, relwidth=1, relheight=1)

        query = "SELECT COUNT(DISTINCT Num_Boleta) FROM venta WHERE usuario_Rut = ?"
        self.cursor.execute(query, (self.user,))
        total_ventas = self.cursor.fetchone()
        if total_ventas:
            total_vent = total_ventas[0]
        else:
            total_vent = 0
        
        total_ventas_label = Label(total, text=total_vent, bg="#222222", fg="white", font=("Helvetica", 11, "bold"))
        total_ventas_label.place(x=108, y=7)

        self.window.mainloop()


    def cambiarImagen(self):
        
        img_dir = os.getcwd()
        perfiles_dir = os.path.join(img_dir, "Imagenes", "Perfiles")
        os.makedirs(perfiles_dir, exist_ok=True)

        img_path = filedialog.askopenfilename(initialdir=img_dir, title="Seleccionar imagen",
                                               filetypes=(("Archivos PNG", "*.png"), ("Todos los archivos", "*.*")))

        if img_path:
            # Usa el rut como nombre de archivo para evitar duplicados
            ext = os.path.splitext(img_path)[1]
            nuevo_nombre = f"{self.user}{ext}"
            destino = os.path.join(perfiles_dir, nuevo_nombre)
            shutil.copy(img_path, destino)

            # Guarda solo el nombre en la BD
            query = "UPDATE usuario SET Imagen = ? WHERE Rut = ?"
            self.cursor.execute(query, (nuevo_nombre, self.user))
            self.mydb.commit()

            # Recarga la imagen circular y actualiza en el canvas
            nueva_img = utl.make_circle_image(destino)
            self.profile_img = nueva_img  # Guarda referencia para evitar GC
            self.canvas.itemconfig(self.foto_perfil_id, image=nueva_img)


    def editarDatos(self):

        self.entry1.configure(state="normal")
        self.entry2.configure(state="normal")
        self.entry3.configure(state="normal")
        self.entry4.configure(state="normal")
        self.entry5.configure(state="normal")
        self.entry5.config(show="")

        self.b4.place_forget()

        self.b5.place(
        x = 678, y = 492,
        width = 286,
        height = 39)


    def realizarCambios(self):

        nuevo_rut = self.entry1.get()
        nuevo_nombre = self.entry2.get()
        nuevo_num_contacto = self.entry3.get()
        nuevo_usuario = self.entry4.get()
        nueva_contraseña = self.entry5.get()

        if not (nuevo_rut and nuevo_nombre and nuevo_num_contacto and nuevo_usuario and nueva_contraseña):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        if self.nombre == nuevo_nombre and self.num_contacto == nuevo_num_contacto and self.usuario == nuevo_usuario and self.contraseña == nueva_contraseña and self.user == nuevo_rut:
            messagebox.showwarning("Advertencia", "No se realizaron cambios en los datos.")
            return        

        resultado = messagebox.askyesno("Confirmar Cambios", "¿Estás seguro de que deseas guardar los cambios?")
        if resultado:
            try:
                self.cursor.execute("""
                    UPDATE usuario
                    SET Rut = ?, Nombre = ?, Num_Contacto = ?, Usuario = ?, Contraseña = ?
                    WHERE Rut = ?
                """, (nuevo_rut, nuevo_nombre, nuevo_num_contacto, nuevo_usuario, nueva_contraseña, self.user))
                self.mydb.commit()

                variables.logged_user = nuevo_rut
                self.user = nuevo_rut

                self.entry1.configure(state="readonly")
                self.entry2.configure(state="readonly")
                self.entry3.configure(state="readonly")
                self.entry4.configure(state="readonly")
                self.entry5.config(show="*")
                self.entry5.configure(state="readonly")

                self.b5.place_forget()

                self.b4.place(
                x = 678, y = 492,
                width = 286,
                height = 39)

                messagebox.showinfo("Éxito", "Datos actualizados correctamente.")

            except sqlite3.IntegrityError as e:
                messagebox.showerror("Error", f"No se pudo actualizar los datos: {e}")