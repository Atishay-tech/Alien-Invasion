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
from enemy import Enemy


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
        self.enemies = pygame.sprite.Group()
        self._create_fleet()
        self.fleet_direction = 1


    def _init_window(self):
        """Initializes window with settings like screen_width and caption."""
        if self.settings.full_screen_mode:  # Full screen mode
            self.screen = pygame.display.set_mode(
                (0, 0), pygame.FULLSCREEN)
        else:                                   # Other modes
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))

        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")


    def _create_fleet(self):
        """Initializes the fleet of aliens."""
        enemy = self._create_enemy(0, 0)

        available_space_x = (self.screen.get_width()
                             - 2*enemy.width)
        available_space_y = (self.screen.get_height()
                             - 3*enemy.height
                             - self.ship.rect.height)
        if self.settings.full_screen_mode:
            available_space_x -= 8*enemy.width 

        enemies_per_row = available_space_x // (2*enemy.width)
        num_of_rows = available_space_y // (2*enemy.height)

        for row in range(num_of_rows):
            for column in range(enemies_per_row):
                enemy = self._create_enemy(row, column)
                self.enemies.add(enemy)


    def _create_enemy(self, row_number: int, column_number: int) -> Enemy:
        """Creates a new enemy"""
        enemy = Enemy(self)
        enemy.width = enemy.rect.width
        enemy.height = enemy.rect.height

        enemy.rect.x += column_number * (2*enemy.width)
        enemy.rect.y += row_number * (2*enemy.height)
        if self.settings.full_screen_mode:
            enemy.rect.x += 4.5*enemy.width

        return enemy


    def run_game(self):
        """Main game loop."""
        game_running = True

        while game_running:
            self._handle_events()
            self._update_screen()


    def _handle_events(self):
        """Updates position of sprites according to given pygame keys."""
        pressed_keys = pygame.key.get_pressed()
        events = pygame.event.get()

        _check_exit_events(events)
        self._move_ship_by(pressed_keys)

        for event in events:
            if event.type == KEYDOWN and event.key == K_SPACE:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

        self._handle_collisions()
        if not self.enemies.sprites():
            self._create_fleet()
            self.settings.fleet_speed_x += 2


    def _update_screen(self):
        """Updates screen and all the images on screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.bullets.update()
        self._move_fleet()
        self.enemies.draw(self.screen)

        pygame.display.flip()


    def _move_ship_by(self, pressed_keys: dict):
        """Change ship's position according to presently pressed keys."""
        if pressed_keys[K_LEFT]:
            self.ship.move_left(self.ship.speed)
        if pressed_keys[K_RIGHT]:
            self.ship.move_right(self.ship.speed)


    def _handle_collisions(self):
        """Handles collisions between any two sprites"""
        pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True,
            pygame.sprite.collide_circle)


    def _move_fleet(self):
        """Changes the position of all alien ship Rects."""
        for enemy in self.enemies:
            if (enemy.rect.right >= self.settings.screen_width
                    or enemy.rect.left <= 0):
                self.fleet_direction *= -1
                for enemy in self.enemies:
                    enemy.rect.y += self.settings.fleet_speed_y
                break
        for enemy in self.enemies:
            enemy.rect.x += (self.fleet_direction
                             * self.settings.fleet_speed_x)


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
