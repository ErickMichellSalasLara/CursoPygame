import pygame, random

WHITE = (255,255,255)
BLACK = (0,0,0)

class Meteor(pygame.sprite.Sprite): #Se crea la clase de la moneda, usando una subclase de Sprite
    def __init__(self): #Iniciamos la clase y la super clase
        super().__init__()
        self.image = pygame.image.load("imagenes/meteor.png").convert_alpha() #Se carga la imagen
        self.rect =  self.image.get_rect() # Posicionamiento del Sprite
        # Creamos un encapsulamiento del movimiento de la moneda, para que el codigo sea mas ordenado y limpio
        # Este encapsulamiento hace que la moneda se mueva hacia abajo, simulando que esta cayendo
    def update(self):
        self.rect.y += 1 
        
        if self.rect.y > 600: #Si la moneda sale de la pantalla, se vuelve a posicionar en un lugar random arriba de la pantalla
            self.rect.y = -20
            self.rect.x = random.randrange(900)
            
        
class Player(pygame.sprite.Sprite):
    def __init__(self): #Iniciamos la clase y la super clase
        super().__init__()
        self.image = pygame.image.load("imagenes/player.png").convert_alpha() #Se carga la imagen
        self.rect =  self.image.get_rect() # Posicionamiento del Sprite
        # Creamos un encapsulamiento del movimiento del jugador, para que el codigo sea mas ordenado y limpio
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]


pygame.init()

pygame.display.set_caption("Monedas cayendo") #Nombre de la ventana
screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()

done = False

background = pygame.image.load("imagenes/background.png").convert()

score = 0

''' Estas listas almacenan todos los Sprites que se creen '''
all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()

for i in range(50):
    meteorito = Meteor() #Se crean 50 instancias de Moneda
    meteorito.rect.x = random.randrange(900) #Se posicionan en un lugar random
    meteorito.rect.y = random.randrange(600)
    
    meteor_list.add(meteorito)
    all_sprite_list.add(meteorito)
    
player = Player() #Se crea la variable del jugador y se iguala a la clase, la cual contiene las bases del jugador
all_sprite_list.add(player) #Se añade el jugador a la lsta de todoos los sprites

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.update() #Llamamos al metodo update de todos los sprites  

    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True) #Se detecta la colision entre el jugador y los meteoros, y se borra el meteorito al colisionar
    
    for meteorito in meteor_hit_list:
        score += 1
        print(score)
        
    screen.fill(WHITE)
 
    all_sprite_list.draw(screen) #Con un solo metodo ya se puede llegar a crear todo
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()