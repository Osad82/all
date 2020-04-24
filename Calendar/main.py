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

		self.setMinimumSize(QSize(820, 500))            # Устанавливаем размеры
		self.setWindowTitle("Calendar")                 # Устанавливаем заголовок окна
		central_widget = QWidget(self)                  # Создаём центральный виджет
		self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет
		grid_layout = QGridLayout()                     # Создаём сетку
		central_widget.setLayout(grid_layout)
		now = datetime.now()
		days_in_month = calendar.monthrange(now.year, now.month)[1]
		
		# Создание интерфейса
		buttons_days = []
		for i in range(days_in_month):
			buttons_days.append(i+1)
		j = 0
		while True:
			for i in range(7):
				try:
					grid_layout.addWidget(QPushButton(str(buttons_days.pop(0)), self), j, i)
				except:
					break
			if buttons_days == []:
				break
			j += 1


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec())