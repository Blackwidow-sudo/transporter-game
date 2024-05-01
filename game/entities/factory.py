import pygame as pg

from .place import Place


class Factory(Place):
  ore = 0

  def __init__(self, x, y, img_path, scale, win_threshold, ore_amount, visible = False):
    super().__init__(x, y, img_path, scale, visible)
    self.win_threshold = win_threshold
    self.ore_amount = ore_amount

  def draw(self, window):
    self.draw_ore_bar(window)
    window.blit(self.image, (self.x, self.y))

  def draw_ore_bar(self, window):
    ore_bar_width = self.rect.width
    ore_bar_height = 20
    # Fill according to progress, but not more than the bar width
    fill = min((self.ore / self.ore_amount) * ore_bar_width, ore_bar_width)
    outline_rect = pg.Rect(self.x, self.y - ore_bar_height - 10, ore_bar_width, ore_bar_height)
    fill_rect = pg.Rect(self.x, self.y - ore_bar_height - 10, fill, ore_bar_height)
    pg.draw.rect(window, (0, 0, 255), fill_rect)
    pg.draw.rect(window, (0, 0, 0), outline_rect, 2)
  
  def get_progress(self):
    needed = self.ore_amount * (self.win_threshold / 100)
    return (self.ore / needed) * 100
  
  def reset(self):
    super().reset()
    self.ore = 0