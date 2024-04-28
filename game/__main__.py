import pygame as pg
from ui.manager import Manager as UIManager


DEBUG = True
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pg.init()
pg.font.init()

pg.display.set_caption('Transporter Game')

paused = True
is_running = True

window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ui_manager = UIManager(window, paused, DEBUG)
clock = pg.time.Clock()

while is_running:
  dt = clock.tick(60) / 1000.0

  for event in pg.event.get():
    if event.type == pg.QUIT:
      is_running = False
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE:
        ui_manager.set_ui_visibility(paused := not paused)

    ui_manager.process_events(event)

  ui_manager.update(dt)

  window.fill('white')

  ui_manager.draw_ui(window)

  pg.display.flip()

pg.quit()