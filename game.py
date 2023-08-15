# import the pygame module
import pygame
  
# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((900, 900))
  
# Set the caption of the screen
pygame.display.set_caption("billy's wordl")
  
# Fill the background colour to the screen
screen.fill(background_colour)
  
# Update the display using flip
pygame.display.flip()
  
# Variable to keep our game loop running
running = True
  
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
        
        # keypress
        if event.type == pygame.KEYDOWN:
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 30, 60, 60))

    # update the screen
    pygame.display.flip()