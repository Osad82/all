# Тесты над прокси

import requests
from bs4 import BeautifulSoup

url = 'https://free-proxy-list.net/'

x = requests.get(url)
if x.status_code == 200:
	print('Connected')
	soup = BeautifulSoup(x.content, 'lxml')
	soup = (soup.find('tbody')).find_all('tr')
	for i in soup:
		print(i)