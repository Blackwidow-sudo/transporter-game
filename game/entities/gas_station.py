import pygame as pg

from .entitiy import Entitiy

class GasStation(Entitiy):
  def __init__(self, position, img_path, scale, visible = False):
    super().__init__(position, img_path, scale, visible)

  def draw(self, window):
    if self.visible:
      window.blit(self.image, self.position)