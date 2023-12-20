import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/pussy_ass.bmp')
        self.rect = self.image.get_rect()
        # print('rect', self.rect)

        # Start each new alien near the top left of the screen.
        # We set the object to default values which is the top left of the screen.
        # we add a space to the left of it that’s equal to the alien’s width
        # and a space above it equal to its height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        # We convert the rect object to a float accepting value object
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # """Move the alien to the right."""
        # self.x += self.settings.alien_speed
        """Move the alien right or left."""
        # self.x = self.x + (self.settings.alien_speed * self.settings.fleet_direction)
        # x = x + 1.0 * 1, x = 1
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
