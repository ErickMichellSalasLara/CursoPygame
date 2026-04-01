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

pygame.mouse.set_visible(0) #false

while True: #Este es el bucle principal del juego, se ejecuta continuamente hasta que se cierre la ventana
    for event in pygame.event.get(): #Aqui se manejan los eventos del juego, como el cierre de la ventana
        if event.type == pygame.QUIT: #Si el evento es el cierre de la ventana
            sys.exit() #Se cierra el programa
            
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, GREEN, (x, y, 100, 100))
    
    pygame.display.flip()
    clock.tick(60)