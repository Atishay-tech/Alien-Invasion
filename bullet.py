"""This module manages the bullets that the ship fires."""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class used to repesent each bullet."""

    def __init__(self, game):
        """Initializes a bullet object at ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.color = game.settings.bullet_color
        self.radius = game.settings.bullet_radius
        self.speed = game.settings.bullet_speed

        self.rect = pygame.draw.circle(self.screen,
                                       self.color,
                                       game.ship.rect.midtop,
                                       self.radius)
        self.rect.midbottom = game.ship.rect.midtop


    def draw_bullet(self):
        """Draws the bullet on the screen."""
        pygame.draw.circle(self.screen,
                           self.color,
                           self.rect.center,
                           self.radius)


    def update(self):
        """Updates the bullet's position."""
        self.rect.move_ip(0, -self.speed)
        self.draw_bullet()

        if self.rect.bottom <= 0:
            self.kill()
