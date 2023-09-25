import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SCALE_FACTOR = 1.0  # Initial scale factor
SCALE_POINT = (400, 300)  # Point around which scaling occurs

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scaling Object")

def scale_object(surface, scale_factor, scale_point):
    """
    Scale a surface around a specific point.
    """
    scaled_size = (int(surface.get_width() * scale_factor), int(surface.get_height() * scale_factor))
    scaled_surface = pygame.transform.scale(surface, scaled_size)
    scaled_rect = scaled_surface.get_rect()
    scaled_rect.center = scale_point
    return scaled_surface, scaled_rect

# Load your object image (replace 'object.png' with your image path)
object_image = pygame.image.load('image3.png')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Handle key presses to scale the object
            if event.key == pygame.K_UP:
                SCALE_FACTOR += 0.1
            elif event.key == pygame.K_DOWN:
                SCALE_FACTOR -= 0.1

    # Clear the screen
    screen.fill(BLACK)

    # Scale the object around the specified point
    scaled_object, scaled_rect = scale_object(object_image, SCALE_FACTOR, SCALE_POINT)

    # Display the scaled object
    screen.blit(scaled_object, scaled_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
