import pygame

# Initialize the Pygame library
pygame.init()

# Set the width and height of the screen
width = 600
height = 400

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set the background color to dark green
screen.fill((0, 100, 0))

# Main game loop
while True:
    # Process any events that have occurred
    for event in pygame.event.get():
        # If the user has clicked the "close" button on the window, exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update the screen
    pygame.display.flip()
