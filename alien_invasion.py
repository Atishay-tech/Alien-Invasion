"""Driver module of the game"""
import pygame

from settings import settings


class AlienInvasion:
    """Class that manages all other game assests."""

    def __init__(self,
                 screen_width: int = 500,
                 screen_height: int = 500,
                 bg_color: 'rgb' = (0, 0, 0)):
        """Initializes the game window and resorces."""
        pygame.init()

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = bg_color


    def run_game(self):
        """Main game loop."""
        game_running = True

        while game_running:
            for event in pygame.event.get():
                # In case use close the window.
                if event.type == pygame.QUIT:
                    game_running = False

            self.screen.fill(self.bg_color)
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    main = AlienInvasion(**settings)
    main.run_game()
