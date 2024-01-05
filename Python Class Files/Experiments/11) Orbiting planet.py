import pygame
import math
import sys

width, height = 800, 600
center_x, center_y = width // 2, height // 2

major_radius = 200
minor_radius = 100

black = (0, 0, 0)
white = (255, 255, 255)

speed = 1
theta = 0

def get_elliptical_point(theta):
    x = major_radius * math.cos(theta)
    y = minor_radius * math.sin(theta)
    return x, y

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Planet Wali game ^^')

planet_radius = 10
planet = pygame.draw.circle(screen, white, (center_x, center_y), planet_radius)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    theta += speed
    x, y = get_elliptical_point(theta)
    planet_x, planet_y = center_x + x, center_y + y
    screen.fill(black)
    planet = pygame.draw.circle(screen, white, (round(planet_x), round(planet_y)), planet_radius)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
