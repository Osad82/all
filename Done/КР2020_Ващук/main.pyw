from datetime import datetime
import PySimpleGUI as gui

gui.ChangeLookAndFeel('Default1')
layout = [
	[gui.Menu([['Iнформацiя', ['Про розробника']]], tearoff=False)],
	[gui.Text('Початкова дата')],
	[gui.Text('Число\t\tМісяць\t\tРік')],
	[
		gui.Input(size=(14, None), key='day1'),
		gui.Input(size=(14, None), key='month1'),
		gui.Input(size=(14, None), key='year1')
	],
	[gui.Text('Кiнцева дата дата')],
	[gui.Text('Число\t\tМісяць\t\tРік')],
	[
		gui.Input(size=(14, None), key='day2'),
		gui.Input(size=(14, None), key='month2'),
		gui.Input(size=(14, None), key='year2')
	],
	[gui.Text('Рiзниця у днях:'), gui.Text('                         ', key='result')],
	[gui.Button('Розрахувати'), gui.Button('Вихiд')]
]
window = gui.Window('Рiзниця мiж датами', layout)

while True:
	event, values = window.Read()
	if event == 'Вихiд' or event is None:
		break
	if event == 'Розрахувати':
		try:
			t1 = datetime.strptime(values['day1'] + values['month1'] +\
				values['year1'], '%d%m%Y')
			t2 = datetime.strptime(values['day2'] + values['month2'] +\
				values['year2'], '%d%m%Y')
			window['result'].update(str(t2-t1).split()[0])
		except:
			print('Невiрно введена дата.')
	elif event == 'Про розробника':
		layout2 = [
			[gui.Image(r'image.png')],
			[gui.Text('Курсова робота на тему:')],
			[gui.Text('Розрахунок кiлькостi днiв мiж двома датами')],
			[gui.Text('Роботу виконав:')],
			[gui.Text('Студент 472 групи')],
			[gui.Text('Ващук Олександр Юрiйович')],
			[gui.Text('2020р.')]
		]
		window2 = gui.Window('Про розробника', layout2)
		event, values = window2.read()