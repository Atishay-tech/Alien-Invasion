"""The module used to store the settings for the game."""

class Settings:
    """Class used to store settings for Alien Invasion."""

    def __init__(self,
                 screen_width: int = 500,
                 screen_height: int = 500,
                 bg_color: '(r,g,b)' = (0, 0, 0)):
        """Initialize the game's settings"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color = bg_color


settings = Settings(
    screen_width=1200,
    screen_height=800,
    bg_color=(255, 255, 255),
)
