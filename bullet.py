import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that manages fired projectiles in 
    current position of the spaceship."""
    def __init__(self, ai_settings, screen, ship):
        """Create a object for the projectile in current position of spaceship"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a rectangle for the projectile in (0, 0) and
        #define correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Stores the position of the projectile as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """move the projectile for top screen"""
        #refresh decimal position of projectile
        self.y -= self.speed_factor
        # Refresh rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the projectile in the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
