__author__ = 'Huvber'
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text="hello")

TestApp().run()