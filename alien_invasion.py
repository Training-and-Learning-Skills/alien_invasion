import sys

import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group

def run_game():
    # Initializes the game and create a object to the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #Create a spaceship
    ship = Ship(screen, ai_settings)

    #Creates a group in which to store the projectiles
    bullets = Group()
    #Initiates the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        

run_game()