# Importa la biblioteca pygame
import pygame

# Inicia los módulos de pygame
pygame.init()

# Colores de fondo RGB
BLUE  = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Abre la ventana
window = pygame.display.set_mode((400, 500))

# Establece el título de la ventana
pygame.display.set_caption("Mi primera ventana en PyGame")

# Establece un color de fondo para la ventana
window.fill(RED)
pygame.display.flip()

# Crea un valor booleano 
run = True

# Revisa los eventos del juego 
while run:
     
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

