"""Driver module of the game."""
import sys
import pygame
from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
)

from settings import settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Class that manages all game assests."""

    def __init__(self):
        """Initializes the game window and resorces."""
        pygame.init()

        self.settings = settings
        self._init_window()

        self.ship = Ship(self)
        self.ship.speed = settings.ship_speed

        self.bullets = pygame.sprite.Group()


    def _init_window(self):
        """Initializes window with settings like screen_width and caption"""

        self.screen = pygame.display.set_mode((0, 0),   # Full Screen mode
                                              pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        #self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")


    def _handle_events(self):
        """Updates position of sprites according to given pygame keys."""
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()

        _check_exit_events(events)

        if pressed_keys[K_LEFT]:
            self.ship.move_left(self.ship.speed)
        if pressed_keys[K_RIGHT]:
            self.ship.move_right(self.ship.speed)

        for event in events:
            if event.type == KEYDOWN and event.key == K_SPACE:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_screen(self):
        """Updates screen and all the images on screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.bullets.update()

        pygame.display.flip()


    def run_game(self):
        """Main game loop."""
        game_running = True

        while game_running:
            self._handle_events()
            self._update_screen()


def _check_exit_events(events: list) -> None:
    """Handle events if player wants to quit the game."""
    for event in events:

        if (event.type == QUIT
                or event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
