import pygame
import time
import random

# Initialize pygame and create a window
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")

# Create a snake and set its initial position
snake = [(200, 200), (210, 200), (220,200)]
snake_color = (255, 0, 0)
snake_direction = RIGHT

# Create a food item and set its initial position
food = (250, 250)
food_color = (0, 255, 0)

# Create the score
score = 0

# Set the initial game speed
game_speed = 10

# Create a function to generate random food
def generate_food():
    food_x = round(random.randrange(0, width — 10) / 10.0)*10.0
    food_y = round(random.randrange(0, height — 10) / 10.0) * 10.0
    return (food_x, food_y)

# Create a function to check for collision
def collision_detection():
    if snake[0][0] >= width or snake[0][0] < 0 or snake[0][1] >= height or snake[0][1] < 0:
    return True
for block in snake[1:]:
    if snake[0][0] == block[0] and snake[0][1] == block[1]:
    return True
    return False

# Main game loop
while True:
# Handle events
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
quit()
elif event.type == pygame.KEYDOWN:
if event.key == pygame.K_LEFT and snake_direction != “RIGHT”:
snake_direction = “LEFT”
elif event.key == pygame.K_RIGHT and snake_direction != “LEFT”:
snake_direction = “RIGHT”
elif event.key == pygame.K_UP and snake_direction != “DOWN”:
snake_direction = “UP”
elif event.key == pygame.K_DOWN and snake_direction != “UP”:
snake_direction = “DOWN”

# Move the snake
if snake_direction == “RIGHT”:
snake[0] = (snake[0][0] + 10, snake[0][1])
elif snake_direction == “LEFT”:
snake[0] = (snake[0][0] — 10, snake[0][1])
elif snake_direction == “UP”:
snake[0] = (snake[0][0], snake[0][1] — 10)
elif snake_direction == “DOWN”:
snake[0] = (snake[0][0], snake[0][1] + 10)

for i in range(len(snake) — 1, 0, -1):
    snake[i] = (snake[i-1][0], snake[i-1][1])

# Check for collision with food
if snake[0][0] == food[0] and snake[0][1] == food[1]:
food = generate_food()
snake.append((snake[-1][0]-10, snake[-1][1]))
score += 1

# Check for collision with the boundaries and the snake’s body
if collision_detection():
    print(“Game Over! Your score is: “, score)
    pygame.quit()
    quit()

# Draw the snake and food
screen.fill((0, 0, 0))
for pos in snake:
pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))
pygame.draw.rect(screen, food_color, pygame.Rect(food[0], food[1], 10, 10))

# Draw the score
font = pygame.font.SysFont(None, 30)
text = font.render(“Score: “+str(score), True, (255,255,255))
screen.blit(text, (0,0))

pygame.display.update()

# Slow down the game
time.sleep(1 / game_speed)

