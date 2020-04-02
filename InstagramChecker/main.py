from selenium import webdriver
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import requests
from user import *

useragent = {
	'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' + \
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}	

def getData(browser, login, url):
	browser.get(url)
	soup = BeautifulSoup(browser.page_source, 'lxml')
	soup = (soup.find('ul', class_='k9GMp')).find_all('span', class_='g47SY')
	user = User(login, soup[0].text, soup[1].text, soup[2].text)
	return user

sg.theme('Black')
layout = [
	[sg.Text('Путь к .txt файлу с логинами:')],
	[sg.Input(key='input'), sg.FileBrowse()],
	[sg.Output(size=(51, 30))],
	[sg.OK(size=(35, None)), sg.Exit(size=(10, None))]
]
window = sg.Window('InstagramCheker', layout)

while True:
	event, values = window.Read()
	if event == 'Exit' or event is None:
		break
	elif event == 'OK':
		try:
			with open(values['input'], 'r') as file:
				accs = (file.read()).split('\n')
			print('Загружено {0} аккаунтов'.format(len(accs)))
			if requests.get('https://www.instagram.com/', 
					headers=useragent).status_code != 200:
				print('Ошибка подключения к Instagram')
			else:
				print('Соединение с Instagram установлено\n')
				browser = webdriver.Firefox()
				good_users = []
				for acc in accs:
					url = 'https://www.instagram.com/{0}/'.format(acc)
					try:
						user = getData(browser, acc, url)
						user.print()
						good_users.append(user)
					except:
						continue
				print('\nРабочих аккаунтов: {0}/{1}'.format(len(good_users), len(accs)))
				browser.quit()
		except:
			print('ОШИБКА. Неверно выбран файл.')
window.close()