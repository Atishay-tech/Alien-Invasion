"""The module used to store the settings for the game."""

class Settings:
    """Class used to store settings for Alien Invasion."""

    def __init__(self,
                # Screen settings
                 screen_width: int = 800,
                 screen_height: int = 600,
                 bg_color: '(r,g,b)' = (0, 0, 0),
                # Ship settings
                 ship_speed: int = 3,
                # Bullets settings
                 bullet_speed: int = 10,
                 bullet_radius: int = 3,
                 bullet_color: '(r,g,b)' = (255, 255, 0)):
        """Initialize the game's settings"""
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color = bg_color
        self.ship_speed = ship_speed
        self.bullet_speed = bullet_speed
        self.bullet_radius = bullet_radius
        self.bullet_color = bullet_color  


settings = Settings(
    screen_width=800,
    screen_height=600,
    bg_color=(0, 0, 0),
    ship_speed=5,
)
