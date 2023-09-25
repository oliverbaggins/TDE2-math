import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Object Reflection")

# Load background image
background = pygame.image.load("image4.png")

# Object properties
object_width, object_height = 100, 50
object_x, object_y = 350, 250
object_rect = pygame.Rect(object_x, object_y, object_width, object_height)

# Axis of reflection properties
axis_y = 300

# Movement variables
object_speed = 2
axis_speed = 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_rect.x -= object_speed
    if keys[pygame.K_RIGHT]:
        object_rect.x += object_speed
    if keys[pygame.K_UP]:
        axis_y -= axis_speed
    if keys[pygame.K_DOWN]:
        axis_y += axis_speed

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the axis
    pygame.draw.line(screen, (255, 255, 255), (0, axis_y), (width, axis_y), 2)

    # Draw the original object
    pygame.draw.rect(screen, (255, 255, 255), object_rect)

    # Calculate the reflected object's position
    reflected_object_rect = object_rect.copy()
    reflected_object_rect.y = 2 * axis_y - object_rect.y - object_rect.height

    # Draw the reflected object
    pygame.draw.rect(screen, (255, 255, 255), reflected_object_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
