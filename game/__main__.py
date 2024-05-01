import pygame as pg
from os import path

from ui import Manager as UIManager, default_config
from entities import Player, Enemy, Ore, Factory, GasStation


DEBUG = True
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
ASSET_PATH = path.join(path.dirname(__file__), 'assets')


def init_game():
  pass


pg.init()
pg.font.init()

pg.display.set_caption('Transporter Game')

paused = True
game_over = False
is_running = True
won = False

window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ui_manager = UIManager(window, paused, default_config, DEBUG)
clock = pg.time.Clock()

player_config = {
  'speed': default_config['player_speed'],
  'fuel_capacity': default_config['fuel_capacity'],
  'fuel_consumption': default_config['fuel_consumption'],
  'ore_capacity': default_config['ore_capacity']
}

enemy_config = {
  'speed': default_config['enemy_speed']
}

player = Player(
  x=SCREEN_WIDTH // 2,
  y=SCREEN_HEIGHT // 2,
  img_path=path.join(ASSET_PATH, 'truck.png'),
  scale=0.3,
  config=player_config
)
ore = Ore(
  x=SCREEN_WIDTH - 150,
  y=SCREEN_HEIGHT // 2,
  img_path=path.join(ASSET_PATH, 'ore.png'),
  capacity=default_config['ore_amount'],
  scale=0.3
)
factory = Factory(
  x=0,
  y=SCREEN_HEIGHT // 2,
  img_path=path.join(ASSET_PATH, 'factory.png'),
  scale=0.3,
  win_threshold=default_config['win_threshold'],
  ore_amount=default_config['ore_amount']
)
gas_station = GasStation(
  x=SCREEN_WIDTH // 2,
  y=SCREEN_HEIGHT - 100,
  img_path=path.join(ASSET_PATH, 'gas_station.png'),
  scale=0.2
)
enemy = Enemy(x=0, y=0, img_path=path.join(ASSET_PATH, 'helicopter.png'), scale=0.5, config=enemy_config)

entities = [player, enemy, ore, factory, gas_station]

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
  player.set_config(ui_manager.get_config())
  enemy.set_config(ui_manager.get_config())

  if not paused and not game_over:
    for entitiy in entities:
      entitiy.visible = True
    player.update(dt)
    enemy.update(player)
    
    # Check entity collisions
    if player.check_collision(enemy) or player.no_fuel():
      game_over = True
      paused = True
    if player.check_collision(ore) and not player.loaded_ore:
      ore.capacity -= player.ore_capacity
      player.loaded_ore += player.ore_capacity
    if player.check_collision(factory):
      factory.ore += player.loaded_ore
      player.loaded_ore = 0
    if player.check_collision(gas_station):
      player.fuel_capacity = 100
  
  if ui_manager.start_pressed:
    for entity in entities:
      entity.reset()
    paused = False
    game_over = False
    ui_manager.start_pressed = False

  ui_manager.update(dt)

  window.fill('white')

  ore.draw(window)
  factory.draw(window)
  gas_station.draw(window)
  player.draw(window)
  enemy.draw(window)
  ui_manager.draw(window)

  pg.display.flip()

pg.quit()