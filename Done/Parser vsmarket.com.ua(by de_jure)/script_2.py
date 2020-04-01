'''Parser vsmarket.com.ua (by de_jure)
16.02.20 - 20.02.20

My Telegram: @de_jure_contora
'''
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm
from time import sleep

sections = [
	'https://vsmarket.com.ua/chehly/xiaomi/',
	'https://vsmarket.com.ua/chehly/samsung/',
	'https://vsmarket.com.ua/chehly/huawei/',
	'https://vsmarket.com.ua/chehly/meizu/',
	'https://vsmarket.com.ua/chehly/asus/',
	'https://vsmarket.com.ua/apple/iphone/',
	'https://vsmarket.com.ua/chehly/bravis/',
	'https://vsmarket.com.ua/chehly/ergo/',
	'https://vsmarket.com.ua/chehly/fly/',
	'https://vsmarket.com.ua/chehly/htc/',
	'https://vsmarket.com.ua/chehly/lenovo/',
	'https://vsmarket.com.ua/chehly/lg/',
	'https://vsmarket.com.ua/chehly/nokia/',
	'https://vsmarket.com.ua/chehly/nomi/',
	'https://vsmarket.com.ua/chehly/prestigio/',
	'https://vsmarket.com.ua/chehly/sony/',
	'https://vsmarket.com.ua/chehly/vivo/',
	'https://vsmarket.com.ua/chehly/zte/',
	'https://vsmarket.com.ua/chehly/universal/',
	'https://vsmarket.com.ua/chehly/glass/',
	'https://vsmarket.com.ua/chehly/tablets/',
	'https://vsmarket.com.ua/chehly/plenki/',
	'https://vsmarket.com.ua/kabeli-i-zaryadki/zaryadnyie-ustroystva/',
	'https://vsmarket.com.ua/kabeli-i-zaryadki/cable/',
	'https://vsmarket.com.ua/powerbank-i-akkumulyatory/akkumulyatory/',
	'https://vsmarket.com.ua/powerbank-i-akkumulyatory/powerbank/',
	'https://vsmarket.com.ua/kompyuternye-aksessuary-i-akustika/mouse/',
	'https://vsmarket.com.ua/aksessuary/bluetooth/',
	'https://vsmarket.com.ua/aksessuary/fm-modulyatory/',
	'https://vsmarket.com.ua/aksessuary/mp3/',
	'https://vsmarket.com.ua/aksessuary/usb-zazhigalki/',
	'https://vsmarket.com.ua/aksessuary/usb-haby-i-kartridery/',
	'https://vsmarket.com.ua/aksessuary/avtoderzhateli/',
	'https://vsmarket.com.ua/aksessuary/detskie-chasy-s-gps/',
	'https://vsmarket.com.ua/aksessuary/zaschitnye-plenki/',
	'https://vsmarket.com.ua/aksessuary/karty-pamyati/',
	'https://vsmarket.com.ua/aksessuary/monopody/',
	'https://vsmarket.com.ua/aksessuary/naushniki/',
	'https://vsmarket.com.ua/aksessuary/popsockets/',
	'https://vsmarket.com.ua/aksessuary/portativnaya-akustika/',
	'https://vsmarket.com.ua/aksessuary/prikoly/',
	'https://vsmarket.com.ua/aksessuary/remeshki-dlya-chasov/',
	'https://vsmarket.com.ua/aksessuary/setevye-filtry-i-udliniteli/',
	'https://vsmarket.com.ua/aksessuary/smart-chasy-i-fitnes-trekery/',
	'https://vsmarket.com.ua/aksessuary/spinnery/',
	'https://vsmarket.com.ua/aksessuary/stilusy/',
	'https://vsmarket.com.ua/zapchasti/korpusa-dlya-mobilnyh-telefonov/',
	'https://vsmarket.com.ua/apple/watch/',
	'https://vsmarket.com.ua/apple/macbook/',
	'https://vsmarket.com.ua/apple/cover-airpods/'
]

sections_names = [
	'chehly/xiaomi/',
	'chehly/samsung/',
	'chehly/huawei/',
	'chehly/meizu/',
	'chehly/asus/',
	'apple/iphone/',
	'chehly/bravis/',
	'chehly/ergo/',
	'chehly/fly/',
	'chehly/htc/',
	'chehly/lenovo/',
	'chehly/lg/',
	'chehly/nokia/',
	'chehly/nomi/',
	'chehly/prestigio/',
	'chehly/sony/',
	'chehly/vivo/',
	'chehly/zte/',
	'chehly/universal/',
	'chehly/glass/',
	'chehly/tablets/',
	'chehly/plenki/',
	'kabeli-i-zaryadki/zaryadnyie-ustroystva/',
	'kabeli-i-zaryadki/cable/',
	'powerbank-i-akkumulyatory/akkumulyatory/',
	'powerbank-i-akkumulyatory/powerbank/',
	'kompyuternye-aksessuary-i-akustika/mouse/',
	'aksessuary/bluetooth/',
	'aksessuary/fm-modulyatory/',
	'aksessuary/mp3/',
	'aksessuary/usb-zazhigalki/',
	'aksessuary/usb-haby-i-kartridery/',
	'aksessuary/avtoderzhateli/',
	'aksessuary/detskie-chasy-s-gps/',
	'aksessuary/zaschitnye-plenki/',
	'aksessuary/karty-pamyati/',
	'aksessuary/monopody/',
	'aksessuary/naushniki/',
	'aksessuary/popsockets/',
	'aksessuary/portativnaya-akustika/',
	'aksessuary/prikoly/',
	'aksessuary/remeshki-dlya-chasov/',
	'aksessuary/setevye-filtry-i-udliniteli/',
	'aksessuary/smart-chasy-i-fitnes-trekery/',
	'aksessuary/spinnery/',
	'aksessuary/stilusy/',
	'zapchasti/korpusa-dlya-mobilnyh-telefonov/',
	'apple/watch/',
	'apple/macbook/',
	'apple/cover-airpods/'
]

