import pygame as pg

from .entitiy import Entitiy


class Factory(Entitiy):
  def __init__(self, position, img_path, scale, config, visible = False):
    super().__init__(position, img_path, scale, visible)
    self.set_config(config)
    self.ore = 0

  def set_config(self, config):
    self.win_threshold = config['win_threshold'] if 'win_threshold' in config else self.win_threshold
    self.ore_amount = config['ore_amount'] if 'ore_amount' in config else self.ore_amount

  def draw(self, window):
    if self.visible:
      self.draw_ore_bar(window)
      window.blit(self.image, self.position)

  def draw_ore_bar(self, window):
    x, y = self.position
    ore_bar_width = self.rect.width
    ore_bar_height = 20
    # Fill according to progress, but not more than the bar width
    fill = min(ore_bar_width, (self.ore / self.get_required_win_amount()) * ore_bar_width)
    outline_rect = pg.Rect(x, y - ore_bar_height - 10, ore_bar_width, ore_bar_height)
    fill_rect = pg.Rect(x, y - ore_bar_height - 10, fill, ore_bar_height)
    pg.draw.rect(window, 'green', fill_rect)
    pg.draw.rect(window, (0, 0, 0), outline_rect, 2)
  
  def get_progress(self):
    """Return the progress of the game in percentage."""
    return (self.ore / self.get_required_win_amount()) * 100
  
  def get_required_win_amount(self):
    """Return the amount of ore required to win the game."""
    return (self.win_threshold * self.ore_amount) / 100

  def reset(self):
    super().reset()
    self.ore = 0