import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initializes the game and create a object to the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #Create a spaceship
    ship = Ship(screen)

    #Initiates the main loop of the game
    while True:
        #notes the events of the keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        #Redrawing the screen every step of the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #leave the most recent screen visible
        pygame.display.flip()



run_game()