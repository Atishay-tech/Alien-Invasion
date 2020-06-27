"""The module used to store the settings for the game."""

class Settings:
    """Class used to store settings for Alien Invasion."""

    def __init__(self, new_values: dict):
        """Initialize the game's settings."""

        # Default values
        self.full_screen_mode = True
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.ship_speed = 5
        self.bullet_speed = 10
        self.bullet_radius = 3
        self.bullet_color = (255, 255, 0)
        self.fleet_speed_x = 1
        self.fleet_speed_y = 20

        # Sets new values.
        for attr, value in new_values.items():
            setattr(self, attr, value)


set_values = {
    'full_screen_mode': True,
    'screen_width': 800,
    'screen_height': 600,
    'bg_color': (0, 0, 0),
    'ship_speed': 5,
    'bullet_speed': 10,
    'bullet_radius': 3,
    'bullet_color': (255, 255, 0),
}

settings = Settings(set_values)
