import random, time, hashlib, gui
from kivy.app import App
from kivy.base import runTouchApp, stopTouchApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.graphics import BorderImage
from kivy.uix.carousel import Carousel

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

class MyApp(App):
	def build(self):
		#self.wind = Window
		#self.wind.size = (480, 854)
		#self.wind_width = self.wind.width
		#self.wind_height = self.wind.height
		self.mainUI = gui.MyUI()
		return self.mainUI.build()

if __name__ == "__main__":
	app = MyApp()
	app.run()
