"""Driver module of the game"""
import pygame

from settings import settings


class AlienInvasion:
    """Class that manages all other game assests."""

    def __init__(self):
        """Initializes the game window and resorces."""
        pygame.init()
        self.settings = settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """Main game loop."""
        game_running = True

        while game_running:
            
            for event in pygame.event.get():
                # In case use close the window.
                if event.type == pygame.QUIT:
                    game_running = False

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    main = AlienInvasion()
    main.run_game()
