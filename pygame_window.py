# Importa la biblioteca pygame
import pygame

# Inicia los módulos de pygame
pygame.init()

# Abre la ventana
pygame.display.set_mode((400, 500))

# Establece el título de la ventana
pygame.display.set_caption("Mi primera ventana en PyGame")

# Crea un valor booleano 
run = True

# Revisa los eventos del juego 
while run:
     
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

