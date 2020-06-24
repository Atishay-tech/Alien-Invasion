"""The module used to store the settings for the game."""

class Settings:
    """Class used to store settings for Alien Invasion."""

    def __init__(self, new_values: dict):
        """Initialize the game's settings"""
        
        # Default values
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.ship_speed = 5
        self.bullet_speed = 10
        self.bullet_radius = 3
        self.bullet_color = (255, 255, 0)

        # Set new values
        for attr, value in new_values.items():
            setattr(self, attr, value)


set_values = {
    # Screen settings
    'screen_width': 800,
    'screen_height': 600,
    'bg_color': (0, 0, 0),
    # Ship settings
    'ship_speed': 5,
    # Bullets settings
    'bullet_speed': 0,
    'bullet_radius': 3,
    'bullet_color': (255, 255, 0),
}

settings = Settings(set_values)
