import pygame, random

WHITE = (255,255,255)
BLACK = (0,0,0)

class Moneda(pygame.sprite.Sprite): #Se crea la clase de la moneda, usando una subclase de Sprite
    def __init__(self): #Iniciamos la clase y la super clase
        super().__init__()
        self.image = pygame.image.load("imagenes/moneda.png").convert_alpha() #Se carga la imagen
        self.rect =  self.image.get_rect() # Posicionamiento del Sprite

class Player(pygame.sprite.Sprite):
    def __init__(self): #Iniciamos la clase y la super clase
        super().__init__()
        self.image = pygame.image.load("imagenes/player.png").convert_alpha() #Se carga la imagen
        self.rect =  self.image.get_rect() # Posicionamiento del Sprite


pygame.init()

pygame.display.set_caption("Sprites")
screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()

done = False
score = 0

''' Estas listas almacenan todos los Sprites que se creen '''
all_sprite_list = pygame.sprite.Group()
moneda_list = pygame.sprite.Group()

for i in range(50):
    moneda = Moneda() #Se crean 50 instancias de Moneda
    moneda.rect.x = random.randrange(720) #Se posicionan en un lugar random
    moneda.rect.y = random.randrange(600)
    
    moneda_list.add(moneda)
    all_sprite_list.add(moneda)
    
player = Player() #Se crea la variable del jugador y se iguala a la clase, la cual contiene las bases del jugador
all_sprite_list.add(player) #Se añade el jugador a la lsta de todoos los sprites

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]
 
    moneda_hit_list = pygame.sprite.spritecollide(player, moneda_list, True) #Se detecta la colision entre el jugador y las monedas, y se borra la moneda al colisionar
    
    for moneda in moneda_hit_list:
        score += 1
        print(score)
        
    screen.fill(WHITE)
 
    all_sprite_list.draw(screen) #Con un solo metodo ya se puede llegar a crear todo
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()