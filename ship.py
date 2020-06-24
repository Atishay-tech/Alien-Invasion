"""This module manages the user's ship."""
from os import name
import pygame
from pygame.sprite import Sprite

if name == 'nt':
    SHIP_IMAGE_PATH = 'images\\ship.bmp'
else:
    SHIP_IMAGE_PATH = 'images/ship.bmp'


class Ship(Sprite):
    """Class that represents the user's ship."""

    def __init__(self, game):
        """Initializes the ship."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(SHIP_IMAGE_PATH)
        self.rect = self.image.get_rect()

        # Places ship block in the mid-bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draws the ship on the screen."""
        self.screen.blit(self.image, self.rect)


    def move_left(self, distance: int = 1):
        """Moves the ship in negative x direction by given distance"""
        if self.rect.left > 0:
            self.rect.move_ip(-distance, 0)


    def move_right(self, distance: int = 1):
        """Moves the ship in positive x direction by given distance"""
        if self.rect.right < self.screen_rect.right:
            self.rect.move_ip(distance, 0)
