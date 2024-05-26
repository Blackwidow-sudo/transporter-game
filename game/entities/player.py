import pygame as pg

from .entitiy import Entitiy


class Player(Entitiy):
  loaded_ore = 0

  def __init__(self, position, img_path, scale, config, visible = False):
    super().__init__(position, img_path, scale, visible)
    self.fuel_amount = 100
    self.set_config(config)

  def check_collision(self, other):
    if self.rect.colliderect(other.rect):
      return True
    return False
  
  def no_fuel(self):
    return self.fuel_amount <= 0
  
  def set_config(self, config):
    self.speed = config['player_speed'] if 'player_speed' in config else self.speed
    self.fuel_consumption = config['fuel_consumption'] if 'fuel_consumption' in config else self.fuel_consumption
    self.ore_capacity = config['ore_capacity'] if 'ore_capacity' in config else self.ore_capacity
  
  def draw_fuel_bar(self, window):
    x, y = self.position
    fuel_bar_width = self.rect.width
    fuel_bar_height = 20
    fill = (self.fuel_amount / 100) * fuel_bar_width
    outline_rect = pg.Rect(x, y - fuel_bar_height - 10, fuel_bar_width, fuel_bar_height)
    fill_rect = pg.Rect(x, y - fuel_bar_height - 10, fill, fuel_bar_height)
    pg.draw.rect(window, (255, 0, 0), fill_rect)
    pg.draw.rect(window, (0, 0, 0), outline_rect, 2)

  def draw_loaded_state(self, window):
    font = pg.font.Font(None, 25)
    text = font.render('Loaded' if self.loaded_ore else '', True, (0, 0, 0))
    x, y = self.position
    window.blit(text, (x, y - 30))

  def draw(self, window):
    if self.visible:
      window.blit(self.image, self.position)
      self.draw_fuel_bar(window)
      self.draw_loaded_state(window)

  def update(self, dt):
    keys = pg.key.get_pressed()
    boundaries = pg.display.get_surface().get_rect()
    x, y = self.position

    if any([keys[pg.K_LEFT], keys[pg.K_RIGHT], keys[pg.K_UP], keys[pg.K_DOWN], keys[pg.K_a], keys[pg.K_d], keys[pg.K_w], keys[pg.K_s]]):
      self.fuel_amount = max(0, self.fuel_amount - self.fuel_consumption * dt)

    if keys[pg.K_LEFT] or keys[pg.K_a]:
      x = max(0, x - self.speed)
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
      x = min(boundaries.width - self.rect.width, x + self.speed)
    if keys[pg.K_UP] or keys[pg.K_w]:
      y = max(0, y - self.speed)
    if keys[pg.K_DOWN] or keys[pg.K_s]:
      y = min(boundaries.height - self.rect.height, y + self.speed)

    self.rect.topleft = self.position = (x, y)

  def reset(self):
    super().reset()
    self.fuel_amount = 100
    self.loaded_ore = 0