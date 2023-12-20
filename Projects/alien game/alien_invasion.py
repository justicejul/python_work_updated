import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from Good_ship import Ship
from bullet import Bullet
from alien import Alien

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


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

        # Create an instance to store game statistics, and create a scoreboard.

        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)

        # Trying to get the class of the bullet and put it in as an attribute
        # this multiplies sprite and like stores them in something like a list
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color.
        # self.bg_color = (230, 230, 230)
        # the color settings has been predefined already, in the settings class

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien using the alien class.
        # We created this alien as a test to get all it's attribute
        # so that we will be able to create the environment for it
        alien = Alien(self)

        # "alien.rect.size" is most likely a class function or variable that receives two variables in form of a tuples
        alien_width, alien_height = alien.rect.size  # Question: what is the use of this Declaration

        # We get the rect object of one alien and get the width of the rect object and assign it to a variable
        alien_width = alien.rect.width

        # we extract a part space of from the overall screen space living space just worth two aliens
        # one of those space will be at the right the other space will be at the left - margins
        # The part of space extracted is  assigned a variable called available_space_x
        available_space_x = self.settings.screen_width - (2 * alien_width)

        # Next, we divide that available space by width worth two aliens,
        # but this time we use floor division which gives us an absolute integer
        # and discards the remainder, no form of decimal
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height

        # to get the available part of the screen where we can place our aliens,
        # We get the vertical measurement of the whole screen and minus the height of the ship,
        # we don't want the aliens images falling on top of the ship, not going to look good
        # we also minus height worth three alien images to put a space in between the Ship and the aliens
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)

        # We then divide the available space by height worth two aliens
        # for the aliens to be perfectly fitted in the available space
        # so there will be one alien then a space of one alien beneath it and that is how it's going to keep going
        number_rows = available_space_y // (2 * alien_height)

        # Since every row has its own column, we said under every row available, in each column available,
        # run the _create_alien() function.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""

        # Unlike the former one this is the main created alien
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        # print(alien.rect.size)

        # alien_width = alien.rect.width, it's not going to be needed since "alien.rect.size" has appeared

        # let us imagine that alien_width is 100px, so this code:
        # alien.x = 100px + 2 times 100px times * (the current alien_number from the for loop)
        # alien.x = 100px + 200px * 1 = 300px, So alien.x = 300px, that will be the position,
        # as the for loop increases so will our position from 1 - the end of the space the aliens can occupy
        alien.x = alien_width + 2 * alien_width * alien_number

        # while it seems that the two are the same, alien.x value holding is temporary
        # while alien.rect.x value holding is more permanent.
        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

        # This line of code is for adding the individual aliens to a list
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            # print('X ', alien.rect.x)
            if alien.check_edges():
                # print('X XXX', alien.rect.x)

                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  # checks for event, and actions
            # In the main loop, we always need to call _check_events(), even if the
            # game is inactive. For example, we still need to know if the user presses Q to
            # quit the game or clicks the button to close the window.
            # We also continue updating the screen, so we can make changes to the screen
            # while waiting to see whether the player chooses to start a new game
            if self.stats.game_active:
                self.ship.update()  # updates the movements of the ship on the screen
                # self.bullets.update()  # updates the movement of the bullets on the screen
                self._update_bullets()
                self._update_aliens()
            self._update_screen()  # updates what has been done lately into the screen

            # Redraw the screen during each pass through the loop.
            # -- self.screen.fill(self.bg_colort)

    # I had a problem getting the function below to work, because it was not showing anything.
    # I tried debugging it but then when I was there was no output or even answer,
    # no reply, but with the help of rico I discovered that i didn't call the function in the first place,
    # where I was supposed to call it,
    # So just a friendly reminder to always check to see if your functions are being refrenced
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # # Check for any bullets that have hit aliens.
        # # If so, get rid of the bullet and the alien.
        # collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # print(collision)

        # Get rid of bullets that have disappeared.
        # When you use a for loop with a list ( or a group in Pygame), Python expects that the list will stay
        # the same length as long as the loop is running.Because we can’t remove items from a list or group
        # within a for loop,we have to loop over a copy of the group.
        # We check each bullet to see whether it has disappeared off the top of the screen at. If it has,
        # we remove it from bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    # The method _check_aliens_bottom() checks whether any aliens have
    # reached the bottom of the screen. An alien reaches the bottom when its
    # rect.bottom value is greater than or equal to the screen’s rect.bottom attribute.
    # If an alien reaches the bottom, we call _ship_hit(). If one alien hits
    # the bottom, there’s no need to check the rest, so we break out of the loop
    # after calling _ship_hit().

    def _start_game(self):
        # with open('high_school.txt', 'r') as file_object:
        #     H_score = file_object.read()
        #     self.stats.high_score = H_score
        # Reset the game settings.
        # with open('high_School.txt', 'r') as file_object:
        #     High_score = file_object.read()
        #     self.stats.high_score = High_score
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()  # the number of ship lives are reset but not yet in motion
        self.stats.game_active = True  # This sets everything in motion

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()

        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor when the game starts.
        pygame.mouse.set_visible(False)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # self.stats.score += self.settings.alien_points
            # the scoring style above is not very precise
            # Since the collision creates a dictionary of items that hits each other and the since the aliens are the
            # values (Key-Value pair) in this case we're using the (.values) method
            #  this one below account for each alien and awards a point for each
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # After collision has been detected and all aliens have been shot down,
        # the group/list that carries it will return "false" if we use an "if statement" to ask.
        # So we say, if aliens does not exist the whole bullet group should be emptied
        # Then a new fleet of aliens
        if not self.aliens:
            self.start_new_level()
            # # Destroy existing bullets and create new fleet.
            # self.bullets.empty()
            # self._create_fleet()
            # self.settings.increase_speed()
            #
            # # Increase level.
            # self.stats.level += 1
            # self.sb.prep_level()

        # print(collision)

    def start_new_level(self):

        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            # print("Ship hit!!!")

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

            # Unhide the mouse cursor when the game stops.
            pygame.mouse.set_visible(True)

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # We want to see the play button exist, only when the game is inactive,
        # if not the button will still exist even when thr game is in motion, only that this time it will be invisible

        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics
            self.stats.reset_stats()  # the number of ship lives are reset but not yet in motion
            self.stats.game_active = True  # This sets everything in motion
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()

            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor when the game starts.
            pygame.mouse.set_visible(False)

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
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            with open('high_School.txt', 'w') as file_object:
                file_object.write(str(self.sb.stats.high_score))
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()


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

        # This draw() method below only works for group sprite and it internal uses the blit() method
        # And why we didn't use this method for the shooting ship was because, like I said before,
        # it is especially for group sprites
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
