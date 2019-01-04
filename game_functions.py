import sys

import pygame

def check_events():
    """respond to keystroke and mouse events."""
    #notes the events of the keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Refresh the images on the screen and toggles for the new screen."""
    #Redrawing the screen every step of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #leave the most recent screen visible
    pygame.display.flip()