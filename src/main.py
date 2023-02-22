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

import re

class CashFlowLayout(BoxLayout):
    pass

class MainMenuLayout(BoxLayout):
    pass


def clean_text(dirty):
    dirty = dirty.replace('[/font]', '')
    dirty = dirty.replace('\n', ' ')
    dirty = re.sub(r'\[font=fonts\/[a-zA-Z0-9_-]*\]', '', dirty)
    return dirty.lower()

class PV(RelativeLayout):
    def on_button_click(self, widget):
        print(clean_text(widget.text))
    
class FV(RelativeLayout):
    def on_button_click(self, widget):
        print(clean_text(widget.text))

class EARAPR(RelativeLayout):
    def on_button_click(self, widget):
        print(clean_text(widget.text))


class TextAndLabel(BoxLayout):
    pass

class finnyApp(App):
    def build(self):
        Window.clearcolor = (.06, .05, .1, 1)
        Window.size = (685, 710)
        return MainMenuLayout()
    
    def add_textbox(self):
            self.root.ids.ti_box.add_widget(TextAndLabel())


LabelBase.register(name='ClashDisplay Regular', fn_regular='fonts/ClashDisplay-Regular.ttf')
LabelBase.register(name='Consolas Regular', fn_regular='fonts/consola.ttf')
    
if __name__ == '__main__':
    finnyApp().run()