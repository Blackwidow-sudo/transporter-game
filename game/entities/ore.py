from .place import Place


class Ore(Place):
  def __init__(self, x, y, img_path, scale, capacity, visible = False):
    super().__init__(x, y, img_path, scale, visible)
    self.capacity = capacity
    self.rect = self.image.get_rect()

  def draw(self, window):
    window.blit(self.image, (self.x, self.y))