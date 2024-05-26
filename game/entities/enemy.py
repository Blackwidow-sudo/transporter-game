import pygame as pg
import math

from .entitiy import Entitiy


class Enemy(Entitiy):
  def __init__(self, position, img_path, scale, config, visible = False):
    super().__init__(position, img_path, scale, visible)
    self.set_config(config)

  def update(self, player):
    player_x, player_y = player.position
    x, y = self.position
    dx = player_x - x
    dy = player_y - y
    dist = math.hypot(dx, dy)

    dx /= dist
    dy /= dist

    self.position = (x + dx * self.speed, y + dy * self.speed)
    
    self.rect.topleft = self.position

  def set_config(self, config):
    self.speed = config['enemy_speed'] if 'enemy_speed' in config else self.speed

  def draw(self, window):
    if self.visible:
      window.blit(self.image, self.position)