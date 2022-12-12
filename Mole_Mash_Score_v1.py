# Import the Pygame library
import pygame

# Create a global integer called score and initialize it to 0
score = 0

class Mole:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color
        # Set the initial value of the is_mole_up variable to True
        self.is_mole_up = True
        
        # Set the maximum time down and minimum time down to 2-1 seconds
        self.max_time_down = 2
        self.min_time_down = 1
        
        # Set the maximum time up and minimum time up to 4-3 seconds
        self.max_time_up = 4
        self.min_time_up = 3


    def draw(self):
        # Draw the mole
        pygame.draw.circle(screen, self.color, self.position, self.radius)
        # If the mole is up, draw the mole sprite at its position
        if self.is_mole_up:
            # Calculate the dimensions of the scaled down mole sprite
            sprite_width = self.radius
            sprite_height = self.radius
            # Calculate the coordinates of the top-left corner of the mole sprite
            sprite_x = self.position[0] - sprite_width // 2
            sprite_y = self.position[1] - sprite_height // 2
            # Create a scaled down version of the mole sprite
            scaled_sprite = pygame.transform.scale(Mole_Sprite, (sprite_width, sprite_height))
            # Draw the scaled down mole sprite on the screen
            screen.blit(scaled_sprite, (sprite_x, sprite_y))

    def clicked(self):
        # If the mole is up, set the is_mole_up variable to False
        if self.is_mole_up:
            self.is_mole_up = False
            # Increment the score by 1
            global score
            score += 1


    def is_clicked(self, mouse_pos):
        # If the distance between the mouse cursor and the center of the mole is less than the radius of the mole, the user has clicked on the mole
        if (self.position[0] - mouse_pos[0]) ** 2 + (self.position[1] - mouse_pos[1]) ** 2 < self.radius ** 2:
            return True
        else:
            return False

def draw_score():
    # Set the font, font size, and font color of the text
    font = pygame.font.SysFont("Arial", 30, (255, 255, 255))
    # Create a text surface that contains the text "Score: x"
    text_surface = font.render("Score: " + str(score), True, (255, 255, 255))
    # Get the dimensions of the text surface
    text_width, text_height = text_surface.get_size()
    # Calculate the position of the top-right corner of the text surface
    text_x = width - text_width - 10
    text_y = 10
    # Draw the text surface on the screen
    screen.blit(text_surface, (text_x, text_y))

# Initialize the Pygame library
pygame.init()

# Load the "mole_sprite.png" image and store it in the Mole_Sprite variable
Mole_Sprite = pygame.image.load("mole_sprite.png")

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
        # If the user has clicked the left mouse button
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the (x, y) position of the mouse cursor
            mouse_pos = pygame.mouse.get_pos()
            # Loop through the grid of moles and check if any of them have been clicked
            for row in mole_grid:
                for mole in row:
                    # If the mole at the current index has been clicked, change its color to red
                    if mole.is_clicked(mouse_pos):
                        mole.clicked()

    # Set the background color to dark green
    screen.fill((0, 100, 0))

    # Draw all the moles on the screen
    for row in mole_grid:
        for mole in row:
            mole.draw()
            
    # Draw the score on the screen
    draw_score()

    # Update the screen
    pygame.display.flip()

