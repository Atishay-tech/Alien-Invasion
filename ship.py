"""This module manages the user's ship."""
from os import name
import pygame

if name == 'nt':
    SHIP_IMAGE_PATH = 'images\\ship.bmp'
else:
    SHIP_IMAGE_PATH = 'images/ship.bmp'


class Ship:
    """Class that represents the user's ship."""

    def __init__(self, game_screen: pygame.Surface):
        """Initializes the ship."""
        self.screen = game_screen
        self.screen_rect = game_screen.get_rect()

        self.image = pygame.image.load(SHIP_IMAGE_PATH)
        self.rect = self.image.get_rect()

        # Places ship block in the mid-bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Transfers ship.image to ship.rect."""
        self.screen.blit(self.image, self.rect)
