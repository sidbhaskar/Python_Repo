import sys
import pygame
pygame.init()

#Displau window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('This is suppose to be a game :)')

#Handling events
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 30))
    pygame.display.update()