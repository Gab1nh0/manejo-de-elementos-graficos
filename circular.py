import tkinter as tk
from tkinter import ttk
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


class Circular(tk.Frame):
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

        titulo = customtkinter.CTkLabel(master=izqFrame, text='Algoritmo de Punto Medio Circular', width=40, height=28, fg_color='transparent', font=("Roboto", 18))
        titulo.place(x=10, y=10)

        label = customtkinter.CTkLabel(master=izqFrame, text='Xc =', width=40, height=28, font=("Roboto", 18, "bold"), fg_color='transparent')
        label.place(x=10, y=70)

        self.xc = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent',)
        self.xc.place(x=60, y=70)
        self.xc.focus_set()

        label = customtkinter.CTkLabel(master=izqFrame, text='Yc =', width=40, height=28, font=("Roboto", 18,"bold"), fg_color='transparent')
        label.place(x=260, y=70)

        self.yc = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.yc.place(x=300, y=70)
        
        label = customtkinter.CTkLabel(master=izqFrame, text='r =', width=40, height=28, font=("Roboto", 18,"bold"), fg_color='transparent')
        label.place(x=10, y=120)

        self.r = customtkinter.CTkEntry(master=izqFrame, width=140, height=28, fg_color='transparent')
        self.r.place(x=60, y=120)

        button = customtkinter.CTkButton(master=izqFrame, text='Graficar', width=140, height=28, font=("Roboto", 18), command=self.button_eventPunto)
        button.place(x=300, y=120)

        button = customtkinter.CTkButton(master=izqFrame, text='Limpiar', width=140, height=28, font=("Roboto", 18), command=self.limpiar, fg_color="#CD3030", hover_color="#900000")
        button.place(x=300, y=150)

    def limpiar(self):
        self.x1.delete(0, tk.END)
        self.y1.delete(0, tk.END)
        self.x2.delete(0, tk.END)
        self.y2.delete(0, tk.END)

        #frame izquierdo inferior sin datos
        izqInf = customtkinter.CTkFrame(master=self, width=560, height=40, fg_color='transparent')
        izqInf.place(x=10, y=290)

        # Frame derecho sin grafica
        derFrame = customtkinter.CTkFrame(master=self, width=560, height=620, fg_color="#222831")
        derFrame.place(x=630, y=140)

        #frame sin tabla
        tablaFrame = customtkinter.CTkFrame(master=self, width=560, height=400, fg_color="#222831")
        tablaFrame.place(x=30, y=360)
    
    def trazarPuntomedio(self, xc, yc, r):
        
        pinicial = int(5/4) - r
        p = [pinicial]
        x = [0]
        y = [r]

        puntosx=[]
        puntosy=[]

        while x[-1] < y[-1]:
            if p[-1] < 0:
                x.append(x[-1] + 1)
                y.append(y[-1])
                p.append(p[-1] + (2 * x[-1]) + 1)
            else:
                x.append(x[-1] + 1)
                y.append(y[-1] - 1)
                p.append(p[-1] + (2 * x[-1]) + 1 - (2 * y[-1]))

            puntosx.append(xc+x[-1])
            puntosy.append(yc+y[-1])
            puntosx.append(xc+y[-1])
            puntosy.append(yc+x[-1])

            puntosx.append(xc+x[-1])
            puntosy.append(yc-y[-1])
            puntosx.append(xc+y[-1])
            puntosy.append(yc-x[-1])

            puntosx.append(xc-x[-1])
            puntosy.append(yc+y[-1])
            puntosx.append(xc-y[-1])
            puntosy.append(yc+x[-1])

            puntosx.append(xc-x[-1])
            puntosy.append(yc-y[-1])
            puntosx.append(xc-y[-1])
            puntosy.append(yc-x[-1])

            puntosx.append(xc-r)
            puntosy.append(yc)
            puntosx.append(xc+r)
            puntosy.append(yc)
            puntosx.append(xc)
            puntosy.append(yc+r)
            puntosx.append(xc)
            puntosy.append(yc-r)

        return puntosx, puntosy, x[-1], y[-1]
    

    def limpiar(self):
        self.x1.delete(0, tk.END)
        self.y1.delete(0, tk.END)
        self.x2.delete(0, tk.END)
        self.y2.delete(0, tk.END)

        #frame izquierdo inferior sin datos
        izqInf = customtkinter.CTkFrame(master=self, width=560, height=40, fg_color='transparent')
        izqInf.place(x=10, y=290)

        # Frame derecho sin grafica
        derFrame = customtkinter.CTkFrame(master=self, width=560, height=620, fg_color="#222831")
        derFrame.place(x=630, y=140)

        #frame sin tabla
        tablaFrame = customtkinter.CTkFrame(master=self, width=560, height=400, fg_color="#222831")
        tablaFrame.place(x=30, y=360)


    
    def button_eventPunto(self): 
        from screens import Home
        xc = int(self.xc.get())
        yc = int(self.yc.get())
        r = int(self.r.get())

        puntosx, puntosy, dx, dy = self.trazarPuntomedio(xc, yc, r)

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
        for i in range(len(puntosx)):
            self.treeview.insert('', 'end', values=(puntosx[i], puntosy[i]))

        # Dibujar la línea
        plot.plot(puntosx, puntosy, 'bo', color='#FFD369')
        plot.set_aspect('equal', adjustable='box')
        plot.set_xlabel('X', color='white')
        plot.set_ylabel('Y',color='white')
        plot.set_title('Punto medio', color='white')
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
