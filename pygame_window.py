# Importa la biblioteca pygame
import pygame

# Inicia los módulos de pygame
pygame.init()

# Colores de fondo RGB
BLUE  = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

# En Hexadecimal
OLD_ROSE = "#B47978"
ENGLISH_VIOLET = "#44344F"
CORAL = "#FF8552"

# Basic colors
WHITE = "white"
YELLOW = "yellow"
GRAY = "gray"

# Abre la ventana
window = pygame.display.set_mode((400, 500))

# Establece el título de la ventana
pygame.display.set_caption("Mi primera ventana en PyGame")

# Establece un color de fondo para la ventana
window.fill(CORAL)
pygame.display.flip()

# Establece un icono para la ventana
icono = pygame.image.load("Figura-2-Stumble-Guys-PNG-660x1024.png")
pygame.display.set_icon(icono)

# Crea un valor booleano 
run = True

# Revisa los eventos del juego 
while run:
     
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

