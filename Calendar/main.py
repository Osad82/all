from datetime import datetime
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt, QRect

class MainWindow(QMainWindow):
	# Переопределяем конструктор класса
	def __init__(self):
		# Обязательно нужно вызвать метод супер класса
		QMainWindow.__init__(self)

		self.setMinimumSize(QSize(820, 500))            # Устанавливаем размеры
		self.setWindowTitle("Calendar")                 # Устанавливаем заголовок окна
		central_widget = QWidget(self)                  # Создаём центральный виджет
		self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет
		grid_layout = QGridLayout()                     # Создаём сетку
		central_widget.setLayout(grid_layout)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec())