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

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import helpers

class MainMenuLayout(Screen):
    def __init__(self, **kwargs):
        super(MainMenuLayout, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('Keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if text == 'q': keyboard.window.close()
        if keycode[0] == 27: self.manager.current='main_menu'
        screen_name = helpers.get_cmnd_name(keycode)
        if screen_name:
            self.manager.current = screen_name
        
        return True

    def on_button_click(self, widget):
        print(helpers.clean_text(widget.text))
    


class StockInfoLayout(Screen):
    pass

class StockProfitLayout(Screen):
    pass

class CashFlowLayout(Screen):
    pass

class PortfolioManagementLayout(Screen):
    pass

class CFDLayout(Screen):
    pass

class FuturesLayout(Screen):
    pass

class OptionsLayout(Screen):
    pass

class MultipliersLayout(Screen):
    pass


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

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("finny.kv")
class finnyApp(App):
    def build(self):
        Window.clearcolor = (.06, .05, .1, 1)
        Window.size = (685, 710)
        
        wm = WindowManager()
        wm.add_widget(PortfolioManagementLayout(name='portfolio_management'))
        wm.add_widget(MainMenuLayout(name='main_menu'))
        
        wm.add_widget(StockInfoLayout(name='stock_info'))
        wm.add_widget(CashFlowLayout(name='cash_flow'))
        wm.add_widget(StockProfitLayout(name='stock_profit'))
        wm.add_widget(FuturesLayout(name='futures'))
        wm.add_widget(CFDLayout(name='cfd'))
        wm.add_widget(OptionsLayout(name='options'))
        wm.add_widget(MultipliersLayout(name='multipliers'))
           
        return wm
    
    def add_textbox(self):
            self.root.ids.ti_box.add_widget(TextAndLabel())


LabelBase.register(name='ClashDisplay Regular', fn_regular='fonts/ClashDisplay-Regular.ttf')
LabelBase.register(name='Consolas Regular', fn_regular='fonts/consola.ttf')
    
if __name__ == '__main__':
    finnyApp().run()