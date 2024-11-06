import tkinter as tk
from tkinter import ttk

texto_bienvenida = "Bienvenido admin al gestionador de la base de datos"

class tab_home(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.label_home = tk.Label( self,text=texto_bienvenida)
        self.label_home.pack(pady = 40, padx = 40)