def pars1(link):
	good_links = []
	browser.get(link)
	while True:
		soup = BeautifulSoup(browser.page_source, 'lxml')
		try:
			if 'Показать' in soup.find('span', class_='main').text:
				browser.send_keys('End')
			else:
				break
		except:
			break
	try:
		divs = soup.find_all('div', 'cat-title')
		if len(divs) != 0:
			for div in divs:
				good_links.append(div.find('a')['href'])
		else:
			good_links.append(link)
	except:
		good_links.append(link)
	print('[Этап 1] Завершён')
	return good_links

def pars2(links):
	good_links = []
	for link in tqdm(links):
		browser.get(link)
		sleep(1)
		while True:
			soup = BeautifulSoup(browser.page_source, 'lxml')
			try:
				if 'Показать' in soup.find('span', class_='main').text:
					browser.send_keys('End')
				else:
					break
			except:
				break
		divs = soup.find_all('div', class_='ty-grid-list__item-name')
		try:
			for div in divs:
				if div.find('a')['href'] in good_links:
					pass
				else:
					good_links.append(div.find('a')['href'])
		except:
			good_links.append(link)
	print('[Этап 2] Завершён')
	return good_links

def pars3(links):
	good_data = []
	for link in tqdm(links):
		try:
			while True:
				try:
					browser.get(link)
					sleep(3)
					soup = BeautifulSoup(browser.page_source, 'lxml')
					name = soup.find('h1', class_='ty-product-block-title').text
					if name != None:
						break
					else:
						input('\nСмените IP и нажмите ENTER')
				except:
					input('\nСмените IP и нажмите ENTER')
			try:
				description = soup.find('div', id='content_description').text
				try:
					if description == '' or description == '\n':
						description = 'None'
				except:
					description = 'None'
			except:
				description = 'None'
			#
			try:
				divs1 = soup.find_all('span', class_='ty-product-feature__label')
				divs2 = soup.find_all('div', class_='ty-product-feature__value')
				if len(divs1) > len(divs2):
					divs1.remove(divs1[0])
			except:
				divs1, divs2 = [], []
			imgs = soup.find('div', class_='owl-wrapper').find_all('a')
			good_imgs = []
			for img in imgs:
				good_imgs.append(img['href'])
			price = soup.find('span', class_='ty-price').text
			data = {}
			data['Раздел'] = sections_names[number]
			data['Артикул'] = link.split('/')[-1].replace('.html', '')
			data['Название'] = name
			data['Описание'] = description
			data['Картинки'] = good_imgs
			try:
				for g in range(0, len(divs2)):
					data[divs1[g].text] = divs2[g].text
			except:
				pass
			data['Цена'] = price
			good_data.append(data)
			with open(exp_file, 'w') as file:
				json.dump(good_data, file, indent=4, separators=(',', ':'), ensure_ascii=False)
		except:
			print('\n[КОД 217] Пропустил ' + link)
			continue
	print('[Этап 3] Завершён')

# Point of entry
dPath = input('Введите путь к папке для сохранения (в формате C:/.../): ')
if dPath == '':
	dPath = ''
	print('Вы не указали путь. Назначен стандартный путь')
pName = input('Введите название .json файла: ')
if dPath == '':
	dPath = 'VSM_Q'
	print('Вы не указали название. Назначено стандартное название VSM_Q')
exp_file = dPath + pName + '.json'
print('Результаты будут сохранены в ' + exp_file)
print('\nРазделы:')
for i in range(0, 50):
	print(str(i) + '\t' + sections_names[i])
while True:
	number = int(input('\nВведите номер раздела: '))
	if number > -1 and number < 57:
		print('Выбран раздел ' + sections[number])
		all_ = input('Парсить все товары с раздела?(Y/N): ')
		if all_ == 'Y':
			all_ = True
			from_who = 0
		elif all_ == 'N':
			all_ = False
		else:
			all_ = True
			from_who = 0
		browser = webdriver.Firefox()
		links = pars1(sections[number])
		links = pars2(links)
		if all_ == False:
			from_who = int(input('\nНайдено ' + str(len(links)) + ' товаров. С какого начать? (0 - первый): '))
			if from_who == '':
				from_who = 0
		pars3(links[from_who:])
		browser.quit()
		print('Парсинг завершён')
		break
	else:
		print('Такого раздела не существует')
		continue
while True:
	pass