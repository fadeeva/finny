from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.text import LabelBase

import helpers

class KeyboardListener(Widget):
    def __init__(self, **kwargs):
        super(KeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('Keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if text == 'q': keyboard.window.close()
        helpers.get_cmnd_name(self.text, keycode)
        return True

class CashFlowLayout(BoxLayout):
    pass

class MainMenuLayout(BoxLayout):
    def on_button_click(self, widget):
        print(helpers.clean_text(widget.text))

class PV(RelativeLayout):
    def on_button_click(self, widget):
        print(helpers.clean_text(widget.text))
    
class FV(RelativeLayout):
    def on_button_click(self, widget):
        print(helpers.clean_text(widget.text))

class EARAPR(RelativeLayout):
    def on_button_click(self, widget):
        print(helpers.clean_text(widget.text))

class TextAndLabel(BoxLayout):
    pass

class finnyApp(App):
    def build(self):
        Window.clearcolor = (.06, .05, .1, 1)
        Window.size = (685, 710)
        return MainMenuLayout()
    
#    def close_app(self):
#        App.get_running_app().stop()
#        Window.close()
    
    def add_textbox(self):
            self.root.ids.ti_box.add_widget(TextAndLabel())


LabelBase.register(name='ClashDisplay Regular', fn_regular='fonts/ClashDisplay-Regular.ttf')
LabelBase.register(name='Consolas Regular', fn_regular='fonts/consola.ttf')
    
if __name__ == '__main__':
    finnyApp().run()