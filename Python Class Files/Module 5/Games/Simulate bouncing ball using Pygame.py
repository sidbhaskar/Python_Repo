import pygame

height = 600
width = 800

ball_radius = 10
ball_color = (255,255,255)

ball_x = width//2
ball_y = height//2

ball_velocity_x = 500
ball_velocity_y = 500

background_color = (0,0,0)
bounce_factor = 1

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Simulate bouncing ball using Pygame')

clock = pygame.time.Clock()


running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT  :
            running = False
    delta_time = clock.tick(60)
    ball_x += ball_velocity_x * delta_time / 1000
    ball_y += ball_velocity_y * delta_time / 1000
    if ball_x < ball_radius or ball_x > width - ball_radius:
        ball_velocity_x *= -bounce_factor
    if ball_y < ball_radius or ball_y > height - ball_radius:
        ball_velocity_y *= -bounce_factor

    screen.fill(background_color)
    pygame.draw.circle(screen,ball_color, (ball_x,ball_y),ball_radius )
    pygame.display.flip()

pygame.quit()

