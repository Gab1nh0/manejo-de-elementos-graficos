import matplotlib.pyplot as plt

def LineaBresenham(X1, Y1, X2, Y2):
    # 0 - Distancias que se desplazan en cada eje
    dY = Y2 - Y1
    dX = X2 - X1
    
    # 1 - Incrementos para las secciones con avance inclinado
    if dY >= 0:
        IncYi = 1
    else:
        dY = -dY
        IncYi = -1
    
    if dX >= 0:
        IncXi = 1
    else:
        dX = -dX
        IncXi = -1
    
    # 2 - Incrementos para las secciones con avance recto
    if dX >= dY:
        IncYr = 0
        IncXr = IncXi
    else:
        IncXr = 0
        IncYr = IncYi
    
        # Cuando dy es mayor que dx, se intercambian, para reutilizar el mismo bucle.
        # ver octantes blancos en la imagen encima del código
        k = dX
        dX = dY
        dY = k
    
    # 3 - Inicializar valores (y de error).
    X = X1
    Y = Y1
    avR = 2 * dY
    av = avR - dX
    avI = av - dX
    
    # Lista para almacenar las coordenadas de los puntos a graficar
    puntos = [(X, Y)]
    
    # 4 - Bucle para el trazado de las línea.
    while True:
        # Agregar coordenadas a la lista de puntos
        puntos.append((X, Y))
        
        if av >= 0:
            X += IncXi     # X aumenta en inclinado
            Y += IncYi     # Y aumenta en inclinado
            av += avI      # Avance Inclinado
        else:
            X += IncXr     # X aumenta en recto
            Y += IncYr     # Y aumenta en recto
            av += avR      # Avance Recto
        
        if X == X2 and Y == Y2:
            break
    
    # Extraer las coordenadas X e Y de la lista de puntos
    Xs, Ys = zip(*puntos)
    
    # Graficar la línea
    plt.plot(Xs, Ys, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linea de Bresenham')
    plt.grid(True)
    plt.show()

# Ejemplo de uso
LineaBresenham(1, -1, 11, -6)  # Llamada a la función con coordenadas de ejemplo
