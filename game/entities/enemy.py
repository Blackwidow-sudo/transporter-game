import pygame as pg
import math

from .vehicle import Vehicle


class Enemy(Vehicle):
  def __init__(self, x, y, img_path, scale, config, visible = False):
    super().__init__(x, y, img_path, scale, config, visible)

  def update(self, player):
    dx = player.x - self.x
    dy = player.y - self.y
    dist = math.hypot(dx, dy)

    dx /= dist
    dy /= dist

    self.x += dx * self.speed
    self.y += dy * self.speed
    
    self.rect.topleft = (self.x, self.y)

  def draw(self, window):
    if self.visible:
      window.blit(self.image, (self.x, self.y))