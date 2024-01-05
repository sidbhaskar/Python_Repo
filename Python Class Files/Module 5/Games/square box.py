import pygame

width, height = 800,600
black = (0,0,0)
white = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Square Box')

square_x = width//2
square_y = height//2
square_width = 50
square_height = 50


running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                square_x += 5
            elif event.key == pygame.K_LEFT:
                square_x -= 5
            elif event.key == pygame.K_UP:
                square_y -= 5
            elif event.key == pygame.K_DOWN:
                square_y += 5

    screen.fill(black)
    pygame.draw.rect(screen , white , (square_x,square_y,square_width,square_height))
    pygame.display.flip()

pygame.quit()
