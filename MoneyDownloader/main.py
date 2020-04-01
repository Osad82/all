import os
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm

link_1 = 'https://modsfire.com/9Ev3C4JDiB5q5EQ' # Ссылка на файл с ModsFire
link_2 = '' # 
link_3 = '' #
link_4 = '' #

useragent = {
	'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

# Ссылки для парсинга proxy
links = [
	'https://hidemy.name/ru/proxy-list/?type=s#list',
	'https://hidemy.name/ru/proxy-list/?start=64#list',
	'https://hidemy.name/ru/proxy-list/?start=128#list',
	'https://hidemy.name/ru/proxy-list/?start=192#list',
]

# Парсинг proxy
def pars_proxies():
	browser = webdriver.Firefox()
	for link in tqdm(links):
		browser.get(link)
		sleep(6)
		soup = BeautifulSoup(browser.page_source, 'lxml')
		divs = soup.find('div', class_='table_block').find_all('tr')
		for div in divs:
			data = div.find_all('td')
			# Дописываем найденный proxy в файл
			with open('proxyies_list.txt', 'a') as file:
				file.write(data[0].text + ':' + data[1].text + '\n')
	browser.quit()

def check_proxies():
	# Получение всех proxy
	with open('proxyies_list.txt', 'r') as file:
		data = file.read().splitlines()

	# Сохранение рабочих proxy в отдельный файл
	for i in tqdm(data):
		session = requests.Session()
		try:
			request = session.get('http://ya.ru/', proxies={'http://': i}, headers=useragent, timeout=5)
			if request.status_code == 200:
				with open('good.txt', 'a') as file:
					file.write(i + '\n')
		except requests.exceptions.ConnectionError:
			continue

def start():
	# Получение рабочих proxy с файла
	with open('good.txt', 'r') as file:
		proxies = file.read().splitlines()
	for proxy in tqdm(proxies):
		try:
			# Проверка прокси на работоспособность
			session = requests.Session()
			try:
				request = session.get('http://ya.ru/', proxies={'http://': proxy}, headers=useragent, timeout=5)
				if request.status_code == 200:
					pass
			except requests.exceptions.ConnectionError:
				continue

			# Настройка FireFox профиля
			proxy_host, proxy_port = proxy.split(':')
			fp = webdriver.FirefoxProfile()

			fp.set_preference("network.proxy.type", 1)
			fp.set_preference("network.proxy.http", proxy_host)
			fp.set_preference("network.proxy.http_port", int(proxy_port))
			fp.set_preference("network.proxy.https", proxy_host)
			fp.set_preference("network.proxy.https_port", int(proxy_port))
			fp.set_preference("network.proxy.ssl", proxy_host)
			fp.set_preference("network.proxy.ssl_port", int(proxy_port))
			fp.set_preference("network.proxy.ftp", proxy_host)
			fp.set_preference("network.proxy.ftp_port", int(proxy_port))
			fp.set_preference("network.proxy.socks", proxy_host)
			fp.set_preference("network.proxy.socks_port", int(proxy_port))
			fp.update_preferences()

			# Запуск процесса
			browser = webdriver.Firefox(firefox_profile=fp)
			try:
				browser.set_page_load_timeout(60)
				browser.get(link_1)
				sleep(5)
				browser.find_element_by_xpath('/html/body/div/section/div/div[4]/div[2]/a').click()
				browser.find_element_by_xpath('/html/body/div/section/div/div[4]/div[2]/a').click()
				os.remove('courseplay.zip')
				browser.quit()
			except:
				try:
					browser.quit()
				except:
					pass
		except:
			print('общая ошибка')
			continue
#pars_proxies()
#check_proxies()
start()