import pygame

screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()

done = False

background = pygame.image.load("imagenes/fondo.png").convert()
player = pygame.image.load("imagenes/player.jpg").convert()

 # Si utilizas el método .convert_alpha() en una imagen PNG, se muestra la transparencia sin problemas, no necesitas usar el color_key.

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
   
	mouse_pos = pygame.mouse.get_pos()
	x = mouse_pos[0]
	y = mouse_pos[1]
 
	screen.blit(background, [-400, 0])
	screen.blit(player, [x, y])
 
	pygame.display.flip()
	clock.tick(60)
 
pygame.quit()