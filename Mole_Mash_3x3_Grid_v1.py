import pygame

class Mole:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

# Initialize the Pygame library
pygame.init()

# Set the width and height of the screen
width = 600
height = 400

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set the background color to dark green
screen.fill((0, 100, 0))

# Create a 3 by 3 grid of moles
mole_grid = [
    [Mole((100, 100), 50, (210, 180, 140)), Mole((300, 100), 50, (210, 180, 140)), Mole((500, 100), 50, (210, 180, 140))],
    [Mole((100, 200), 50, (210, 180, 140)), Mole((300, 200), 50, (210, 180, 140)), Mole((500, 200), 50, (210, 180, 140))],
    [Mole((100, 300), 50, (210, 180, 140)), Mole((300, 300), 50, (210, 180, 140)), Mole((500, 300), 50, (210, 180, 140))],
]

# Main game loop
while True:
    # Process any events that have occurred
    for event in pygame.event.get():
        # If the user has clicked the "close" button on the window, exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw all the moles on the screen
    for row in mole_grid:
        for mole in row:
            mole.draw()

    # Update the screen
    pygame.display.flip()
