#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import webbrowser  # Para abrir el mapa en el navegador

#modulos
import centros as m

"""funciones del sistema"""

# Función para filtrar centros por material reciclable
def filtrar_centros(material):
    resultados = []
    for centro in m.centros_reciclaje:
        if material in centro["materiales"]:
            resultados.append(centro)
    return resultados

# Funcion para filtrar y mostrar los centros
def arrojar_centros(list, frame): #lista de materiales y el frame del scrollbar
    material = list.get()
    resultados = filtrar_centros(material)
    frame.clear() #Limpiar la lista de resultados
    if resultados:
        for centro in resultados:
            mostrar_centro(centro["nombre"], centro["direccion"], centro["materiales"], frame.scrollable_frame)
    else:
        pass
        #resultado_list.insert(tk.END, "No se encontraron centros de reciclaje para el material especificado.") ???????????????


"""funciones de interfaz"""
#funcion para mostrar los centros filtrados, es la interfaz chavos
def mostrar_centro(nombre, direccion,materiales, root):
    # Crear un Frame para contener el centro
    centro = Frame(root, padx=15, pady=15, bg="#D9D9D9")
    centro.pack()

    # Agregar el nombre del centro
    nombreCentro = Label(centro, text=nombre, font=("Arial", 24, "bold"), fg="black", bg="#FFFFFF")
    nombreCentro.pack()

    # Agregar la direccion
    t_direccion = Label(centro, text="Direccion:", font=("Arial", 12, "bold"), bg="#D9D9D9", fg="black")
    m_direccion = Label(centro, text=direccion, font=("Arial", 12, "bold"), bg="#D9D9D9", fg="black")
    t_direccion.pack()
    m_direccion.pack()

    # Agregar un frame de informacion
    informacion = Frame(centro, bg="#FFFFFF", width=400, height=250)
    informacion.pack_propagate(False) #evitar el resize
    informacion.pack(side=LEFT, padx=25, pady=25)

    # Agregar los materiales
    t_materiales = Label(informacion, text="Materiales aceptados", font=("Arial", 12, "bold"), bg="#E6FFE6", fg="#2E8B57")
    t_materiales.pack()
    for m in materiales:
        m_materiales = Label(informacion, text=m)
        m_materiales.pack()
    
    # Agregar el frame de "imagenes" y maps
    imagenes = Frame(centro, bg="#FFFFFF", width=400, height=250)
    imagenes.pack_propagate(False) #evitar el resize
    imagenes.pack(side=RIGHT, padx=15, pady=15)

    #mostrar informacion
    t_map = Label(imagenes, text="Mapa:", font=("Arial", 12, "bold"), bg="#E6FFE6", fg="#2E8B57")
    t_map.pack()

#encabezado, solo interfaz
def encabezado(root):
    titulo_label = Label(root, text="GreenPoint", font=("Arial", 24, "bold"), bg="#ABEEB5", fg="#2E8B57")
    titulo_label.pack(fill="x")

#botones de inciar sesion
def Agregar_botones_inicio(encabezado,root):
    #agregamos los botones de iniciar sesion y 
    global btn_iniciar_sesion
    global btn_registrar_usuario

    btn_iniciar_sesion = Button(encabezado, text="inciar sesion", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command=lambda: abrir_ventana_login(root))
    btn_registrar_usuario = Button(encabezado, text="registrar usuario", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command=lambda: abrir_ventana_registar(root))
    btn_iniciar_sesion.grid(row=0, column=0)
    btn_registrar_usuario.grid(row=0, column=1)

#para elimninarlos
def actualizar_interfaz():
    btn_iniciar_sesion.grid_forget()
    btn_registrar_usuario.grid_forget()

#limpiar frames (por si acaso jsjs)
def limpiar_frame(frame):
   for w in frame.winfo_children():
      w.destroy()

#esto es robado si? sufri mucho agregando el scrollbar
class Frame_scroll(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self, height=500, width=1000)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, padx=50, pady=15)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side = RIGHT, fill = Y )
    
    def clear(self):
        limpiar_frame(self.scrollable_frame)

"""funciones de flujos alternos"""


