from .entitiy import Entitiy


class Ore(Entitiy):
  def __init__(self, position, img_path, scale, config, visible = False):
    super().__init__(position, img_path, scale, visible)
    self.set_config(config)

  def set_config(self, config):
    self.initial_amount = config['ore_amount'] if 'ore_amount' in config else self.amount
    self.amount = self.initial_amount

  def reset(self):
    super().reset()
    self.amount = self.initial_amount