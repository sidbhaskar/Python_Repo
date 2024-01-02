import pygame
# Initialize Pygame
pygame.init()
# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")
# Set ball properties
ball_color = (255, 0, 0) # Red
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_x_speed = 5
ball_y_speed = 5
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     # Update ball position
    ball_x += ball_x_speed
    ball_y += ball_y_speed
     # Bounce off walls
    if ball_x + ball_radius > screen_width or ball_x - ball_radius < 0:
        ball_x_speed = -ball_x_speed
    if ball_y + ball_radius > screen_height or ball_y - ball_radius < 0:
        ball_y_speed = -ball_y_speed
     # Clear screen
    screen.fill((0, 0, 0)) # Black background
     # Draw ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
     # Update display
    pygame.display.update()
# Quit Pygame
pygame.quit()
