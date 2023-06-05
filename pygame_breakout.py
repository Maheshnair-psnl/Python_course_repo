import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the paddle
paddle_width = 100
paddle_height = 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 50
paddle_dx = 5

# Set up the ball
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-2, 2])
ball_dy = -2

# Set up bricks
brick_width = 80
brick_height = 20
num_bricks = 10
bricks = []
for i in range(num_bricks):
    brick_x = i * (brick_width + 10) + 35
    brick_y = 50
    bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_dx
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_dx

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Collisions with the walls
    if ball_x <= 0 or ball_x >= WIDTH - ball_radius:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    # Collision with the paddle
    if ball.colliderect(pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)):
        ball_dy *= -1

    # Collision with the bricks
    for brick in bricks:
        if ball.colliderect(brick):
            ball_dy *= -1
            bricks.remove(brick)
            break

    # Check if the ball falls below the paddle
    if ball_y >= HEIGHT:
        running = False

    # Clear the window
    win.fill(WHITE)

    # Draw the paddle, ball, and bricks
    pygame.draw.rect(win, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(win, RED, (ball_x, ball_y), ball_radius)
    for brick in bricks:
        pygame.draw.rect(win, BLUE, brick)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
