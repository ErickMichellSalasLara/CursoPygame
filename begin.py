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

size = (700, 500) #Aqui se define el tamaño de la pantalla

''' Creamos ventana '''
screen = pygame.display.set_mode(size) #Aqui se crea la ventana con el tamaño definido anteriormente

while True: #Este es el bucle principal del juego, se ejecuta continuamente hasta que se cierre la ventana
    for event in pygame.event.get(): #Aqui se manejan los eventos del juego, como el cierre de la ventana
        if event.type == pygame.QUIT: #Si el evento es el cierre de la ventana
            sys.exit() #Se cierra el programa