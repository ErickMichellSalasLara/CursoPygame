import pygame, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/imagenes/player.png").convert_alpha()
        self.rect = self.image.get_rect() # Posicionamiento del Sprite
        self.speed_x = 0 #Velocidad del jugador en el eje x
        self.speed_y = 0 #Velocidad del jugador en el eje y
        
    def changespeed(self, x):
        self.speed_x += x #Se cambia la velocidad del jugador en el eje x
        
    def update(self):
        self.rect.x += self.speed_x #Se actualiza la posición del jugador en el eje x
        player.rect.y = 510 #Se mantiene la posición del jugador en el eje y
        

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/imagenes/meteor.png").convert_alpha()
        self.rect = self.image.get_rect() # Posicionamiento del Sprite
    
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/imagenes/laser.png").convert_alpha()
        self.rect = self.image.get_rect() # Posicionamiento del Sprite
    
    def update(self):
        self.rect.y -= 5 #Entre más alto el número, más rápido va el láser

# Definir colores
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

pygame.init() #Aqui se inicializa la libreria de pygame
size = (900, 600) #Aqui se define el tamaño de la pantalla

clock = pygame.time.Clock() #Aqui se crea un reloj para controlar los frames por segundo
screen = pygame.display.set_mode(size) #Aqui se crea la ventana con el tamaño definido anteriormente

done = False 
score = 0

laser_list = pygame.sprite.Group() #Se crea una lista para almacenar los láseres
all_sprite_list = pygame.sprite.Group() #Se crea una lista para almacenar los sprites
meteor_list = pygame.sprite.Group() #Se crea una lista para almacenar los meteoros

for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(880) #Se posicionan en un lugar random
    meteor.rect.y = random.randrange(450) #Se posicionan en un

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player() #Se crea la instancia del jugador
all_sprite_list.add(player) #Añadir el jugador a la lista de sprites

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN: #Si se presiona una tecla
            if event.key == pygame.K_LEFT: #Si se presiona la flecha izquierda
                player.changespeed(-3) #Entra dentro del método changespeed y se cambia la velocidad del jugador a la izquierda
            if event.key == pygame.K_RIGHT: #Si se presiona la flecha derecha
                player.changespeed(3) #Entra dentro del método changespeed y se cambia la velocidad del jugador a la derecha
            if event.key == pygame.K_SPACE:
                laser = Laser() #Se crea una instancia del láser
                laser.rect.x = player.rect.x + 45 # Se posiciona el láser en la posición del jugador
                laser.rect.y = player.rect.y - 20# Se posiciona el láser en la posición del jugador
        
                all_sprite_list.add(laser) #Se añade el láser a la lista de sprites
                laser_list.add(laser) #Se añade el láser a la lista de láseres
        
        
        if event.type == pygame.KEYUP: #Si se suelta una tecla
            if event.key == pygame.K_LEFT: #Si se suelta la flecha izquierda
                # Se invierte el signo para que el jugador deje de moverse a la izquierda
                player.changespeed(3) #Entra dentro del método changespeed y se cambia la velocidad del jugador a la derecha
            if event.key == pygame.K_RIGHT: #Si se suelta la flecha derecha
                # Se invierte el signo para que el jugador deje de moverse a la derecha
                player.changespeed(-3) #Entra dentro del método changespeed y se cambia la velocidad del jugador a la izquierda
                
    all_sprite_list.update() #Aqui se actualizan los sprites, en este caso solo el jugador
            
    screen.fill(WHITE)
    all_sprite_list.draw(screen) #Aqui se dibujan todos los sprites en la pantalla
    
    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True) #Se detecta la colision entre el láser y los meteoros, y se borra el meteoro al colisionar   
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser) #Se borra el láser al colisionar
            laser_list.remove(laser) #Se borra el láser de la lista de láseres
            score += 1
            print(score)
        if laser.rect.y < -10: #Si el láser sale de la pantalla, se borra
            all_sprite_list.remove(laser) #Se borra el láser al salir de la pantalla
            laser_list.remove(laser) #Se borra el láser de la lista de láseres
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()