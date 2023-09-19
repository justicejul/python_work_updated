import sys
import pygame
from settings import Settings
from Good_ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # When creating the screen surface, we pass a size of (0, 0) and the parameter pygame.FULLSCREEN.
        # This tells Pygame to figure out a window size that will fill the screen.
        # Because we don’t know the width and height of the screen ahead of time,
        # we update these settings after the screen is created.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Trying to get the class of the bullet and put it in as an attribute
        # this multiplies sprite and like stores them in something like a list
        self.bullets = pygame.sprite.Group()

        # Set the background color.
        # self.bg_color = (230, 230, 230)
        # the color settings has been predefined already, in the settings class

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  # checks for event, and actions
            self.ship.update()  # updates the movements of the ship on the screen
            self.bullets.update()  # updates the movement of the bullets on the screen
            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                    print(len(self.bullets))

            self._update_screen()  # updates what has been done lately into the screen

            # Redraw the screen during each pass through the loop.
            # -- self.screen.fill(self.bg_colort)

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

#  We broke the control of movement through events into
#  two and store each in a function, One controls the
#  movement when the key is pressed the other controls
#  the movement when it is released.
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.b
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # if the length of our bullets list is less than number of bullets allowed, let the following code under run.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)     # new_bullet = Bullet(ai_game)
            # This adds the created bullets to that our bullet group list above(self.bullets = pygame.sprite.Group())
            self.bullets.add(new_bullet)  # ai_game.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        """
        since we have put the settings in one class,
        We'll define it there call it from there, 
        instead of just randomly putting it
        """

        self.ship.blitme()
        # This is a function taken from the ship class

        for bullet in self.bullets.sprites():
            # the ".sprites()" is a method provided by pygame.sprite.Group objects.
            # This method is used to retrieve a list of all the sprites contained within the group.
            # It returns a list of sprite objects that are part of the group.
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
