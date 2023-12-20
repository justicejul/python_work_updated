import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        super().__init__()

        # Trying to get the screen attribute of the instance of the AlienInvasion class
        self.screen = ai_game.screen
        # We call the settings class which was imported into the alien_invasion class,
        # and we assigned it to name called "Self.settings"
        self.settings = ai_game.settings

        # retrieves the rectangular dimensions of the screen attribute as a Rect object.This Rect object has
        # attributes like x, y, width, and height that describe the position and size of the screen.
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its Rect object.
        self.image = pygame.image.load('images/normal_ship-1.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # The Rect object treats things like a rectangle for better positioning and measurement
        # for this one, just imagine the game screen and the ship image as rectangle
        # we gave the ship a value of midbottom and the game screen the value of midbottom,
        # the ships bottom part will align with the bottom of the screen, to put it more plainly
        # the bottom of the ship will touch the bottom of the game screen, if the screen position was
        # midtop, the bottom of the screen would have been on the screen(we wouldn't have seen it).
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        # We want fine and more precise movement, that's why we're going for decimal values
        # We carry our image sprite rect value and convert it into a float value type
        # We then assign it to a variable, "self.x"
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value for movement due to a condition being True.
        # It mainly just move the ship horizontally (x-axis), and the x value is responsible for that.
        # if the amount of movement and the right position of the sprite image is less than the right
        # edge of the screen,
        # it should keep on moving that means it can only move as long as it doesn't touch the edge of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # We have changed the increment values from integer values to floats fo fine and better movement
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        # We assign the name of new rect value to
        # the old name of the old rect value for easy usage
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        # This is function is used to draw surface on order surfaces,
        # you could also say put or paste in place of draw.
        # And you could also use objects in place of surfaces.
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


