from .place import Place


class Ore(Place):
  def __init__(self, x, y, img_path, scale, amount, visible = False):
    super().__init__(x, y, img_path, scale, visible)
    self.initial_amount = amount
    self.amount = amount
    self.rect = self.image.get_rect()

  def reset(self):
    super().reset()
    self.amount = self.initial_amount