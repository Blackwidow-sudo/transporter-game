import pygame as pg
from typing import Union, Tuple

class Entitiy:
  def __init__(self, position: Tuple[int, int], img_path: str, scale: float, visible: bool):
    img = pg.image.load(img_path)
    width, height = img.get_size()

    self.image = pg.transform.smoothscale(img, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.visible = visible
    self.initial_position = self.position = position

  def draw(self, window: pg.Surface):
    if self.visible:
      window.blit(self.image, self.position)

  def toggle_visibility(self, visible: Union[bool, None] = None):
    self.visible = not self.visible if visible is None else visible

  def reset(self):
    self.position = self.initial_position
    self.rect.topleft = self.position
