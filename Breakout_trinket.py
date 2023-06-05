from tkinter import *
import random
import time

# Set up the game window
WIDTH = 800
HEIGHT = 600

win = Tk()
win.title("Breakout Game")
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# Set up colors
WHITE = "#ffffff"
BLUE = "#0000ff"
RED = "#ff0000"

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
    bricks.append(canvas.create_rectangle(brick_x, brick_y, brick_x + brick_width, brick_y + brick_height, fill=BLUE))

# Set up the paddle
paddle = canvas.create_rectangle(paddle_x, paddle_y, paddle_x + paddle_width, paddle_y + paddle_height, fill=BLUE)

# Set up the ball
ball = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius, ball_y + ball_radius, fill=RED)

# Function to move the paddle
def move_paddle(event):
    if event.keysym == "Left" and paddle_x > 0:
        canvas.move(paddle, -paddle_dx, 0)
    if event.keysym == "Right" and paddle_x < WIDTH - paddle_width:
        canvas.move(paddle, paddle_dx, 0)

# Bind the arrow keys to move the paddle
canvas.bind_all("<KeyPress-Left>", move_paddle)
canvas.bind_all("<KeyPress-Right>", move_paddle)

# Game loop
running = True
while running:
    # Move the ball
    canvas.move(ball, ball_dx, ball_dy)
    ball_coords = canvas.coords(ball)

    # Collisions with the walls
    if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
        ball_dx *= -1
    if ball_coords[1] <= 0:
        ball_dy *= -1

    # Collision with the paddle
    paddle_coords = canvas.coords(paddle)
    if ball_coords[3] >= paddle_coords[1] and ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2]:
        ball_dy *= -1

    # Collision with the bricks
    for brick in bricks:
        brick_coords = canvas.coords(brick)
        if ball_coords[1] <= brick_coords[3] and ball_coords[3] >= brick_coords[1] and ball_coords[2] >= brick_coords[0] and ball_coords[0] <= brick_coords[2]:
            canvas.delete(brick)
            bricks.remove(brick)
            ball_dy *= -1
            break

    # Check if the ball falls below the paddle
    if ball_coords[3] >= HEIGHT:
        running = False

    # Update the canvas
    win.update()

    # Pause for a short while
    time.sleep(0)

