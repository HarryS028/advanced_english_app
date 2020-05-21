import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp 

class MainWindow(Screen):
    pass

class PlayWindow(Screen):
    pass

class SearchWindow(Screen):
    pass

class PreferenceWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file("main.kv")
        return kv

if __name__ == "__main__":
    MyApp().run()

