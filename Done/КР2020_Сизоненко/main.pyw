from datetime import datetime, timedelta
import PySimpleGUI as sg

sg.ChangeLookAndFeel('Default1')
layout = [
	[sg.Menu([['Iнформацiя', ['Про розробника']]], tearoff=False)],
	[sg.Text('Число\t\tМісяць\t\tРік')],
	[
		sg.Input(size=(14, None), key='day'),
		sg.Input(size=(14, None), key='month'),
		sg.Input(size=(14, None), key='year')
	],
	[sg.Text('Кiлькiсть днiв:   '), sg.Input(size=(14, None), key='days')],
	[sg.Text('                 ', key='result')],
	[sg.Button('Розрахувати'), sg.Button('Вихiд')]
]
window = sg.Window('Рiзниця мiж датами', layout)
while True:
	event, values = window.Read()
	if event == 'Вихiд' or event is None:
		break
	elif event == 'Розрахувати':
		try:
			date = datetime.strptime(values['day'] + values['month'] +\
				values['year'], '%d%m%Y')
			result = date + timedelta(int(values['days']))
			window['result'].update(str(result.day) + '.' + \
									str(result.month) + '.' + \
									str(result.year))
		except:
			window['result'].update('Помилка')
	elif event == 'Про розробника':
		layout2 = [
			[sg.Image(r'img.png')],
			[sg.Text('Курсова робота на тему:')],
			[sg.Text('Визначення дати, яка наступить через визначену кількість днів')],
			[sg.Text('Роботу виконав:')],
			[sg.Text('Студент 472 групи')],
			[sg.Text('Сизоненко Артем Олександрович')],
			[sg.Text('2020р.')]
		]
		window2 = sg.Window('Про розробника', layout2)
		event, values = window2.read()