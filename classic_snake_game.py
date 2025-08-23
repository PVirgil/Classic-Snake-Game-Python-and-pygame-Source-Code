import pygame
import time
import random

pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))

# Colors
white, black, red, green = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
speed = 15

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = 'UP'
            elif event.key == pygame.K_DOWN: change_to = 'DOWN'
            elif event.key == pygame.K_LEFT: change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT: change_to = 'RIGHT'

    # Update direction
    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'

    # Update snake position
    if direction == 'UP': snake_pos[1] -= 10
    if direction == 'DOWN': snake_pos[1] += 10
    if direction == 'LEFT': snake_pos[0] -= 10
    if direction == 'RIGHT': snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    snake_body.pop()

    # Draw
    screen.fill(black)
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], 10, 10))
    pygame.display.flip()
    clock.tick(speed)

