import pygame as pg
import pygame_gui as pgui


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pg.init()
pg.font.init()

pg.display.set_caption('Transporter Game')

window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
manager = pgui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
is_running = True

while is_running:
  td = clock.tick(60) / 1000.0

  for event in pg.event.get():
    if event.type == pg.QUIT:
      is_running = False

    manager.process_events(event)

  manager.update(td)

  window.fill((30, 30, 30))

  manager.draw_ui(window)

  pg.display.update()

pg.quit()