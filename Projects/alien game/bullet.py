import pygame
from pygame.sprite import Sprite

# Our class is inheriting a class from the pygame library to use for the bullet part
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # We're creating an object(the bullet) with an initial position set to null(0, 0).
        # We left it, so that we'll be able to specify it(the positioning) later.
        # We create a bullet with measurement which are referenced from the settings class
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        # Let the top of the bullet touch the top of the ship sprite they should be aligned at the top.
        # We're positioning the bullet to be place at the top of our ship sprite.
        # This is the specification of the positioning.
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        # W'ere trying to get the bullet as a float or decimal value'
        # And we're also using 'Y' instead of x, this, instead of a '
        # vertical position is going to horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        # In python's pygame, decreasing numbers move object upwards, unlike in maths
        self.y -= self.settings.bullet_speed  # self.y = self.y - self.settings.bullet_speed
        # Update the rect position.

        self.rect.y = self.y  #Qestion: when we assigned self.y as the Float accepting variable of "self.rect.y" did it still have the rect attribute

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        # Just like how we drew our in ship image on the screen using the blitme() function
        # We're doin the same here, except that we're using a different function,
        # because we're not dealing with downloaded images, instead We're dealing with
        # directly created object which were not imported.
        # We're using ".rect" because we're working with an object created with the Rect function
        # we want to draw it.

        pygame.draw.rect(self.screen, self.color, self.rect)
