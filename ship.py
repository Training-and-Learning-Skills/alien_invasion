import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        """Initializes the spaceship and set your starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        #load the image of the spaceship and get you rect
        self.image = pygame.image.load('images/ship.bmp')
        #self.image = pygame.image.load('images/mordomo.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Starts each new spaceship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #stores a value decimal to the center of the spaceship
        self.center = float(self.rect.centerx)
        #Flag of movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Upgrades position of the spaceship according to 
        Flag of movement."""

        #upgrades the value of the center of the ship, not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor            
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Upgrades object according with self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the spaceship in your current position."""
        self.screen.blit(self.image, self.rect)