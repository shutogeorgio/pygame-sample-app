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
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      
      # Redraw the screen during each pass through the loop. 
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()
      
      pygame.display.flip()

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()