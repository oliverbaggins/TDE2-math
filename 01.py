import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Object Translation")

# Load background image
background_image = pygame.image.load("image.png")

# Load character image
character_image = pygame.image.load("totoro.png")
character_width, character_height = 10, 10
character_x, character_y = WIDTH // 3 - character_width // 5, HEIGHT // 5 - character_height // 2

# Object speed
object_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Translate the character based on key presses
    if keys[pygame.K_LEFT]:
        character_x -= object_speed
    if keys[pygame.K_RIGHT]:
        character_x += object_speed
    if keys[pygame.K_UP]:
        character_y -= object_speed
    if keys[pygame.K_DOWN]:
        character_y += object_speed

    # Clear the screen
    screen.blit(background_image, (0, 0))

    # Draw the character
    screen.blit(character_image, (character_x, character_y))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
