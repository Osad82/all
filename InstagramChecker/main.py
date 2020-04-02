import PySimpleGUI as sg

sg.theme('Topanga')

layout = [
	[sg.Text('Путь к Excel таблице:')],
	[sg.Input(), sg.FileBrowse()],
	[sg.Output(size=(51, 30))],
	[sg.OK(), sg.Exit()]
]

window = sg.Window('InstagramCheker', layout)

while True:
	event, values = window.Read()
	if event == 'Exit' or event is None:
		break
	elif event == 'OK':
		# Начать обработку
		pass

window.close()