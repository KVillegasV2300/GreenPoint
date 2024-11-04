#librerias
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import webbrowser  # Para abrir el mapa en el navegador

# Lista de materiales reciclables
materiales_reciclables = [
    "Escombros", "Desechos vegetales", "Aceites y grasas", "Plásticos", "Papel", "Cartón",
    "Vidrio", "Metales", "Electrónicos", "Cascajo", "Aceites usados"
]

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
    },
    {
        "nombre": "Centro de Reciclaje Avenida Juárez",
        "direccion": "Avenida Juárez, Miguel Hidalgo",
        "materiales": ["Aceites y grasas", "Plásticos", "Papel", "Cartón"],
        "horarios": "Lunes a viernes: 7:00 am - 4:00 pm",
        "coordenadas": "19.436, -99.142"
    }
]

usuarios = {}  # Diccionario para almacenar los usuarios registrados

incio_sesion=False