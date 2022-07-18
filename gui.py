import os, sys
from filemover import moverFile
from threading import Thread
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
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.filechooser import FileChooserListLayout
from kivy.uix.filechooser import FileChooser
from kivy.uix.progressbar import ProgressBar
from kivy.metrics import dp

if (platform == "android"):
	from android.storage import primary_external_storage_path


class MyUI():
	def build(self):
		self.wind = Window
		#self.wind.size = (480, 854)
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height
		self.createScreenManager()
		return self.carousel

	def createScreenManager(self):
		#self.scman = ScreenManager()
		self.carousel = Carousel(loop=True)
		#self.scman.add_widget(self.carousel)
		self.screenMain = Screen(name="main")
		self.screenHelp = Screen(name="help")
		self.screenFileChoose = Screen(name="filechooser")

		#в какой пункт записывать полученный путь
		self.flagPath = 0

		self.bxMain = BoxLayout(orientation="vertical")

		self.lblInFilePath = Label(text="Откуда перемещаем файлы")
		if (platform == "android"):
			self.inFilePath = Button(text=primary_external_storage_path(),\
									on_press=self.goFchooser)
			self.fchoose = FileChooserIconView(path=primary_external_storage_path(), dirselect=True)
		else:
			self.inFilePath = Button(text=os.path.expanduser("~"),\
									on_press=self.goFchooser)
			self.fchoose = FileChooserIconView(path=os.path.expanduser("~"), dirselect=True)
		self.lblOutFilePath = Label(text="Куда перемещаем файлы")
		self.outFilePath = TextInput(text="SaveExt")
		self.lblExtFile = Label(text="Расширения перемещаемых файлов")
		self.extFile = TextInput(text='png jpg jpeg bmp')
		self.startMoveBtn = Button(text='Переместить',\
									on_press=self.startMoveFile)
		self.pb = ProgressBar()

		self.lblHelp = Label(text='''[b][color=0000ff]File Mover 1.0[/color][/b]\n\nПрограмма для перемещения файлов по [color=ff3333]расширению[/color]
Картинки: имя-картинки[color=ff3333].png[/color] - в этом случае расширение [color=ff3333]png[/color]
Расширения Вы заполняете самостоятельно или используете заданные по умолчанию.
Все найденные файлы с этими расширениями перемещаются в [color=ff3333]новый каталог[/color] и сортируются.
Цель: собрать все фото/видео/... на Вашем устройстве для удобного перемещения в один каталог.
Связаться с автором:
Вконтакте: [i][color=0000ff][ref=]vk.com/shurikkomyakov[/ref][/color][/i]
GitHub: [i][color=a6a0a6][ref=]github.com/Alexander-Komyakov[/ref][/color][/i]'''
							, halign="center", text_size=(self.wind_width-100,None), markup=True)
		self.screenHelp.add_widget(self.lblHelp)

		self.bxMain.add_widget(self.lblInFilePath)
		self.bxMain.add_widget(self.inFilePath)
		self.bxMain.add_widget(self.lblOutFilePath)
		self.bxMain.add_widget(self.outFilePath)
		self.bxMain.add_widget(self.lblExtFile)
		self.bxMain.add_widget(self.extFile)
		self.bxMain.add_widget(self.startMoveBtn)
		self.bxMain.add_widget(self.pb)

		self.screenMain.add_widget(self.bxMain)

		self.carousel.add_widget(self.screenMain)
		self.carousel.add_widget(self.screenFileChoose)
		self.carousel.add_widget(self.screenHelp)

		self.screenFileChoose.add_widget(self.fchoose)
		self.fchoose.bind(selection=self.clickFileChooser)

	def fchooseThSt(self):
		self.fm = moverFile(self.extFile.text.split(),\
							self.inFilePath.text,\
							self.outFilePath.text,\
							self.setProgressBar)

	def clickFileChooser(self, cap, cap2):
		self.inFilePath.text = str(self.fchoose.selection[0])

	def goFchooser(self, instance):
		self.carousel.load_next()


	def startMoveFile(self, cap):
		self.thFsChooser = Thread(target=self.fchooseThSt)
		self.thFsChooser.start()

	def setProgressBar(self, val, maxval):
		self.pb.value = val
		self.pb.max = maxval

if __name__ == "__main__":
	app = MyApp()
	app.run()
