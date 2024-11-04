import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser  # Para abrir el mapa en el navegador

# Datos de los centros de reciclaje
centros_reciclaje = [
    {
        "nombre": "Planta de Reciclaje CIREC Miguel Hidalgo",
        "direccion": "Calle 5 de mayo #150, Col. San Lorenzo Tlaltenango",
        "materiales": ["Escombros", "Desechos vegetales", "Aceites y grasas"],
        "horarios": "Lunes a viernes: 8:00 am - 6:00 pm",
        "coordenadas": "19.432608, -99.133209"
    },
    {
        "nombre": "Centro de Acopio de Residuos Reciclables (CAMH)",
        "direccion": "Alcaldía Miguel Hidalgo, CDMX",
        "materiales": ["Plásticos", "Papel", "Cartón", "Vidrio", "Metales", "Electrónicos"],
        "horarios": "Lunes a sábado: 9:00 am - 5:00 pm",
        "coordenadas": "19.434, -99.140"
    },
    {
        "nombre": "Centro de Reciclaje Avenida Juárez",
        "direccion": "Avenida Juárez, Miguel Hidalgo",
        "materiales": ["Cascajo", "Residuos vegetales", "Aceites usados"],
        "horarios": "Lunes a viernes: 7:00 am - 4:00 pm",
        "coordenadas": "19.436, -99.142"
    }
]

usuarios = {}  # Diccionario para almacenar los usuarios registrados

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = entry_nombre.get()
    email = entry_email.get()
    password = entry_password.get()
    tipo_usuario = tipo_usuario_combo.get()

    if nombre and email and password and tipo_usuario:
        usuarios[email] = {"nombre": nombre, "password": password, "tipo": tipo_usuario}
        messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente")
        entry_nombre.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        tipo_usuario_combo.set('')  # Limpiar el combo box
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

# Función para iniciar sesión
def iniciar_sesion():
    email = entry_email_login.get()
    password = entry_password_login.get()

    if email in usuarios and usuarios[email]["password"] == password:
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido {usuarios[email]['nombre']}")
        ventana_login.withdraw()  # O puedes usar destroy()
        abrir_busqueda_centros()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

# Función para abrir el mapa en el navegador
def abrir_mapa(coordenadas):
    lat, lon = coordenadas.split(", ")
    url = f"https://www.google.com/maps?q={lat},{lon}"
    webbrowser.open(url)

# Función para mostrar detalles del centro y abrir el mapa
def mostrar_detalles(event):
    seleccion = resultado_list.curselection()
    if seleccion:
        index = seleccion[0]
        centro = centros_reciclaje[index]
        detalles_text.delete(1.0, tk.END)
        detalles_text.insert(tk.END, f"Nombre: {centro['nombre']}\n")
        detalles_text.insert(tk.END, f"Dirección: {centro['direccion']}\n")
        detalles_text.insert(tk.END, f"Materiales: {', '.join(centro['materiales'])}\n")
        detalles_text.insert(tk.END, f"Horarios: {centro['horarios']}\n")

        # Botón para abrir mapa
        for widget in detalles_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        btn_mapa = tk.Button(detalles_frame, text="Ver en Mapa", command=lambda: abrir_mapa(centro['coordenadas']), bg="#2E8B57", fg="white")
        btn_mapa.pack()

# Función para filtrar centros por material reciclable
def filtrar_centros(material):
    resultados = []
    for centro in centros_reciclaje:
        if material in centro["materiales"]:
            resultados.append(centro)
    return resultados

# Función para mostrar resultados de búsqueda
def mostrar_resultados():
    material = material_combo.get()
    resultados = filtrar_centros(material)
    resultado_list.delete(0, tk.END)  # Limpiar la lista de resultados
    if resultados:
        for centro in resultados:
            resultado_list.insert(tk.END, centro["nombre"])
    else:
        resultado_list.insert(tk.END, "No se encontraron centros de reciclaje para el material especificado.")

