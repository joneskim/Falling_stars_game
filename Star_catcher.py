import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 50
STAR_SIZE = 20
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)
STAR_COLOR = (255, 255, 0)
BOMB_COLOR = (255, 0, 0)
FONT = pygame.font.Font(None, 36)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collect the Falling Stars")

# Initialize player position and speed
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE
player_speed = 5

# star speed
fall_speed = 5

# Create a list to store the stars
stars = []
bombs = []

# Function to generate a random star
def create_star():
    x = random.randint(0, SCREEN_WIDTH - STAR_SIZE)
    y = 0
    return pygame.Rect(x, y, STAR_SIZE, STAR_SIZE)

def create_bomb():
    x = random.randint(0, SCREEN_WIDTH - STAR_SIZE)
    y = 0
    return pygame.Rect(x, y, STAR_SIZE, STAR_SIZE)

# Function to draw the player and stars
def draw_objects():
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    
    for star in stars:
        pygame.draw.rect(screen, STAR_COLOR, star)

    for bomb in bombs:
        pygame.draw.rect(screen, BOMB_COLOR, bomb)


# Function to display the score and remaining time
def draw_score_time(score, remaining_time):
    score_text = FONT.render(f"Score: {score}", True, (0, 0, 0))
    time_text = FONT.render(f"Time: {remaining_time} seconds", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

# Main game loop
running = True
clock = pygame.time.Clock()
score = 0
total_time = 300  # Total game time in seconds
remaining_time = total_time

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Create a new star at random intervals
    if random.randint(0, 100) < 5:
        stars.append(create_star())

    if random.randint(0, 100) < 1:
        bombs.append(create_bomb())

    for bomb in bombs:
        if pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE).colliderect(bomb):
            bombs.remove(bomb)
            score -= 20
            if score < 0:
                score = 0
                # quit the game
                running = False

    # Check for collisions between player and stars
    for star in stars:
        if pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE).colliderect(star):
            stars.remove(star)
            score += 1



    # INTRODUCE GRAVITY
    # Move the stars
    for star in stars:
        star.y += fall_speed

    for bomb in bombs:
        bomb.y += fall_speed


    # Clear the screen
    screen.fill(WHITE)

    # Draw objects
    draw_objects()

    # Draw score and remaining time
    draw_score_time(score, remaining_time)

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

    # Update remaining time
    remaining_time = max(total_time - pygame.time.get_ticks() // 1000, 0)

    # Check if the game is over
    if remaining_time == 0:
        running = False

# Game over
pygame.quit()
sys.exit()