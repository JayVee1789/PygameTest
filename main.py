import pygame

pygame.init()

#creer la fenetre de jeu

pygame.display.set_mode((800,600))
pygame.display.set_caption("pygame - test faisabilite")

#boucle de jeu
running = True

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()