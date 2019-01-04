class Ship():
    def __init__(self, screen):
        """Initializes the spaceship and set your starting position."""
        self.screen = screen

        #load the image of the spaceship and get you rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Starts each new spaceship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the spaceship in your current position."""
        self.screen.blit(self.image, self.rect)