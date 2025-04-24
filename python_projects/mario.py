import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Mario Game")

# Player settings
player_size = 40
player_x = 100
player_y = SCREEN_HEIGHT - player_size
player_speed = 5
player_jump = 15
velocity_y = 0
gravity = 1
is_jumping = False

# Ground
ground_height = SCREEN_HEIGHT - player_size

# Game loop
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)  # Clear the screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not is_jumping:  # Jump
        is_jumping = True
        velocity_y = -player_jump

    # Gravity and jumping
    if is_jumping:
        player_y += velocity_y
        velocity_y += gravity
        if player_y >= ground_height:
            player_y = ground_height
            is_jumping = False
    
    # Draw player and ground
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # 30 FPS
