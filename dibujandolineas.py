import pygame, sys

# Definir colores
BLACK = (0, 0, 0) #Negro
WHITE = (255, 255, 255) #Blanco
RED = (255, 0, 0) #Rojo
GREEN = (0, 255, 0) #Verde
BLUE = (0, 0, 255) #Azul

pygame.init() #Aqui se inicializa la libreria de pygame

'''Una tupla es una estructura de datos que se utiliza para almacenar una colección de elementos.
A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.'''
        # x   y
size = (700, 500) #Aqui se define el tamaño de la pantalla

''' Creamos ventana '''
screen = pygame.display.set_mode(size) #Aqui se crea la ventana con el tamaño definido anteriormente

while True: #Este es el bucle principal del juego, se ejecuta continuamente hasta que se cierre la ventana
    for event in pygame.event.get(): #Aqui se manejan los eventos del juego, como el cierre de la ventana
        if event.type == pygame.QUIT: #Si el evento es el cierre de la ventana
            sys.exit() #Se cierra el programa
            
    # Pintamos el fondo de la pantalla de blanco
    screen.fill(WHITE) #Aqui se pinta el fondo de la pantalla de blanco
    ''' Zona donde se dibujara '''
    pygame.draw.line(screen, RED, (0, 0), (700, 500), 5) #Aqui se dibuja una linea roja desde la esquina superior izquierda hasta la esquina inferior derecha con un grosor de 5
    pygame.draw.rect(screen, BLUE, (50, 50, 200, 100), 5) #Aqui se dibuja un rectangulo azul con un grosor de 5 en la posicion (50, 50) con un ancho de 200 y una altura de 100
    pygame.draw.circle(screen, GREEN, (350, 250), 50, 5) #Aqui se dibuja un circulo verde con un grosor de 5 en la posicion (350, 250) con un radio de 50
    pygame.draw.arc(screen, BLACK, (200, 400, 200, 100), 0, 3.14, 5) #Aqui se dibuja un arco
    pygame.draw.ellipse(screen, BLACK, (400, 50, 200, 100), 5) #Aqui se dibuja una elipse negra con un grosor de 5 en la posicion (400, 50) con un ancho de 200 y una altura de 100
    ''' Fin de la zona donde se dibujara '''
    # Actualizamos la pantalla
    pygame.display.flip() #Aqui se actualiza la pantalla para mostrar los cambios realizados