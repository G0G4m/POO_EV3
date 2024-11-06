import tkinter as tk
from tkinter import ttk

class tab_proyecto(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        subtab_proyecto = ttk.Notebook(self)
        subtab_proyecto.pack(expand = True, fill = "both")
        
        tab_proyecto_agregar = tk.Frame(subtab_proyecto)
        tab_proyecto_editar = tk.Frame(subtab_proyecto)
        tab_proyecto_eliminar = tk.Frame(subtab_proyecto)

        subtab_proyecto.add(tab_proyecto_agregar, text= "Agregar")
        subtab_proyecto.add(tab_proyecto_editar, text= "Editar")
        subtab_proyecto.add(tab_proyecto_eliminar, text = "Eliminar") 