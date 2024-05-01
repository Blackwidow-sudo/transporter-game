import pygame as pg

from os import path

from ui import Manager as UIManager, default_config
from entities import Player, Enemy, Ore, Factory, GasStation


DEBUG = True
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
ASSET_PATH = path.join(path.dirname(__file__), 'assets')


def is_winnable(available_ore, collected_ore, win_amount):
  """Check if the player can still win the game."""
  return available_ore + collected_ore >= win_amount


def draw_game_over(window, won):
  """Draw the game over screen."""
  font_height = 100
  font = pg.font.Font(None, font_height)
  text = font.render('You won!' if won else 'Game Over!', True, (0, 0, 0))
  text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, font_height))
  window.blit(text, text_rect)


# Initialize pygame
pg.init()
pg.font.init()
pg.display.set_caption('Transporter Game')

# Initialize game state
paused = True
game_over = False
is_running = True
won = False

# Initialize game window
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ui_manager = UIManager(window, paused, default_config, DEBUG)
clock = pg.time.Clock()

# Instantiate entities
player = Player(
  x=SCREEN_WIDTH // 2,
  y=SCREEN_HEIGHT // 2,
  img_path=path.join(ASSET_PATH, 'truck.png'),
  scale=0.3,
  config=default_config
)
ore = Ore(
  x=SCREEN_WIDTH - 150,
  y=SCREEN_HEIGHT // 2,
  img_path=path.join(ASSET_PATH, 'ore.png'),
  scale=0.3,
  config=default_config
)
factory = Factory(
  x=0,
  y=SCREEN_HEIGHT // 2,
  img_path=path.join(ASSET_PATH, 'factory.png'),
  scale=0.3,
  config=default_config
)
gas_station = GasStation(
  x=SCREEN_WIDTH // 2,
  y=SCREEN_HEIGHT - 100,
  img_path=path.join(ASSET_PATH, 'gas_station.png'),
  scale=0.2
)
enemy = Enemy(
  x=0,
  y=0,
  img_path=path.join(ASSET_PATH, 'helicopter.png'),
  scale=0.5,
  config=default_config
)

# The order of entities is important for drawing
entities = [ore, factory, gas_station, player, enemy]

# Game loop
while is_running:
  dt = clock.tick(60) / 1000.0

  for event in pg.event.get():
    if event.type == pg.QUIT:
      is_running = False
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE and not game_over:
        paused = not paused

    ui_manager.process_events(event)
  
  ui_manager.set_ui_visibility(paused)

  # Update configs of entities
  current_config = ui_manager.get_config()

  for entity in entities:
    if hasattr(entity, 'set_config'):
      entity.set_config(current_config)

  if not paused:
    if not game_over:
      for entitiy in entities:
        entitiy.toggle_visibility(True)
    player.update(dt)
    enemy.update(player)
    
    # Check entity collisions
    if player.check_collision(enemy):
      stolen_ore = player.loaded_ore
      player.loaded_ore = 0
      if stolen_ore > 0:
        enemy.reset()
    if player.check_collision(ore) and not player.loaded_ore:
      ore.amount -= player.ore_capacity
      player.loaded_ore += player.ore_capacity
    if player.check_collision(factory):
      factory.ore += player.loaded_ore
      player.loaded_ore = 0
      game_over = won = factory.get_progress() >= 100
    if player.check_collision(gas_station):
      player.fuel_amount = 100
  
  if ui_manager.start_pressed:
    for entity in entities:
      entity.reset()
    paused = game_over = won = False
    ui_manager.start_pressed = False

  # Game over when player has no fuel or he cant win anymore
  can_win = is_winnable(ore.amount, factory.ore + player.loaded_ore, factory.get_required_win_amount())
  game_over = player.no_fuel() or won or not can_win

  paused = paused or game_over

  ui_manager.update(dt)

  # Draw everything
  window.fill('white')

  for entity in entities:
    entity.draw(window)

  ui_manager.draw(window)

  if game_over:
    draw_game_over(window, won)

  pg.display.flip()

pg.quit()