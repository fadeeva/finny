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

class FinnyLayout(BoxLayout):
    pass

class finnyApp(App):
    
    def build(self):
        Window.clearcolor = (.06, .05, .1, 1)
        Window.size = (685, 670)
        return FinnyLayout()


LabelBase.register(name='ClashDisplay Regular', fn_regular='fonts/ClashDisplay-Regular.ttf')
    
if __name__ == '__main__':
    finnyApp().run()