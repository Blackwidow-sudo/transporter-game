import pygame as pg


class Place:
  def __init__(self, x, y, img_path, scale, visible):
    img = pg.image.load(img_path)
    width, height = img.get_size()
    self.image = pg.transform.smoothscale(img, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect() if self.image else None
    self.x = x
    self.start_position = (x, y)
    self.y = y
    self.visible = visible

  def draw(self, window):
    if self.visible:
      window.blit(self.image, (self.x, self.y))

  def reset(self):
    self.x, self.y = self.start_position
    self.rect.topleft = (self.x, self.y)