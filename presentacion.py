import tkinter as tk
from tkinter import ttk
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


class Presentacion(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background="#222831")
        self.controller = controller
        self.init_widgets()
        self.treeview = None

    def init_widgets(self):
        # Frame navbar
        topframe = customtkinter.CTkFrame(master=self, width=1000, height=400, fg_color='transparent')
        topframe.pack(expand=True)
        topframe.place(x=10, y=10)

        imgBack = ImageTk.PhotoImage(Image.open('backbtn.png'))

        button = customtkinter.CTkButton(master=topframe, text='Regresar', width=200, height=40, font=("Roboto", 22), command=self.moverHome, 
                                         fg_color='transparent', anchor="w", image=imgBack, compound=tk.LEFT, hover=False)
        button.place(x=10, y=10)

        #frame Inferior
        frameInferior = customtkinter.CTkFrame(master=self, width=1000, height=600, fg_color='transparent')
        frameInferior.place(x=100, y=60)

        label = customtkinter.CTkLabel(master=frameInferior, text='Universidad Tecnlógica de Panamá', width=40, height=28, fg_color='transparent',  font=("Roboto", 22), justify="center")
        label.place(x=303, y=10)

        label = customtkinter.CTkLabel(master=frameInferior, text='Facultad de Ingeniería de Sistemas Computacionales', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=212, y=60)

        label = customtkinter.CTkLabel(master=frameInferior, text='Ingeniería de Software', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=377, y=110)

        label = customtkinter.CTkLabel(master=frameInferior, text='Computación Gráfica y Visual', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=338, y=160)

        label = customtkinter.CTkLabel(master=frameInferior, text='Proyecto #1', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=436, y=210)

        label = customtkinter.CTkLabel(master=frameInferior, text='Eric Bethancourt', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=408, y=260)

        label = customtkinter.CTkLabel(master=frameInferior, text='Gabriel Martínez', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=408, y=290)

        label = customtkinter.CTkLabel(master=frameInferior, text='Javier Urrutia', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=426, y=320)

        label = customtkinter.CTkLabel(master=frameInferior, text='Profesor: Mark Tack', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=391, y=370)

        label = customtkinter.CTkLabel(master=frameInferior, text='I Semestre', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=442, y=420)

        label = customtkinter.CTkLabel(master=frameInferior, text='2024', width=40, height=28, fg_color='transparent',  font=("Roboto", 22))
        label.place(x=471, y=450)

    def moverHome(self): #nos lleva al inicio
        from screens import Home
        self.controller.show_frame(Home)

    