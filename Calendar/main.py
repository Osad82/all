import sys
import calendar
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt, QRect

class MainWindow(QMainWindow):
	# Переопределяем конструктор класса
	def __init__(self):
		# Обязательно нужно вызвать метод супер класса
		QMainWindow.__init__(self)

		self.setMinimumSize(QSize(720, 400))            # Устанавливаем размеры
		self.setWindowTitle("Calendar")                 # Устанавливаем заголовок окна
		central_widget = QWidget(self)                  # Создаём центральный виджет
		self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет
		grid_layout = QGridLayout()                     # Создаём сетку
		central_widget.setLayout(grid_layout)
		now = datetime.now()
		days_in_month = calendar.monthrange(now.year, now.month)[1]
		
		# Создание интерфейса
		buttons_days = [i+1 for i in range(days_in_month)]
		j = 0
		while True:
			for i in range(7):
				try:
					btn = QPushButton(str(buttons_days.pop(0)), self)
					btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
					grid_layout.addWidget(btn, j, i)
				except:
					break
			if buttons_days == []:
				break
			j += 1
		plainText = QPlainTextEdit() # Создание TextInput'a
		plainText.setPlaceholderText('Text')
		grid_layout.addWidget(plainText, 0, 7, 5, 5) # Размещение TextInput'a

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec())