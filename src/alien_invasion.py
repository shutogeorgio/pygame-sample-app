import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:

  def __init__(self):
    # Initialise the game, and crate game resource.
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)
    
    # Set Backgroud Color
    self.bg_color = (230, 230, 230)

  def run_game(self):
    while True:
      self._check_events()
      self.ship.update()
      self._update_screen()
  
  # Define Check Event Feature
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      elif event.type == pygame.KEYDOWN: 
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:    
        self._check_keydown_events(event)
          
    # Redraw the screen during each pass through the loop. 
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    pygame.display.flip()

  # Define Update Event Feature
  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
  
  def _check_keydown_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True 
    elif event.key == pygame.K_LEFT: 
      self.ship.moving_left = True

  def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT: 
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT: 
      self.ship.moving_left = False

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()