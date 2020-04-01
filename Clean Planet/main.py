import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar



Window.size = (320, 400)

class Menu(BoxLayout):
	pass

class MyApp(App):
	def build(self):
		return Menu()

if __name__ == "__main__":
	MyApp().run()