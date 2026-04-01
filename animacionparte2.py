import pygame, sys, random
pygame.init()

#Definimos colores

white = (255, 255, 255)
red = (255, 0, 0)

size = (800, 500) #Tupla / Encapsulamiento
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_list = []
for i in range(60):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coor_list.append([x,y])
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    #Pintamos la pantalla de algun color
    screen.fill(white)
    
    # Efecto de lluvia, recorremos la lista de coordenadas y dibujamos un circulo en cada coordenada
    # luego aumentamos la coordenada y en 1 para simular el movimiento de la lluvia,
    # si la coordenada y es mayor a 500, entonces reiniciamos la coordenada y a 0 y le asignamos una nueva coordenada x aleatoria
    for coord in coor_list:
        pygame.draw.circle(screen, red, coord, 4)
        coord[1] += 1
        if coord[1] > 500: # Si la coordenada y es mayor a 500, entonces reiniciamos la coordenada y a 0 y le asignamos una nueva coordenada x aleatoria
            coord[0] = random.randint(0,800)
            coord[1] = 0
        
    pygame.display.flip() #Actualizar la pantalla IMPORTANTE
    clock.tick(60)