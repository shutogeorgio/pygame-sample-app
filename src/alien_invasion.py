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
        if event.key == pygame.K_RIGHT:
          self.ship.rect.x += 1
          # Move flag
          self.ship.moving_right = True
        elif event.key == pygame.K_LEFT: 
          self.ship.moving_left = True
  

      elif event.type == pygame.KEYUP:    
        if event.key == pygame.K_RIGHT: 
          self.ship.moving_right = False
        elif event.key == pygame.K_LEFT: 
          self.ship.moving_left = False
          
    # Redraw the screen during each pass through the loop. 
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    pygame.display.flip()

  # Define Update Event Feature
  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()