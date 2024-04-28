import pygame_gui as pgui
import pygame as pg


ELEMENT_HEIGHT = 50
ELEMENT_WIDTH = 200
MENU_PADDING = 50

lang_keys = {
  'fuel_cap': 'Enter fuel capacity:',
  'fuel_consum': 'Enter fuel consumption:',
  'ore_cap': 'Enter ore capacity:',
  'player_speed': 'Enter player speed:',
  'enemy_speed': 'Enter enemy speed:',
  'win_threshold': 'Enter win threshold:',
}

default_config = {
  'fuel_cap': 100,
  'fuel_consum': 10,
  'ore_cap': 100,
  'player_speed': 1,
  'enemy_speed': 1,
  'win_threshold': 100,
}


class Manager:
  ui_elements = []

  def __init__(self, window, visible, debug=False):
    self.window = window
    self.visible = visible
    self.manager = pgui.UIManager(window.get_size())
    self.manager.set_visual_debug_mode(debug)
    # Calculate some values that are needed for the UI
    self.window_width, self.window_height = self.window.get_size()
    self.middles = (self.window_width // 2, self.window_height // 2)
    self.total_fields_height = len(lang_keys) * ELEMENT_HEIGHT
    self.total_fields_width = 2 * ELEMENT_WIDTH

    self.draw_menu_bg()
    self.create_elements()

  def process_events(self, event):
    self.manager.process_events(event)

  def update(self, dt):
    self.manager.update(dt)

  def draw_menu_bg(self):
    middle_x, middle_y = self.middles
    menu_x = middle_x - self.total_fields_width // 2 - (MENU_PADDING // 2)
    menu_y = middle_y - self.total_fields_height // 2 - (MENU_PADDING // 2)
    bg_rect = pg.Rect(menu_x, menu_y, self.total_fields_width + MENU_PADDING, self.total_fields_height + (MENU_PADDING * 2.5))
    pg.draw.rect(self.window, 'black', bg_rect)

  def draw_ui(self, window):
    self.draw_menu_bg() if self.visible else None
    self.manager.draw_ui(window)

  def set_ui_visibility(self, visible):
    self.visible = visible
    for el in self.ui_elements:
      el.show() if visible else el.hide()

  def create_elements(self):
    middle_x, middle_y = self.middles
    self.menu_dimensions = (self.total_fields_width, self.total_fields_height)
    x, y = (middle_x - self.total_fields_width // 2, middle_y - self.total_fields_height // 2)

    for key, value in lang_keys.items():
      self.ui_elements.append(pgui.elements.UILabel(
        relative_rect=pg.Rect((x, y), (ELEMENT_WIDTH, ELEMENT_HEIGHT)),
        text=value,
        manager=self.manager
      ))

      input_field = pgui.elements.UITextEntryLine(
        relative_rect=pg.Rect((x + ELEMENT_WIDTH, y), (ELEMENT_WIDTH, ELEMENT_HEIGHT)),
        initial_text=str(default_config[key]),
        manager=self.manager
      )

      input_field.set_text_length_limit(3)
      input_field.set_allowed_characters('numbers')

      self.ui_elements.append(input_field)

      y += 50

    self.ui_elements.append(pgui.elements.UIButton(
      relative_rect=pg.Rect((middle_x - 100, middle_y + self.total_fields_height // 2 + (ELEMENT_HEIGHT // 2)), (200, ELEMENT_HEIGHT)),
      text='Start',
      manager=self.manager
    ))

  def get_values(self):
    values = {}
    for i in range(0, len(self.ui_elements), 2):
      key = self.ui_elements[i].text.lower().replace(' ', '_')
      value = self.ui_elements[i + 1].get_text()
      values[key] = int(value)
    return values
