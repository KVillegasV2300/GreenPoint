#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import webbrowser  # Para abrir el mapa en el navegador

#modulos
import centros as m
import funciones_c as f

#configuracion de la aplicacion
root = tk.Tk() #establecemos la "rama" principal
root.geometry("1100x700")
root.configure(bg="#E6FFE6")
root.resizable(False, False)


"""flujo principal"""

f.encabezado(root) #necabezado por default
#botones de iniciar sesion y registrarse
encabezado2 = Frame(root, bg="#636363")
encabezado2.pack(fill="x")
f.Agregar_botones_inicio(encabezado2, root)

#texto
subtitulo_label = Label(root, text="Buscar Centros de Reciclaje por Material", font=("Arial", 14), bg="#E6FFE6")
subtitulo_label.pack(pady=5)

# Menú desplegable para seleccionar material
busqueda = Frame(root)
busqueda.pack()

#Este es un multi opciones
material_combo = ttk.Combobox(busqueda, values=m.materiales_reciclables, state="readonly", width=40) #aqui se establece
material_combo.grid(row=0, column=1)
material_combo.current(0)  # Establecer el valor por defecto

# Botón de búsqueda
buscar_btn = Button(busqueda, text="Buscar", bg="#2E8B57", fg="white", font=("Arial", 12, "bold"), command=lambda: f.arrojar_centros(material_combo, lista)) #aqui metemos el frame y el multiselector, se usa lambda por los argumentos, que no se les olvide porfa
buscar_btn.grid(row=0, column=0)

#frame.clear()

#frames
lista = f.Frame_scroll(root) #frame principal de busqueda y SCROLLBAR
lista.pack()

root.mainloop()
