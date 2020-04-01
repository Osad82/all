from datetime import datetime
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
	[sg.Output(size=(46, None))],
	[sg.OK(), sg.Cancel()]
]
window = sg.Window('Дні народження', layout)

while True:
	event, values = window.Read()
	if event == 'Cancel' or event is None:
		break
	if event == 'OK':
		print('='*40)
		try:
			d, m, Y = values['day'], values['month'], values['year']
			if d == '29' and m in ['02', '2'] and int(Y)//4 == 0:
				step = 4
			else:
				step = 1
			dweek = datetime.strptime(d + m + Y, '%d%m%Y').isoweekday()
			while 1:
				Y = str(int(Y) + step)
				if int(Y) > 2100:
					break
				try:	
					if datetime.strptime(d + m + Y, '%d%m%Y').isoweekday() == dweek:
						if dweek == 1:
							w = 'Понеділок'
						elif dweek == 2:
							w = 'Вівторок'
						elif dweek == 3:
							w = 'Середа'
						elif dweek == 4:
							w = 'Четвер'
						elif dweek == 5:
							w = "П'ятниця"
						elif dweek == 6:
							w = 'Субота'
						elif dweek == 7:
							w = 'Неділя'
						print(d, m, Y, w)
				except:
					pass
		except:
			print('Помилка. Невірно введена дата.')
	elif event == 'Про розробника':
		
		layout2 = [
			[sg.Image(r'1.png')],
			[sg.Text('Курсова робота на тему:')],
			[sg.Text("Комп'ютерний додаток для роботи з календарем")],
			[sg.Text('Роботу виконав:')],
			[sg.Text('Студент 472 групи')],
			[sg.Text('Грициненко Денис Павлович')],
			[sg.Text('2020р.')]
		]
		window2 = sg.Window('Про розробника', layout2)
		event, values = window2.read()

window.close()