#kivy заготовка
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import kivy
from kivy.uix.checkbox import CheckBox
#====================================================
Window.size = (400, 700)
#====================================================
class Menu(BoxLayout):
	pass
#====================================================
class MyApp(App):
	def build(self):
		return Menu()
#====================================================
if __name__ == "__main__":
	MyApp().run()
