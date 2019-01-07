class Settings():
    """A class for store all settings if the
    alien invasion"""

    def __init__(self):
        """Initializes the settings of the game."""
        # Settings of the screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #self.bg_color = (135,206,235)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3