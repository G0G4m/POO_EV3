import tkinter as tk
from tkinter import ttk

class tab_reg_tiempo(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        subtab_reg_tiempo = ttk.Notebook(self)
        subtab_reg_tiempo.pack(expand=True,fill="both")

        tab_reg_tiempo = tk.Frame(subtab_reg_tiempo)

        subtab_reg_tiempo.add(tab_reg_tiempo,text="Agregar")

        label_reg_tiempo_agregar = tk.Label(tab_reg_tiempo,text="AGREGAR REGISTRO DE TIEMPO",font=("arial",16)).place(x=100,y=10)

        tittle_id_empleado = tk.Label(tab_reg_tiempo,text="Empleado").place(x=50,y=60)
        text_id_empleado = tk.Entry(tab_reg_tiempo,width=55).place(x=150,y=60)
        
        tittle_id_proyecto = tk.Label(tab_reg_tiempo,text="Proyecto").place(x=50,y=80)
        text_id_proyecto = tk.Entry(tab_reg_tiempo,width=55).place(x=150,y=80)

        tittle_registro = tk.Label(tab_reg_tiempo,text="Fecha registro").place(x=50,y=100)
        text_registro = tk.Entry(tab_reg_tiempo,width=55).place(x=150,y=100)

        tittle_reg_horas = tk.Label(tab_reg_tiempo,text="Cantidad horas").place(x=50,y=120)
        text_reg_horas = tk.Entry(tab_reg_tiempo,width=55).place(x=150,y=120)

        tittle_tb_realizado = tk.Label(tab_reg_tiempo,text="Trabajo realizado").place(x=50,y=140)
        text_tb_realizado = tk.Entry(tab_reg_tiempo,width=55).place(x=150,y=140)

        button_save = tk.Button(tab_reg_tiempo,text="Guardar").place(x=150,y=180)
        button_update = tk.Button(tab_reg_tiempo,text="Editar").place(x=220,y=180)
        button_delete = tk.Button(tab_reg_tiempo,text="Borrar").place(x=270,y=180)