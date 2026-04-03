import pygame, sys

# Definir colores
BLACK = (0, 0, 0) #Negro
WHITE = (255, 255, 255) #Blanco
CYAN = (0, 255, 255) #Cian
RED = (255, 0, 0) #Rojo

pygame.init() #Aqui se inicializa la libreria de pygame

size = (700, 500) #Aqui se define el tamaño de la pantalla
clock = pygame.time.Clock() #Definimos los ticks (FPS)
screen = pygame.display.set_mode(size) #Aqui se crea la ventana con el tamaño definido anteriormente

game_over = False #Variable para controlar el estado del juego

''' Constantes del jugador '''
player_height = 100
player_weight = 20

''' Coordenadas y Velocidad del jugador 1'''
coord_x_player = 10
coord_y_player = 10
y_speed_player = 0

''' Coordenadas y Velocidad del jugador 2'''
coord_x_player2 = 770 - player_height
coord_y_player2 = 300 - player_weight // 2
y_speed_player2 = 0

''' Coordenadas de la pelota'''
pelota_x = 350
pelota_y = 240
pelota_speed_x = 3
pelota_speed_y = 3

pygame.time.delay(1000) # Se hace una pausa de 1 segundo para poder iniciar el juego con tranquilidad

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            game_over = True   
        
        # Eventos Teclados
        if event.type == pygame.KEYDOWN: #Cuando se presiona una tecla
            # Jugador 1
            if event.key == pygame.K_w:
                y_speed_player = -3 # Negativo == arriba
            if event.key == pygame.K_s:
                y_speed_player = 3 # Positivo == abajo
                
            # Jugador 2
            if event.key == pygame.K_UP:
                y_speed_player2 = -3 # Negativo == arriba
            if event.key == pygame.K_DOWN:
                y_speed_player2 = 3 # Positivo == abajo
                
        if event.type == pygame.KEYUP: #Cuando se suelta una tecla
            #Jugador 1
            if event.key == pygame.K_w:
                y_speed_player = 0 #Aqui se asigna 0 al cuadrado para que se detenga cuando se suelta la tecla arriba
            if event.key == pygame.K_s:
                y_speed_player = 0 #Aqui se asigna 0 al cuadrado para que se detenga cuando se suelta la tecla abajo
            
            # Jugador 2
            if event.key == pygame.K_UP:
                y_speed_player2 = 0 #Aqui se asigna 0 al cuadrado para que se detenga cuando se suelta la tecla arriba
            if event.key == pygame.K_DOWN:
                y_speed_player2 = 0 #Aqui se asigna 0 al cuadrado para que se detenga cuando se suelta la tecla abajo

    if pelota_y > 490 or pelota_y < 10: #Si la pelota toca el borde superior o inferior del campo de juego
        pelota_speed_y *= -1 #Aqui se invierte la velocidad de la pelota en el eje y para que rebote

    # Revisa si la pelota sale del campo de juego por la izquierda o derecha
    if pelota_x > 690 or pelota_x < 10:
        pelota_x = 350
        pelota_y = 240
        pelota_speed_x *= -1 #Aqui se invierte la velocidad de la pelota en el
        pelota_speed_y *= -1 #Aqui se invierte la velocidad de la pelota en el eje y para que rebote
        
    # Modifica las coordenadas para dar mov. a los jugadores / pelota
    coord_y_player += y_speed_player #Aqui se actualiza la coordenada y del cuadrado sumando la velocidad
    coord_y_player2 += y_speed_player2 #Aqui se actualiza la coordenada y del cuadrado sumando la velocidad
    # Movimiento de la pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y
    
    # Gano?
    if pelota_x < 10:
        print("Gano el jugador 2")
        pygame.time.delay(1000) #Aqui se hace una pausa de 1 segundo antes de mostrar el mensaje de ganador
        game_over = True
    if pelota_x > 690:
        print("Gano el jugador 1")
        pygame.time.delay(1000) #Aqui se hace una pausa de 1 segundo antes de mostrar el mensaje de ganador
        game_over = True
    
    screen.fill(BLACK)
    
    # Dibujamos los rectangulos
    jugador1 = pygame.draw.rect(screen, CYAN, (coord_x_player, coord_y_player, player_weight, player_height))
    jugador2 = pygame.draw.rect(screen, WHITE, (coord_x_player2, coord_y_player2, player_weight, player_height))
    
    ''' Zona de campo de juego'''
    
    # Dibujamos la linea del medio del juego y la lineas que bordean el campo de juego
    pygame.draw.line(screen, WHITE, (350, 0), (350, 500), 4) # x1 / y1 / x2 / y2 / grosor
    #lina superior del campo de juego
    pygame.draw.line(screen, WHITE, (2, 2), (698, 2), 4) # x1 / y1 / x2 / y2 / grosor
    #lina inferior del campo de juego
    pygame.draw.line(screen, WHITE, (5, 495), (695, 495), 4) # x1 / y1 / x2 / y2 / grosor
    
    # Circulo del medio del juego
                                    # x / y / radio / grosor
    pygame.draw.circle(screen, WHITE, (350, 240), 50, 4) 
    
    ''' Zona de campo de juego'''
    
    ''' Pelota '''
    
    pelota = pygame.draw.circle(screen, RED, (pelota_x, pelota_y), 10) # x / y / radio / grosor
    
    ''' Pelota '''
    
        # Revisa si la pelota colisiona con el jugador 1 o jugador 2
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1 #Aqui se invierte la velocidad de la pelota en el eje x para que rebote
        
    pygame.display.flip()
    clock.tick(60) #Dejamos los ticks en 60 fps
