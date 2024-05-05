import tkinter as tk
from tkinter import ttk
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


class Bresen(tk.Frame):
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

        titulo = customtkinter.CTkLabel(master=izqFrame, text='Algoritmo de Bresenham', width=40, height=28, fg_color='transparent', font=("Roboto", 18))
        titulo.place(x=10, y=10)

        label = customtkinter.CTkLabel(master=izqFrame, text='x₁ =', width=40, height=28, font=("Roboto", 18, "bold"), fg_color='transparent')
        label.place(x=10, y=70)

        self.x1 = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent',)
        self.x1.place(x=60, y=70)
        self.x1.focus_set()


        label = customtkinter.CTkLabel(master=izqFrame, text='y₁ =', width=40, height=28, font=("Roboto", 18,"bold"), fg_color='transparent')
        label.place(x=260, y=70)

        self.y1 = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.y1.place(x=300, y=70)
        

        label = customtkinter.CTkLabel(master=izqFrame, text='x₂ =', width=40, height=28, font=("Roboto", 18,"bold"), fg_color='transparent')
        label.place(x=10, y=120)

        self.x2 = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.x2.place(x=60, y=120)

        label = customtkinter.CTkLabel(master=izqFrame, text='y₂ =', width=40, height=28, font=("Roboto", 18, "bold"), fg_color='transparent')
        label.place(x=260, y=120)

        self.y2 = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.y2.place(x=300, y=120)

        button = customtkinter.CTkButton(master=izqFrame, text='Graficar', width=140, height=28, font=("Roboto", 18), command=self.button_eventBresen)
        button.place(x=300, y=170)
    
    def trazarBresenham(self, numx1, numy1, numx2, numy2):
        dx = abs(numx2 - numx1)
        dy = abs(numy2 - numy1)
    
        if numx1 < numx2:
            incX = 1
        else:
            incX = -1

        if numy1 < numy2:
            incY = 1
        else:
            incY = -1

        x = numx1
        y = numy1
        puntosbb = [(x, y)]

        if dx > dy:
            p = 2 * dy - dx
        for i in range(0, dx):
            if p >= 0:
                y += incY
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
            x += incX
            puntosbb.append((x, y))
        else:
            p = 2 * dx - dy
        for i in range(0, dy):
            if p >= 0:
                x += incX
                p += 2 * (dx - dy)
            else:
                p += 2 * dx
            y += incY
            puntosbb.append((x, y))

        return puntosbb, dx, dy


    
    def button_eventBresen(self): #funcion q obtiene los datos 
        from screens import Home
        numx1 = int(self.x1.get())
        numy1 = int(self.y1.get())
        numx2 = int(self.x2.get())
        numy2 = int(self.y2.get())

        puntosbb, dx, dy = self.trazarBresenham(numx1, numy1, numx2, numy2)

        # Crear la figura y el gráfico
        fig = Figure(figsize=(5, 4), dpi=100, facecolor='#222831')
        plot = fig.add_subplot(111)

        plot.set_facecolor('#222831')


        #frame izquierdo inferior con datos
        izqInf = customtkinter.CTkFrame(master=self, width=560, height=40, fg_color='transparent')
        izqInf.place(x=10, y=290)

        dxLabel = customtkinter.CTkLabel(master=izqInf, text='dx = '+ str(dx), width=40, height=28, font=("Roboto", 18, "bold"), fg_color='transparent')
        dxLabel.place(x=10, y=10)

        dyLabel = customtkinter.CTkLabel(master=izqInf, text='dy = '+ str(dy), width=40, height=28, font=("Roboto", 18, "bold"), fg_color='transparent')
        dyLabel.place(x=100, y=10)


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
        for punto in puntosbb:
            self.treeview.insert('', 'end', values=punto)

        # Dibujar la línea
        plot.plot(*zip(*puntosbb), marker='o', color='#FFD369')
        plot.set_title('Algoritmo de Bresenham para trazar una línea', color='white')
        plot.set_xlabel('X', color='white')
        plot.set_ylabel('Y', color='white')
        plot.grid(True, color='#FFFFFF')

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

    
