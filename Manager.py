#tkinder para la interfaz
import tkinter as tk
from screens import Home, Dda, Bresen, Circular



class Manager(tk.Tk):
    def  __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.title("Computacion Grafica y Visual - Proyecto 1")
        container = tk.Frame(self) #container va a ser el contenerdor de todos los frames Home, dda, circular, elipse, berman
        
        container.pack(         #el .pack es pa decirle al conteiner donde va a estar ubicado
            side   =  tk.TOP,   #top pa ponerlo arriba del todo
            fill   =  tk.BOTH,  #both pa que ocupe de derecha a izquierda
            expand =  True      #expand pa q se expanda de derecha a izquierda
        )

        container.configure(background="#222831")
        container.grid_columnconfigure(0, weight=1)  #esto es para poner el container en la primera columna osea el primero a la izquierda
        container.grid_rowconfigure(0, weight=1)     #esto es pa lo mismo na ma q pa la primera fila, asi nos queda un cuadrao grande


        self.frame = {}
        for F in (Home, Dda, Bresen, Circular):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise() #manda el frame delante de todo