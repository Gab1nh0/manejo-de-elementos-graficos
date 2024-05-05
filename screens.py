import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from dda import Dda
from bresenham import Bresen
from circular import Circular

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background="#222831")
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):

        topframe = customtkinter.CTkFrame(master=self, width=1000, height=400, fg_color='transparent')
        topframe.pack(expand=True)
        topframe.place(x=10, y=10)

        imgMenu = ImageTk.PhotoImage(Image.open('menubtn.png'))
        
        btnIni = customtkinter.CTkButton(self, text='Computacion Grafica y Visual - Proyecto 1', width=140, height=28, fg_color='transparent', font=("Roboto", 22), anchor="w", image=imgMenu, compound=tk.LEFT, hover=False)
        btnIni.pack(expand=True)
        btnIni.place(x=20, y=20)


        button = customtkinter.CTkButton(self, text='Algoritmo DDA para dibujar líneas', width=1180, height=70, fg_color="#393E46", hover_color="#2C3037", 
                                        anchor="w",corner_radius=50, font=("Roboto", 24), command=self.moverDda)
        button.place(x=10, y=120)

        btnBerman = customtkinter.CTkButton(self, text='Algoritmo de Bresenham para dibujar líneas', width=1180, height=70, fg_color="#393E46", hover_color="#2C3037", 
                                        anchor="w",corner_radius=50, font=("Roboto", 24), command=self.moverBresenham)
        btnBerman.place(x=10, y=220)

        btnBerman = customtkinter.CTkButton(self, text='Algoritmo de Punto Medio para la circunferencia', width=1180, height=70, fg_color="#393E46", hover_color="#2C3037", 
                                        anchor="w",corner_radius=50, font=("Roboto", 24), command=self.moverCircular)
        btnBerman.place(x=10, y=320)

    def moverDda(self):  # nos muestra el frame del dda
        self.controller.show_frame(Dda)
    
    def moverBresenham(self):  # nos muestra el frame del dda
        self.controller.show_frame(Bresen)

    def moverCircular(self):  # nos muestra el frame del dda
        self.controller.show_frame(Circular)
