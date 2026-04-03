import pygame, random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.display.set_caption("Juego de Meteoritos") #Titulo de la ventana del juego

class Meteor(pygame.sprite.Sprite): #Se crea la clase de la moneda, usando una subclase de Sprite
    def __init__(self): #Iniciamos la clase y la super clase
        super().__init__()
        self.image = pygame.image.load("Pygame/imagenes/meteor.png").convert_alpha() #Se carga la imagen
        self.rect =  self.image.get_rect() # Posicionamiento del Sprite
        # Creamos un encapsulamiento del movimiento de la moneda, para que el codigo sea mas ordenado y limpio
        # Este encapsulamiento hace que la moneda se mueva hacia abajo, simulando que esta cayendo
    def update(self):
        self.rect.y += 1
        
        if self.rect.y > SCREEN_HEIGHT: #Si la moneda sale de la pantalla, se vuelve a posicionar en un lugar random arriba de la pantalla
            self.rect.y = -20
            self.rect.x = random.randrange(SCREEN_WIDTH)
            
        
class Player(pygame.sprite.Sprite):
    def __init__(self): #Iniciamos la clase y la super clase
        super().__init__()
        self.image = pygame.image.load("Pygame/imagenes/player.png").convert_alpha() #Se carga la imagen
        self.rect =  self.image.get_rect() # Posicionamiento del Sprite
        # Creamos un encapsulamiento del movimiento del jugador, para que el codigo sea mas ordenado y limpio
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

class Game(object):
    def __init__(self):
        self.game_over = False
        self.score = 0
        
        self.meteor_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()
        
        for i in range(50):
            meteorito = Meteor() #Se crean 50 instancias de meteoros
            meteorito.rect.x = random.randrange(SCREEN_WIDTH) #Se posicionan en un lugar random
            meteorito.rect.y = random.randrange(SCREEN_HEIGHT)
    
            self.meteor_list.add(meteorito)
            self.all_sprite_list.add(meteorito)
            
        self.player = Player() #Se crea la variable del jugador y se iguala a la clase, la cual contiene las bases del jugador
        self.all_sprite_list.add(self.player) #Se añade el jugador a la lsta de todoos los sprites
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__() #Si el juego se ha terminado, se reinicia el juego al hacer click con el mouse
        return False
    
    def run_logic(self):
        # Si el juego no se ha terminado, se ejecuta la logica del juego, que es actualizar los sprites y detectar las colisiones entre el jugador y los meteoros
        if not self.game_over:
            self.all_sprite_list.update() #Llamamos al metodo update de todos los sprites

            self.meteorito_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True) #Se detecta la colision entre el jugador y los meteoros, y se borra el meteorito al colisionar
        
            for meteorito in self.meteorito_hit_list:
                self.score += 1
                print(self.score)
            
            if len(self.meteor_list) == 0: #Si no quedan meteoros, se termina el juego
                self.game_over = True
                
    def display_frame(self, screen):
        screen.fill(WHITE)
        # Ponemos texto en pantalla, para mostrar el score y el mensaje de game over
        
        if self.game_over:
            font = pygame.font.SysFont("Arial", 25)
            # El mensaje de game over se muestra en pantalla, junto con el score final del jugador
            # True es para que el texto se vea suave, False es para que se vea pixelado
            text = font.render("Game Over!. Click to continue. Score: " + str(self.score), True, BLACK)
            # El texto se centra en la pantalla, restando la mitad del ancho del texto al centro de la pantalla, y lo mismo con la altura del texto, para que quede perfectamente centrado
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            # El texto se dibuja en pantalla, en la posicion calculada anteriormente
            # Se manda a llamar la variable text, y se pone la posicion la cual es una tupla con las coordenadas x e y, para que el texto se dibuje en esa posicion
            screen.blit(text, [center_x, center_y])
            
        if not self.game_over:
            self.all_sprite_list.draw(screen) #Con un solo metodo ya se puede llegar a crear todo
        
        pygame.display.flip()

def main(): # Funcion principal del juego, donde se ejecuta el bucle del juego
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego de Meteoritos")
    
    done = False
    clock = pygame.time.Clock()
    
    game = Game() #Se crea una instancia de la clase Game, para poder acceder a sus metodos y atributos
    
    while not done:
        done = game.process_events() #Se llama a los metodos de la clase Game para procesar los eventos y ejecutar la logica del juego
        game.run_logic() #Se llama a los metodos de la clase Game para procesar los eventos y ejecutar la logica del juego
        game.display_frame(screen) #Se llama a los metodos de la clase Game para procesar los eventos, ejecutar la logica del juego y mostrar el frame en pantalla
        clock.tick(60)
    pygame.quit()

# El if servira solamente para ejecutar la funcion main, y no ejecutar el codigo si se importa este archivo como un modulo
if __name__ == "__main__":
    main()