def abrir_ventana_registar(root):
    #abrir ventana secundaria
    global ventana_registrar
    ventana_registrar = tk.Toplevel(root)
    ventana_registrar.title("Inicio de Sesión")
    ventana_registrar.geometry("400x300")
    ventana_registrar.configure(bg="#E6FFE6")

    # Título de la ventana
    titulo_label = tk.Label(ventana_registrar, text="Registro de Usuario", font=("Arial", 24, "bold"), bg="#E6FFE6", fg="#2E8B57")
    titulo_label.pack(pady=10)

    # Campos de entrada para el registro
    label_nombre = tk.Label(ventana_registrar, text="Nombre:", bg="#E6FFE6")
    label_nombre.pack(pady=5)
    
    global entry_nombre
    entry_nombre = tk.Entry(ventana_registrar, width=30)
    entry_nombre.pack(pady=5)

    label_email = tk.Label(ventana_registrar, text="Email:", bg="#E6FFE6")
    label_email.pack(pady=5)
    
    global entry_email
    entry_email = tk.Entry(ventana_registrar, width=30)
    entry_email.pack(pady=5)

    label_password = tk.Label(ventana_registrar, text="Contraseña:", bg="#E6FFE6")
    label_password.pack(pady=5)
    global entry_password
    entry_password = tk.Entry(ventana_registrar, width=30, show="*")
    entry_password.pack(pady=5)

    # Botón para registrar
    registrar_btn = tk.Button(ventana_registrar, text="Registrar", command=registrar_usuario, bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
    registrar_btn.pack(pady=10)

def registrar_usuario():
    nombre = entry_nombre.get()
    email = entry_email.get()
    password = entry_password.get()

    if nombre and email and password:
        m.usuarios[email] = {"nombre": nombre, "password": password}
        messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente")
        entry_nombre.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        ventana_registrar.withdraw() # destruyelo w
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")


# Función para iniciar sesión
def iniciar_sesion():
    email = entry_email_login.get()
    password = entry_password_login.get()
    #codigo chido que puso alexis, no me gusta pero se ve chido
    if email in m.usuarios and m.usuarios[email]["password"] == password:
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido {m.usuarios[email]['nombre']}")
        #root.update_idletasks()
        m.incio_sesion = True
        print(m.incio_sesion)
        actualizar_interfaz() #para actualizar si ya incio sesion
        ventana_login.withdraw()  # destruye la ventana alv
    else:
        messagebox.showerror("Error", "Contraseña o email incorrecto")


# Función para abrir la ventana de inicio de sesión
def abrir_ventana_login(root):
    #abrir ventana secundaria
    global ventana_login
    ventana_login = tk.Toplevel(root)
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("400x300")
    ventana_login.configure(bg="#E6FFE6")

    #iniciar sesion
    label_login = tk.Label(ventana_login, text="Inicio de Sesión", font=("Arial", 16, "bold"), bg="#E6FFE6")
    label_login.pack(pady=10)

    #email
    label_email_login = tk.Label(ventana_login, text="Email:", bg="#E6FFE6")
    label_email_login.pack(pady=5)
    global entry_email_login
    entry_email_login = tk.Entry(ventana_login, width=30)
    entry_email_login.pack(pady=5)

    #contraseña
    label_password_login = tk.Label(ventana_login, text="Contraseña:", bg="#E6FFE6")
    label_password_login.pack(pady=5)
    global entry_password_login
    entry_password_login = tk.Entry(ventana_login, width=30, show="*")
    entry_password_login.pack(pady=5)

    #boton para tenerminar la operacion
    login_btn = tk.Button(ventana_login, text="Iniciar Sesión", command=iniciar_sesion, bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
    login_btn.pack(pady=10)
        

        
"""""
class Ventana_principal(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.geometry("1100x700")
        self.master.configure(bg="#E6FFE6")
        self.master.resizable(False, False)
        self.pack(fill=BOTH)
        self.Crear_widgets()

    
    def Crear_widgets(self):
        #flujo normal
        encabezado(self) #necabezado por default

        #botones de iniciar sesion y registrarse
        encabezado2 = Frame(self, bg="green")
        encabezado2.pack(fill="x")

        if m.incio_sesion == False:
            #agregamos los botones de iniciar sesion y registrarse
            iniciar_sesion = Button(encabezado2, text="inciar sesion", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command=lambda: abrir_ventana_login(self))
            iniciar_sesion.grid(row=0, column=0)

            registrar_usuario = Button(encabezado2, text="registrar usuario", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command=lambda: abrir_ventana_registar(self))
            registrar_usuario.grid(row=0, column=1)

        #texto
        subtitulo_label = tk.Label(self, text="Buscar Centros de Reciclaje por Material", font=("Arial", 14), bg="#E6FFE6")
        subtitulo_label.pack(pady=5)

        # Menú desplegable para seleccionar material
        busqueda = Frame(self)
        busqueda.pack()

        #Este es un multi opciones
        material_combo = ttk.Combobox(busqueda, values=m.materiales_reciclables, state="readonly", width=40) #aqui se establece
        material_combo.grid(row=0, column=1)
        material_combo.current(0)  # Establecer el valor por defecto

        # Botón de búsqueda
        buscar_btn = Button(busqueda, text="Buscar", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command=lambda: arrojar_centros(material_combo, lista)) #aqui metemos el frame y el multiselector, se usa lambda por los argumentos, que no se les olvide porfa
        buscar_btn.grid(row=0, column=0)

        #frame.clear()

        #frames
        lista = Frame_scroll(self) #frame principal de busqueda y SCROLLBAR
        lista.pack()

    # La razon por lo que hice este flujo como CLASE JAJAJAJAJAJA
    def Refrescar(self):
        pass
        # self.update_idletasks()
"""
