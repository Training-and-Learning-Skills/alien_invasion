import sys

import pygame

def check_keydown_events(event, ship):
    """Respond to keystroke"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ship):
    """respond to keystroke and mouse events."""
    #notes the events of the keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship):
    """Refresh the images on the screen and toggles for the new screen."""
    #Redrawing the screen every step of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #leave the most recent screen visible
    pygame.display.flip()