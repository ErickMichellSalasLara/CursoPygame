import pygame, sys
pygame.init() #Aqui se inicializa la libreria de pygame

# Definir colores
BLACK = (0, 0, 0) #Negro
WHITE = (255, 255, 255) #Blanco
RED = (255, 0, 0) #Rojo
GREEN = (0, 255, 0) #Verde
BLUE = (0, 0, 255) #Azul

size = (800, 500) #Aqui se define el tamaño de la pantalla
clock = pygame.time.Clock() #Aqui se crea un reloj para controlar la velocidad del juego
screen = pygame.display.set_mode(size) #Aqui se crea la ventana con el tamaño definido anteriormente

# Coordenadas del cuadrado
coord_x = 300
coord_y = 300

#Velocidad del cuadrado
x_speed = 0
y_speed = 0



while True: #Este es el bucle principal del juego, se ejecuta continuamente hasta que se cierre la ventana
    for event in pygame.event.get(): #Aqui se manejan los eventos del juego, como el cierre de la ventana
        if event.type == pygame.QUIT: #Si el evento es el cierre de la ventana
            sys.exit() #Se cierra el programa
    
    # Eventos Teclados
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -3 #Aqui se asigna una velocidad negativa al cuadrado para que se mueva hacia la izquierda
            if event.key == pygame.K_d:
                x_speed = 3 #Aqui se asigna una velocidad positiva al cuadrado para que se mueva hacia la derecha
            if event.key == pygame.K_w:
                y_speed = -3 #Aqui se asigna una velocidad negativa al cuadrado para que se mueva hacia arriba
            if event.key == pygame.K_s:
                y_speed = 3 #Aqui se asigna una velocidad positiva al cuadrado para que se mueva hacia abajo
                
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_speed = 0 #Aqui se asigna una velocidad de 0 al cuadrado para que se detenga cuando se suelta la tecla izquierda
            if event.key == pygame.K_d:
                x_speed = 0 #Aqui se asigna una velocidad de 0 al cuadrado para que se detenga cuando se suelta la tecla derecha
            if event.key == pygame.K_w:
                y_speed = 0 #Aqui se asigna una velocidad de 0 al cuadrado para que se detenga cuando se suelta la tecla arriba
            if event.key == pygame.K_s:
                y_speed = 0 #Aqui se asigna una velocidad de 0 al cuadrado para que se detenga cuando se suelta la tecla abajo
        
    screen.fill(WHITE)
    
    coord_x += x_speed #Aqui se actualiza la coordenada x del cuadrado sumando la velocidad
    coord_y += y_speed #Aqui se actualiza la coordenada y del cuadrado sumando la velocidad

    pygame.draw.rect(screen, GREEN, (coord_x, coord_y, 100, 100))

    pygame.display.flip()
    clock.tick(60)