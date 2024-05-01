import pygame as pg

from .place import Place

class GasStation(Place):
  def __init__(self, x, y, img_path, scale, visible = False):
    super().__init__(x, y, img_path, scale, visible)
    self.visible = visible

  def draw(self, window):
    if self.visible:
      window.blit(self.image, (self.x, self.y))