import os
import PySimpleGUI as sg

table = [
	['A', 'B', 'C', 'D', 'E'],
	['F', 'G', 'H', 'I/J', 'K'],
	['L', 'M', 'N', 'O', 'P'],
	['Q', 'R', 'S', 'T', 'U'],
	['V', 'W', 'X', 'Y', 'Z']
]

subtable = [
	'A', 'B', 'C', 'D', 'E',
	'F', 'G', 'H', 'I/J', 'K',
	'L', 'M', 'N', 'O', 'P',
	'Q', 'R', 'S', 'T', 'U',
	'V', 'W', 'X', 'Y', 'Z'
]

'''Функция для зашифровки/разшифровки
Принимает такие параметры:
str message - сообщение.
list[list] table - таблица для работы
int how - вид работы(1 - зашифровка, -1 - разшифровка).

'''
def encodeDecode(message, table, how):
	code, done = [], ''
	if len(table) > 5:
		save = table.pop(-1)
	else:
		save = '13'
	for i in message:
		for k in table:
			for g in k:
				if i.upper() == g:
					code.append(str(table.index(k))+str(k.index(i.upper())))
					break
		if i.upper() in ['I', 'J']:
			code.append(save)
		elif i.upper() not in subtable:
			code.append(i)
		try:
			code.append(str(int(i)))
		except:
			pass
	for i in code:
		try:
			x, y = int(i[0]), int(i[1])		
			try:
				done += table[x+how][y]
			except:
				done += table[0][y]
		except:
			done += str(i)
	return done

'''Функция создаёт новую таблицу на основе ключа.
Принимает один параметр:
key - ключ для зашифровки/разшифровки

'''
def makeNewTable(key):
	uni = []
	for i in key:
		if i not in uni:
			uni.append(i)
	key = uni
	if len(key) <= 25:
		new_subtable = []
		for i in key:
			if i.upper() == 'I' or i.upper() == 'J':
				i = 'I/J'
			new_subtable.append(i.upper())
		for i in subtable:
			if i not in new_subtable:
				new_subtable.append(i)
			if len(new_subtable) == 25:
				break
		new_table = [[], [], [], [], []]
		for i in range(5):
			for k in range(5):
				if new_subtable[0] == 'I/J':
					save = str(i) + str(k)
				new_table[i].append(new_subtable.pop(0))
		new_table.append(save)
		return new_table
	else:
		return 'Error'

# Выбор цветовой схемы
sg.ChangeLookAndFeel('Default1')

# Создание интерфейса
layout = [
	[sg.Menu([['Info', ['About us']]], tearoff=False)],
	[sg.Text('Ключ:'), sg.Input(size=(33, None), key='key')],
	[sg.Multiline(size=(40, 10), key='input')],
	[sg.Button(button_text='Encode'), sg.Button(button_text='Decode'), sg.Cancel()]
]

# Вызов окна
window = sg.Window('Шифр Полібія', layout)

# Главный цикл
while True:
	event, values = window.Read()
	if event == 'Cancel' or event is None:
		break
	elif event == 'Encode':
		key = list(values['key'])
		try:
			if key == []:
				# Шифровка без ключа
				with open('result.txt', 'w') as file:
					file.write(encodeDecode(list(values['input']), table, 1))
				os.system('result.txt')
			else:
				for i in key:
					if i.upper() not in subtable and i.upper() not in ['I', 'J']:
						print('Помилка. Невiрно введений ключ.')
						break
				else:
					# Шифровка с ключом
					result = makeNewTable(key)
					if result == 'Error':
						print('Помилка. Ключ занадто довгий.')
					else:
						with open('result.txt', 'w') as file:
							file.write(encodeDecode(list(values['input']), result, 1))
						os.system('result.txt')
		except:
			print('Невірно введений ключ')
	elif event == 'Decode':
		key = list(values['key'])
		try:
			if key == []:
				# Разшифровка без ключа
				with open('result.txt', 'w') as file:
					file.write(encodeDecode(list(values['input']), table, -1))
				os.system('result.txt')
				
			else:
				for i in key:
					if i.upper() not in subtable and i.upper() not in ['I', 'J']:
						print('Помилка. Невiрно введений ключ.')
						break
				else:
					# Разшифровка с ключом
					result = makeNewTable(key)
					if result == 'Error':
						print('Помилка. Ключ занадто довгий.')
					else:
						with open('result.txt', 'w') as file:
							file.write(encodeDecode(list(values['input']), result, -1))
						os.system('result.txt')
		except:
			print('Невірно введений ключ')
	elif event == 'About us':
		layout2 = [
			[sg.Text('Курсова робота на тему:')],
			[sg.Text('Пiдстановочний шифр Палiбiя')],
			[sg.Text('Роботу виконав:')],
			[sg.Text('Студент 472 групи')],
			[sg.Text('Шиян Ярослав Анатолiйович')],
			[sg.Text('2020 р.')],
			[sg.Image(r'img.png')]
		]
		window2 = sg.Window('Про розробника', layout2)
		event, values = window2.read()
window.close()