# Función para abrir la ventana de búsqueda de centros
def abrir_busqueda_centros():
    ventana_busqueda = tk.Toplevel(root)
    ventana_busqueda.title("Buscar Centros de Reciclaje")
    ventana_busqueda.geometry("600x600")
    ventana_busqueda.configure(bg="#E6FFE6")

    # Pestaña de búsqueda de centros de reciclaje
    titulo_label = tk.Label(ventana_busqueda, text="GreenPoint", font=("Arial", 24, "bold"), bg="#E6FFE6", fg="#2E8B57")
    titulo_label.pack(pady=10)
    subtitulo_label = tk.Label(ventana_busqueda, text="Buscar Centros de Reciclaje por Material", font=("Arial", 14), bg="#E6FFE6")
    subtitulo_label.pack(pady=5)

    # Lista de materiales reciclables (para el dropdown)
    materiales_reciclables = [
        "Escombros", "Desechos vegetales", "Aceites y grasas", "Plásticos", "Papel", "Cartón",
        "Vidrio", "Metales", "Electrónicos", "Cascajo", "Aceites usados"
    ]

    # Menú desplegable para seleccionar material
    material_label = tk.Label(ventana_busqueda, text="Selecciona un material reciclable:", bg="#E6FFE6")
    material_label.pack(pady=5)
    global material_combo
    material_combo = ttk.Combobox(ventana_busqueda, values=materiales_reciclables, state="readonly", width=40)
    material_combo.pack(pady=5)
    material_combo.current(0)  # Establecer el valor por defecto

    # Botón de búsqueda
    buscar_btn = tk.Button(ventana_busqueda, text="Buscar", command=mostrar_resultados, bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
    buscar_btn.pack(pady=10)

    # Lista para mostrar los resultados
    global resultado_list
    resultado_list = tk.Listbox(ventana_busqueda, height=10, width=60)
    resultado_list.pack(pady=10)

    # Mostrar detalles cuando seleccionan un centro de la lista
    resultado_list.bind("<<ListboxSelect>>", mostrar_detalles)

    # Área de texto para mostrar detalles
    global detalles_frame
    detalles_frame = tk.Frame(ventana_busqueda, bg="#E6FFE6")
    detalles_frame.pack(pady=10)

    global detalles_text
    detalles_text = tk.Text(detalles_frame, height=8, width=60, wrap="word", bg="#F0FFF0")
    detalles_text.pack()

# Función para abrir la ventana de inicio de sesión
def abrir_ventana_login():
    global ventana_login
    ventana_login = tk.Toplevel(root)
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("400x300")
    ventana_login.configure(bg="#E6FFE6")

    label_login = tk.Label(ventana_login, text="Inicio de Sesión", font=("Arial", 16, "bold"), bg="#E6FFE6")
    label_login.pack(pady=10)
    label_email_login = tk.Label(ventana_login, text="Email:", bg="#E6FFE6")
    label_email_login.pack(pady=5)
    global entry_email_login
    entry_email_login = tk.Entry(ventana_login, width=30)
    entry_email_login.pack(pady=5)
    label_password_login = tk.Label(ventana_login, text="Contraseña:", bg="#E6FFE6")
    label_password_login.pack(pady=5)
    global entry_password_login
    entry_password_login = tk.Entry(ventana_login, width=30, show="*")
    entry_password_login.pack(pady=5)
    login_btn = tk.Button(ventana_login, text="Iniciar Sesión", command=iniciar_sesion, bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
    login_btn.pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("GreenPoint - Registro de Usuario")
root.geometry("400x400")
root.configure(bg="#E6FFE6")

# Título de la ventana
titulo_label = tk.Label(root, text="Registro de Usuario", font=("Arial", 24, "bold"), bg="#E6FFE6", fg="#2E8B57")
titulo_label.pack(pady=10)

# Campos de entrada para el registro
label_nombre = tk.Label(root, text="Nombre:", bg="#E6FFE6")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack(pady=5)

label_email = tk.Label(root, text="Email:", bg="#E6FFE6")
label_email.pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

label_password = tk.Label(root, text="Contraseña:", bg="#E6FFE6")
label_password.pack(pady=5)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(pady=5)

label_tipo_usuario = tk.Label(root, text="Tipo de Usuario:", bg="#E6FFE6")
label_tipo_usuario.pack(pady=5)
tipo_usuario_combo = ttk.Combobox(root, values=["Usuario Común", "Propietario de Centro"], state="readonly", width=28)
tipo_usuario_combo.pack(pady=5)
tipo_usuario_combo.current(0)  # Establecer valor por defecto

# Botón para registrar
registrar_btn = tk.Button(root, text="Registrar", command=registrar_usuario, bg="#2E8B57", fg="white", font=("Arial", 12, "bold"))
registrar_btn.pack(pady=10)

# Botón para abrir la ventana de inicio de sesión
login_btn = tk.Button(root, text="Ya tengo una cuenta - Iniciar Sesión", command=abrir_ventana_login, bg="#F0F0F0", fg="#2E8B57")
login_btn.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
