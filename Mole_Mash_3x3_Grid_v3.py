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

# Set the width and height of the mole grid
grid_width = 3
grid_height = 3

# Calculate the spacing between each mole
x_spacing = width // grid_width
y_spacing = height // grid_height

# Set the color of the moles
mole_color = (210, 180, 140)

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set the background color to dark green
screen.fill((0, 100, 0))

# Create a grid of moles using a for loop
mole_grid = []
for y in range(grid_height):
    row = []
    for x in range(grid_width):
        mole = Mole((x * x_spacing + x_spacing // 2, y * y_spacing + y_spacing // 2), 50, mole_color)
        row.append(mole)
    mole_grid.append(row)

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
