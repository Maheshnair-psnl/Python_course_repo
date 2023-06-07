# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
import random

# Constants
WIDTH = 600
HEIGHT = 400
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 20
ALIEN_SIZE = 20
BULLET_SIZE = 5
MAX_ALIENS = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load images
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
alien_image = pygame.image.load("alien.png")
alien_image = pygame.transform.scale(alien_image, (ALIEN_SIZE, ALIEN_SIZE))

# Game state
player_pos = (WIDTH - PLAYER_WIDTH) // 2
bullets = []
aliens = []

# Initialize aliens
for _ in range(MAX_ALIENS):
    aliens.append([random.randint(0, WIDTH - ALIEN_SIZE), random.randint(0, HEIGHT // 2)])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos = max(0, player_pos - 5)
            elif event.key == pygame.K_RIGHT:
                player_pos = min(WIDTH - PLAYER_WIDTH, player_pos + 5)
            elif event.key == pygame.K_SPACE:
                bullets.append([player_pos + (PLAYER_WIDTH - BULLET_SIZE) // 2, HEIGHT - PLAYER_HEIGHT])

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player
    screen.blit(player_image, (player_pos, HEIGHT - PLAYER_HEIGHT))

    # Draw the bullets
    new_bullets = []
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], BULLET_SIZE, BULLET_SIZE))
        bullet[1] -= 5
        if bullet[1] > -BULLET_SIZE:
            new_bullets.append(bullet)
    bullets = new_bullets

    # Draw the aliens
    for alien in aliens:
        screen.blit(alien_image, (alien[0], alien[1]))
        alien[1] += 1
        if alien[1] > HEIGHT:
            alien[0] = random.randint(0, WIDTH - ALIEN_SIZE)
            alien[1] = random.randint(-HEIGHT, -ALIEN_SIZE)

    # Check for collision
    for bullet in bullets:
        for alien in aliens:
            if bullet[1] < alien[1] + ALIEN_SIZE and \
                    bullet[1] + BULLET_SIZE > alien[1] and \
                    bullet[0] < alien[0] + ALIEN_SIZE and \
                    bullet[0] + BULLET_SIZE > alien[0]:
                aliens.remove(alien)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
