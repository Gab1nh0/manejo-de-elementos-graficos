import tkinter as tk
from tkinter import ttk
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

class Elipse(tk.Frame):
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


        # Frame izquierdo superior con los puntos

        izqFrame = customtkinter.CTkFrame(master=self, width=600, height=250, fg_color='transparent')
        izqFrame.place(x=10, y=70)

        titulo = customtkinter.CTkLabel(master=izqFrame, text='Algoritmo de Punto Medio Elipse', width=40, height=28, fg_color='transparent', font=("Roboto", 18))
        titulo.place(x=10, y=10)

        label = customtkinter.CTkLabel(master=izqFrame, text='rx =', width=40, height=28, font=("Roboto", 18, "bold"), fg_color='transparent')
        label.place(x=10, y=70)

        self.rx = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent',)
        self.rx.place(x=60, y=70)
        self.rx.focus_set()

        label = customtkinter.CTkLabel(master=izqFrame, text='ry =', width=40, height=28, font=("Roboto", 18,"bold"), fg_color='transparent')
        label.place(x=260, y=70)

        self.ry = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.ry.place(x=300, y=70)
        
        label = customtkinter.CTkLabel(master=izqFrame, text='xc =', width=40, height=28, font=("Roboto", 18,"bold"), fg_color='transparent')
        label.place(x=10, y=120)

        self.xc = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.xc.place(x=60, y=120)

        label = customtkinter.CTkLabel(master=izqFrame, text='yc =', width=40, height=28, font=("Roboto", 18,"bold"), fg_color='transparent')
        label.place(x=260, y=120)

        self.yc = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.yc.place(x=300, y=120)

        button = customtkinter.CTkButton(master=izqFrame, text='Graficar', width=140, height=28, font=("Roboto", 18), command=self.button_eventElipse)
        button.place(x=300, y=170)

        button = customtkinter.CTkButton(master=izqFrame, text='Limpiar', width=140, height=28, font=("Roboto", 18), command=self.limpiar, fg_color="#CD3030", hover_color="#900000")
        button.place(x=150, y=170)
    
    def trazarElipse(self, xc, yc, rx, ry):
        x = 0
        y = ry

        x_points = []
        y_points = []

        # Parámetro de decisión inicial de la región 1
        d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
        dx = 2 * ry * ry * x
        dy = 2 * rx * rx * y

        # Para la región 1
        while dx < dy:
            # Agregar puntos basados en simetría de 4 vías
            x_points.extend([x + xc, -x + xc, x + xc, -x + xc])
            y_points.extend([y + yc, y + yc, -y + yc, -y + yc])

            # Actualizar valor del parámetro de decisión basado en el algoritmo
            if d1 < 0:
                x += 1
                dx = dx + (2 * ry * ry)
                d1 = d1 + dx + (ry * ry)
            else:
                x += 1
                y -= 1
                dx = dx + (2 * ry * ry)
                dy = dy - (2 * rx * rx)
                d1 = d1 + dx - dy + (ry * ry)
        
        # Parámetro de decisión de la región 2
        d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry))

        # Agregar puntos de la región 2
        while y >= 0:
            # Agregar puntos basados en simetría de 4 vías
            x_points.extend([x + xc, -x + xc, x + xc, -x + xc])
            y_points.extend([y + yc, y + yc, -y + yc, -y + yc])

            # Actualizar parámetro de decisión
            if d2 > 0:
                y -= 1
                dy = dy - (2 * rx * rx)
                d2 = d2 + (rx * rx) - dy
            else:
                y -= 1
                x += 1
                dx = dx + (2 * ry * ry)
                dy = dy - (2 * rx * rx)
                d2 = d2 + dx - dy + (rx * rx)

        return x_points, y_points
    

    def limpiar(self):
        self.xc.delete(0, tk.END)
        self.yc.delete(0, tk.END)
        self.rx.delete(0, tk.END)
        self.ry.delete(0, tk.END)

        #frame izquierdo inferior sin datos
        izqInf = customtkinter.CTkFrame(master=self, width=560, height=40, fg_color='transparent')
        izqInf.place(x=10, y=290)

        # Frame derecho sin grafica
        derFrame = customtkinter.CTkFrame(master=self, width=560, height=620, fg_color="#222831")
        derFrame.place(x=630, y=140)

        #frame sin tabla
        tablaFrame = customtkinter.CTkFrame(master=self, width=560, height=400, fg_color="#222831")
        tablaFrame.place(x=30, y=360)

    def button_eventElipse(self): 
        xc = int(self.xc.get())
        yc = int(self.yc.get())
        rx = int(self.rx.get())
        ry = int(self.ry.get())  # Corregido: utilizamos self.ry en lugar de self.rx para obtener el valor de ry

        x_points, y_points = self.trazarElipse(xc, yc, rx, ry)

        # Crear la figura y el gráfico
        fig = Figure(figsize=(5, 4), dpi=100, facecolor='#222831')
        plot = fig.add_subplot(111)
        plot.set_facecolor('#222831')

        if self.treeview:
            self.treeview.destroy()

        tablaFrame = customtkinter.CTkFrame(master=self, width=560, height=400, fg_color="#222831")
        tablaFrame.place(x=30, y=360)

        style = ttk.Style()
        style.configure("Treeview", background="#222831", foreground="white", font=("Roboto", 18), rowheight=30, bordercolor="#FFD369")
        style.configure("Treeview.Heading", background="#222831", foreground="black", font=("Roboto", 18), rowheight=30)

        self.treeview = ttk.Treeview(tablaFrame, columns=('X', 'Y'), show='headings', style="Treeview")
        self.treeview.heading('X', text='X')
        self.treeview.heading('Y', text='Y')
        self.treeview.pack()

        # Agregar los puntos a la tabla
        for i in range(len(x_points)):
            self.treeview.insert('', 'end', values=(x_points[i], y_points[i]))

        # Dibujar la línea
        plot.plot(x_points, y_points, 'bo', color='#FFD369')
        plot.set_aspect('equal', adjustable='box')
        plot.set_xlabel('X',color='white')
        plot.set_ylabel('Y', color='white')
        plot.set_title('Punto Medio Elipse', color='white')
        plot.grid(True, color='white')

        plot.spines['bottom'].set_color('white')
        plot.spines['left'].set_color('white')
        plot.spines['top'].set_color('white')
        plot.spines['right'].set_color('white')

        plot.tick_params(axis='x', colors='white')
        plot.tick_params(axis='y', colors='white')

        # Frame derecho con grafica
        derFrame = customtkinter.CTkFrame(master=self, width=560, height=620, fg_color="#222831")
        derFrame.place(x=630, y=140)

        canvas = FigureCanvasTkAgg(fig, master=derFrame)
        canvas.draw()
        canvas.get_tk_widget().pack()



    def moverHome(self): #nos lleva al inicio
        from screens import Home
        self.controller.show_frame(Home)
