import pygame as pg

from .vehicle import Vehicle


class Player(Vehicle):
  loaded_ore = 0

  def __init__(self, x, y, img_path, scale, config, visible = False):
    super().__init__(x, y, img_path, scale, config, visible)
    self.fuel_amount = 100

  def check_collision(self, other):
    if self.rect.colliderect(other.rect):
      return True
    return False
  
  def no_fuel(self):
    return self.fuel_amount <= 0
  
  def set_config(self, config):
    self.fuel_consumption = config['fuel_consumption'] if 'fuel_consumption' in config else self.fuel_consumption
    self.ore_capacity = config['ore_capacity'] if 'ore_capacity' in config else self.ore_capacity
  
  def draw_fuel_bar(self, window):
    fuel_bar_width = self.rect.width
    fuel_bar_height = 20
    fill = (self.fuel_amount / 100) * fuel_bar_width
    outline_rect = pg.Rect(self.x, self.y - fuel_bar_height - 10, fuel_bar_width, fuel_bar_height)
    fill_rect = pg.Rect(self.x, self.y - fuel_bar_height - 10, fill, fuel_bar_height)
    pg.draw.rect(window, (255, 0, 0), fill_rect)
    pg.draw.rect(window, (0, 0, 0), outline_rect, 2)

  def draw_loaded_state(self, window):
    font = pg.font.Font(None, 25)
    text = font.render('Loaded' if self.loaded_ore else '', True, (0, 0, 0))
    window.blit(text, (self.x, self.y - 30))

  def draw(self, window):
    if self.visible:
      window.blit(self.image, (self.x, self.y))
      self.draw_fuel_bar(window)
      self.draw_loaded_state(window)

  def update(self, dt):
    keys = pg.key.get_pressed()
    boundaries = pg.display.get_surface().get_rect()

    if any([keys[pg.K_LEFT], keys[pg.K_RIGHT], keys[pg.K_UP], keys[pg.K_DOWN], keys[pg.K_a], keys[pg.K_d], keys[pg.K_w], keys[pg.K_s]]):
      self.fuel_amount = max(0, self.fuel_amount - self.fuel_consumption * dt)

    if keys[pg.K_LEFT] or keys[pg.K_a]:
      self.x = max(0, self.x - self.speed)
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
      self.x = min(boundaries.width - self.rect.width, self.x + self.speed)
    if keys[pg.K_UP] or keys[pg.K_w]:
      self.y = max(0, self.y - self.speed)
    if keys[pg.K_DOWN] or keys[pg.K_s]:
      self.y = min(boundaries.height - self.rect.height, self.y + self.speed)

    self.rect.topleft = (self.x, self.y)

  def reset(self):
    super().reset()
    self.fuel_amount = 100
    self.loaded_ore = 0