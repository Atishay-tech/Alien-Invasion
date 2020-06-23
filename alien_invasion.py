"""Driver module of the game."""
import sys
import pygame
from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
)

from settings import settings
from ship import Ship


class AlienInvasion:
    """Class that manages all game assests."""

    def __init__(self):
        """Initializes the game window and resorces."""
        pygame.init()

        self.settings = settings
        self._init_window()
        self.ship = Ship(self.screen)


    def _init_window(self):
        """Initializes window with settings like screen_width and caption"""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")


    def update_ship(self, pressed_keys: dict):
        """Updates the ship's position according to given pygame keys"""
        if pressed_keys[K_LEFT]:
            self.ship.move_left(3)
        if pressed_keys[K_RIGHT]:
            self.ship.move_right(3)


    def run_game(self):
        """Main game loop."""
        game_running = True

        while game_running:
            _handle_exit_events()

            pressed_keys = pygame.key.get_pressed()
            self.update_ship(pressed_keys)

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            pygame.display.flip()

        pygame.quit()


def _handle_exit_events() -> None:
    """Handle events if player wants to quit the game."""
    for event in pygame.event.get():

        if (event.type == QUIT
                or event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main = AlienInvasion()
    main.run_game()
