import sys

import pygame

def run_game():
    # Initializes the game and create a object to the screen
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')

    #Initiates the main loop of the game
    while True:
        #notes the events of the keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        #leave the most recent screen visible
        pygame.display.flip()

run_game()