import pygame_gui as pgui
import pygame as pg

from .config import lang_keys


ELEMENT_HEIGHT = 50
ELEMENT_WIDTH = 200
MENU_PADDING = 50


class Manager:
  ui_elements = []

  def __init__(self, window, visible, config, debug):
    self.window = window
    self.visible = visible
    self.config = config
    self.start_pressed = False
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
    if event.type == pgui.UI_BUTTON_PRESSED:
      if event.ui_element == self.ui_elements[-1]:
        self.start_pressed = True
    else:
      self.manager.process_events(event)

  def update(self, dt):
    self.manager.update(dt)

  def draw_menu_bg(self):
    middle_x, middle_y = self.middles
    menu_x = middle_x - self.total_fields_width // 2 - (MENU_PADDING // 2)
    menu_y = middle_y - self.total_fields_height // 2 - (MENU_PADDING // 2)
    bg_rect = pg.Rect(menu_x, menu_y, self.total_fields_width + MENU_PADDING, self.total_fields_height + (MENU_PADDING * 2.5))
    pg.draw.rect(self.window, 'black', bg_rect)

  def draw(self, window):
    if self.visible:
      self.draw_menu_bg()
      self.manager.draw_ui(window)

  def set_config(self, config):
    self.config = config

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
        initial_text=str(self.config[key]),
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

  def get_config(self):
    values = {}
    for i in range(0, len(self.ui_elements) - 1, 2):
      key = self.ui_elements[i].text.lower().replace(' ', '_')
      value = self.ui_elements[i + 1].get_text()
      values[key] = int(value)
    return values
