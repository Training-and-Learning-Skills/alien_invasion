import sys

import pygame
import game_functions as gf

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
    ship = Ship(screen, ai_settings)

    #Initiates the main loop of the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        

run_game()