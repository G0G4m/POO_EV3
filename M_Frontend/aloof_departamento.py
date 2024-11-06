import tkinter as tk
from tkinter import ttk

class tab_departamento(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        subtab_departamento = ttk.Notebook(self)
        subtab_departamento.pack(expand = True, fill = "both")

        tab_departamento_agregar = tk.Frame(subtab_departamento)
        tab_departamento_editar = tk.Frame(subtab_departamento)
        tab_departamento_eliminar = tk.Frame(subtab_departamento)

        subtab_departamento.add(tab_departamento_agregar, text= "Agregar")
        subtab_departamento.add(tab_departamento_editar, text= "Editar")
        subtab_departamento.add(tab_departamento_eliminar, text = "Eliminar")