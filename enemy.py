"""This module contains classes and methods of enemy ships."""
from os import name
import pygame

from ship import Ship

if name == 'nt':
    SHIP_IMAGE_PATH = 'images\\enemy.bmp'
else:
    SHIP_IMAGE_PATH = 'images/enemy.bmp'


class Enemy(Ship):
    """Class representing each enemy ship."""

    def __init__(self, game):
        """Initializes new enemy object at top left corner of screen"""
        super().__init__(game)
        self.settings = game.settings

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(SHIP_IMAGE_PATH).convert()
        self.rect = self.image.get_rect()

        # Places alien ship near top left corner of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


    def update(self):
        pass
