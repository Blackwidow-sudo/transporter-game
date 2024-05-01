import pygame as pg

class Vehicle:
  def __init__(self, x, y, img_path, scale, config, visible):
    img = pg.image.load(img_path)
    width, height = img.get_size()
    self.image = pg.transform.smoothscale(img, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
    self.visible = visible
    self.start_position = (x, y)
    for key in config:
      setattr(self, key, config[key])

  def set_config(self, config):
    self.speed = config['speed'] if 'speed' in config else self.speed

  def draw(self, window):
    if self.visible:
      window.blit(self.image, (self.x, self.y))

  def reset(self):
    self.x, self.y = self.start_position
    self.rect.topleft = (self.x, self.y)