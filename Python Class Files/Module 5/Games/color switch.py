import pygame

width, height = 800, 600
black = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Color Switcher')

square_size = 100
square_margin = 50

square_x1, square_y1 = square_margin, square_margin
square_x2, square_y2 = square_margin + square_size + square_margin, square_margin
square_x3, square_y3 = square_margin, square_margin + square_size + square_margin
square_x4, square_y4 = square_margin + square_size + square_margin, square_margin + square_size + square_margin

current_color = black

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if square_x1 <= x <= square_x1 + square_size and square_y1 <= y <= square_y1 + square_size:
                current_color = COLORS[0]
            elif square_x2 <= x <= square_x2 + square_size and square_y2 <= y <= square_y2 + square_size:
                current_color = COLORS[1]
            elif square_x3 <= x <= square_x3 + square_size and square_y3 <= y <= square_y3 + square_size:
                current_color = COLORS[2]
            elif square_x4 <= x <= square_x4 + square_size and square_y4 <= y <= square_y4 + square_size:
                current_color = COLORS[3]

    screen.fill(current_color)

    pygame.draw.rect(screen, COLORS[0], (square_x1, square_y1, square_size, square_size))
    pygame.draw.rect(screen, COLORS[1], (square_x2, square_y2, square_size, square_size))
    pygame.draw.rect(screen, COLORS[2], (square_x3, square_y3, square_size, square_size))
    pygame.draw.rect(screen, COLORS[3], (square_x4, square_y4, square_size, square_size))

    pygame.display.flip()

pygame.quit()

