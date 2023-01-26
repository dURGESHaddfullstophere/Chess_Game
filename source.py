import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

# Initialize pygame
pygame.init()

# Get the current screen resolution
infoObject = pygame.display.Info()
size = (infoObject.current_w, infoObject.current_h)

# Set the display mode to full screen
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

# Set the title of the window
pygame.display.set_caption("Chess Game")

# Get the square size based on the aspect ratio
aspect_ratio = min(size) / max(size)
square_size = int(min(size) * aspect_ratio / 8)

# Create a chess board using a surface
board = pygame.Surface((8*square_size, 8*square_size))

# Fill the surface with white and black squares
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(board, color, (i*square_size, j*square_size, square_size, square_size))

# Draw a border around the board
border_width = 5
border_color = (0, 225, 255)
pygame.draw.rect(board, border_color, (0, 0, 8*square_size, 8*square_size), border_width)

# Calculate the offset to center the board
offset_x = (size[0] - 8*square_size) // 2
offset_y = (size[1] - 8*square_size) // 2

# Create quit button surface
button_size = (100, 50)
button_color = (255, 72, 0)
quit_button = pygame.Surface(button_size)
quit_button.fill(button_color)

# Create minimize button surface
button_color = (97, 176, 12)
minimize_button = pygame.Surface(button_size)
minimize_button.fill(button_color)

# Adding text to the button
font = pygame.font.SysFont(None, 30)
minimize_text = font.render("Minimize", True, (255,255,255))
quit_text = font.render("Quit", True, (255,255,255))

# Create the border surfaces 
border_color = (255,255,255)
left_border = pygame.Surface((offset_x, 8*square_size))
left_border.fill(border_color)
right_border = pygame.Surface((offset_x, 8*square_size))
right_border.fill(border_color)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (mouse_pos[0] >= offset_x and mouse_pos[0] <= offset_x + button_size[0]) and (mouse_pos[1] >= offset_y + 8*square_size and mouse_pos[1] <= offset_y + 8*square_size + button_size[1]):
                pygame.display.iconify() # to minimize the window
            if (mouse_pos[0] >= offset_x and mouse_pos[0] <= offset_x + button_size[0]) and (mouse_pos[1] >= offset_y + 8*square_size + button_size[1] and mouse_pos[1] <= offset_y + 8*square_size + 2*button_size[1]):
                running = False # to quit the game
    # Display the chess board
    screen.blit(board, (offset_x, offset_y))
    border_color = (0, 225, 255)

    screen.blit(quit_button, (offset_x, offset_y + 8*square_size))
    screen.blit(minimize_button, (offset_x, offset_y + 8*square_size + button_size[1]))
    screen.blit(minimize_text, (offset_x+10, offset_y + 8*square_size + 10))
    screen.blit(quit_text, (offset_x+30, offset_y + 8*square_size + button_size[1]+10))

    pygame.display.flip()
    pygame.draw.line(screen, border_color, (size[0]/3, 0), (size[0]/3, size[1]), border_width)
    pygame.draw.line(screen, border_color, (size[0]*2/3, 0), (size[0]*2/3, size[1]), border_width)


# Quit pygame
pygame.quit()            
           
