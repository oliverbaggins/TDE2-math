import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Object Rotation")

# Load background image and character image
background_image = pygame.image.load("image2.png")
character_image = pygame.image.load("mooncake.png")

# Initialize character properties
character_rect = character_image.get_rect()
character_position = (WIDTH // 2, HEIGHT // 2)  # Centered on the screen
angle = 0
rotation_speed = 2  # Adjust as needed

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    
    # Rotate the character clockwise
    if keys[pygame.K_w]:
        angle += rotation_speed

    # Rotate the character counterclockwise
    if keys[pygame.K_s]:
        angle -= rotation_speed

    # Rotate the character
    rotated_character = pygame.transform.rotate(character_image, angle)
    rotated_rect = rotated_character.get_rect(center=character_position)

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the rotated character on top of the background
    screen.blit(rotated_character, rotated_rect.topleft)

    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()
