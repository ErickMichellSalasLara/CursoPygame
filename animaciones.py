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
size = (720, 500) #Aqui se define el tamaño de la pantalla

''' Creamos ventana '''
screen = pygame.display.set_mode(size) #Aqui se crea la ventana con el tamaño definido anteriormente

# Controlar los frames por segundo
clock = pygame.time.Clock() #Aqui se crea un reloj para controlar los frames por segundo

# Coordenadas del cuadrado
cord_x = 400 # Posicion inicial en el eje x
cord_y = 200 # Posicion inicial en el eje y

# Velocidad a la que se movera el cuadrado
speed_x = 3 #pixeles
speed_y = 3 #pixeles

while True: #Este es el bucle principal del juego, se ejecuta continuamente hasta que se cierre la ventana
    for event in pygame.event.get(): #Aqui se manejan los eventos del juego, como el cierre de la ventana
        if event.type == pygame.QUIT: #Si el evento es el cierre de la ventana
            sys.exit() #Se cierra el programa
    
            
    ''' Logica '''
    if (cord_x > 640 or cord_x < 0):
        speed_x *= -1 #Si el cuadrado llega al borde de la pantalla, se invierte la dirección del movimiento
    if (cord_y > 430 or cord_y < 0):
        speed_y *= -1 #Si el cuadrado llega al borde de la pantalla, se invierte la dirección del movimiento

    cord_x += speed_x
    cord_y += speed_y
    ''' Logica'''
    
    # Pintamos el fondo de la pantalla de blanco
    screen.fill(BLACK) #Aqui se pinta el fondo de la pantalla de blanco
    
    ''' Zona donde se dibujara '''
                                # x     y
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
    pygame.draw.circle(screen, GREEN, (cord_x, cord_y), 40)
    
    ''' Fin de la zona donde se dibujara '''
    # Actualizamos la pantalla
    pygame.display.flip() #Aqui se actualiza la pantalla para mostrar los cambios realizados
    clock.tick(60) #Se limita a 60 fps