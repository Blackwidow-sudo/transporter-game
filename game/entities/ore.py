from .place import Place


class Ore(Place):
  def __init__(self, x, y, img_path, scale, config, visible = False):
    super().__init__(x, y, img_path, scale, visible)
    self.set_config(config)
    self.rect = self.image.get_rect()

  def set_config(self, config):
    self.initial_amount = config['ore_amount'] if 'ore_amount' in config else self.amount
    self.amount = self.initial_amount

  def reset(self):
    super().reset()
    self.amount = self.initial_amount