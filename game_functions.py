import sys

import pygame
import game_functions as gf

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keystroke"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        gf.fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """respond to keystroke and mouse events."""
    #notes the events of the keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship, bullets):
    """Refresh the images on the screen and toggles for the new screen."""
    #Redrawing the screen every step of the loop
    screen.fill(ai_settings.bg_color)
    #Redrawing all the projectiles behind spaceship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    #leave the most recent screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Refresh projectiles position and get rid of old projectiles."""
    #Refresh projectiles position
    bullets.update()

    #Gets rid of projectiles that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Shoot a projectile if the limit is not reached"""
    #Creates a new projectiles and add to the projectiles group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)