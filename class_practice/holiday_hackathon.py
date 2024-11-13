import pygame, sys
from pygame.locals import QUIT

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reindeer Platform Jumper")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Reindeer properties
reindeer_width = 50
reindeer_height = 50
reindeer_x = WIDTH // 2 - reindeer_width // 2
reindeer_y = HEIGHT - reindeer_height - 10
reindeer_speed = 5
jump_speed = -15
gravity = 0.8

# Platform properties
platform_width = 100
platform_height = 20
platforms = [[WIDTH // 2 - platform_width // 2, HEIGHT - 100]]

# Game variables
score = 0
jump = False
y_velocity = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jump:
                jump = True
                y_velocity = jump_speed

    # Move reindeer
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and reindeer_x > 0:
        reindeer_x -= reindeer_speed
    if keys[pygame.K_RIGHT] and reindeer_x < WIDTH - reindeer_width:
        reindeer_x += reindeer_speed

    # Apply gravity
    if jump:
        reindeer_y += y_velocity
        y_velocity += gravity

    # Check platform collisions
    for platform in platforms:
        if (reindeer_y + reindeer_height >= platform[1] and 
            reindeer_y + reindeer_height <= platform[1] + platform_height and
            reindeer_x < platform[0] + platform_width and
            reindeer_x + reindeer_width > platform[0]):
            jump = False
            y_velocity = 0
            reindeer_y = platform[1] - reindeer_height

    # Move platforms down and create new ones
    if reindeer_y < HEIGHT // 2:
        reindeer_y += 5
        for platform in platforms:
            platform[1] += 5
        if platforms[-1][1] > 100:
            x = random.randint(0, WIDTH - platform_width)
            y = platforms[-1][1] - 200
            platforms.append([x, y])
            score += 1

    # Remove off-screen platforms
    while len(platforms) > 0 and platforms[0][1] > HEIGHT:
        platforms.pop(0)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (reindeer_x, reindeer_y, reindeer_width, reindeer_height))
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, (platform[0], platform[1], platform_width, platform_height))

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
