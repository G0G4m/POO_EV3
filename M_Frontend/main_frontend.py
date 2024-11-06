from M_Frontend.aloof_home import tab_home
from M_Frontend.aloof_proyecto import tab_proyecto
from M_Frontend.aloof_departamento import tab_departamento
from M_Frontend.aloof_reg_tiempo import tab_reg_tiempo
import tkinter as tk
from tkinter import ttk

def main():

    root = tk.Tk()
    root.geometry("750x650")
    root.title("Framwork DB")
    root.resizable(False,False)

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True,fill="both")

    home_tab = tab_home(notebook)
    notebook.add(home_tab,text="Home")
    #empleado_tab = ""
    #notebook.add(empleado_tab,text="Empleado")
    departamento_tab = tab_departamento(notebook)
    notebook.add(departamento_tab,text="Departamento")
    proyecto_tab = tab_proyecto(notebook)
    notebook.add(proyecto_tab,text="Proyecto")
    registro_tab = tab_reg_tiempo(notebook)
    notebook.add(registro_tab,text="Registro de Tiempo")
    #api_tab = ""
    #notebook.add(api_tab,text="Informacion")

    root.mainloop()