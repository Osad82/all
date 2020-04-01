'''Parser gsmarena.com (by de_jure)
08.02.20 - 11.02.20

My Telegram: @de_jure_contora
'''
import json
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm

url = 'https://www.gsmarena.com/'
sections = [
	'https://www.gsmarena.com/samsung-phones-9.php',
	'https://www.gsmarena.com/apple-phones-48.php',
	'https://www.gsmarena.com/huawei-phones-58.php',
	'https://www.gsmarena.com/nokia-phones-1.php',
	'https://www.gsmarena.com/sony-phones-7.php',
	'https://www.gsmarena.com/lg-phones-20.php',
	'https://www.gsmarena.com/htc-phones-45.php',
	'https://www.gsmarena.com/motorola-phones-4.php',
	'https://www.gsmarena.com/lenovo-phones-73.php',
	'https://www.gsmarena.com/xiaomi-phones-80.php',
	'https://www.gsmarena.com/google-phones-107.php',
	'https://www.gsmarena.com/honor-phones-121.php',
	'https://www.gsmarena.com/oppo-phones-82.php',
	'https://www.gsmarena.com/realme-phones-118.php',
	'https://www.gsmarena.com/oneplus-phones-95.php',
	'https://www.gsmarena.com/vivo-phones-98.php',
	'https://www.gsmarena.com/meizu-phones-74.php',
	'https://www.gsmarena.com/blackberry-phones-36.php',
	'https://www.gsmarena.com/asus-phones-46.php',
	'https://www.gsmarena.com/alcatel-phones-5.php',
	'https://www.gsmarena.com/zte-phones-62.php',
	'https://www.gsmarena.com/microsoft-phones-64.php',
	'https://www.gsmarena.com/vodafone-phones-53.php',
	'https://www.gsmarena.com/energizer-phones-106.php',
	'https://www.gsmarena.com/cat-phones-89.php',
	'https://www.gsmarena.com/sharp-phones-23.php',
	'https://www.gsmarena.com/micromax-phones-66.php',
	'https://www.gsmarena.com/infinix-phones-119.php',
	'https://www.gsmarena.com/ulefone_-phones-124.php',
	'https://www.gsmarena.com/tecno-phones-120.php',
	'https://www.gsmarena.com/blu-phones-67.php',
	'https://www.gsmarena.com/acer-phones-59.php',
	'https://www.gsmarena.com/wiko-phones-96.php',
	'https://www.gsmarena.com/panasonic-phones-6.php',
	'https://www.gsmarena.com/verykool-phones-70.php',
	'https://www.gsmarena.com/plum-phones-72.php'
]

# Parsing of pages
def parsPages(links):
	pages_list = []
	for link in tqdm(links):
			while True:
				pages_list.append(link)
				browser.get(link)
				soup = BeautifulSoup(browser.page_source, 'lxml')
				try:
					soup.find('h1', class_='article-info-name').text
					try:
						divs = soup.find('div', class_ = 'nav-pages')
						divs = divs.find_all('a')
						for div in divs:
							href = div['href']
							pages_list.append(url + href)
					except:
						pass
					break
				except:
					input('\nСмените IP и нажмите ENTER')
	print('[Этап 1] Завершён')
	return pages_list

# Parsing of Models
def parsModels(links):
	models_links = []
	for link in tqdm(links):
		while True:
			try:
				browser.get(link)
				soup = BeautifulSoup(browser.page_source, 'lxml')
				divs = soup.find('div', class_='makers').find_all('li')
				for div in divs:
					href = div.find()['href']
					models_links.append(url + href)
				break
			except:
				input('\nСмените IP и нажмите ENTER')
	print('[Этап 2] Завершён')
	return models_links

# Parsing of model's attributes
def parsAttributes(links):
	good_data = []
	for link in tqdm(links):
		while True:
			try:
				browser.get(link)
				i_list = []
				k_list = []
				soup = BeautifulSoup(browser.page_source, 'lxml')
				name = soup.find('h1', class_='specs-phone-name-title').text
				i_list.append('name')
				k_list.append(name)
				img = (soup.find('div', class_='specs-photo-main')).find('img')['src']
				i_list.append('img')
				k_list.append(img)
				gDate = str(datetime.datetime.today().strftime('%d.%m.%Y'))
				i_list.append('gDate')
				k_list.append(gDate)
				divs = soup.find('div', id='specs-list')
				attrs_names = divs.find_all('td', class_='ttl')
				for i in attrs_names:
					try:
						i = i.find().text
						i_list.append(i)
					except:
						i_list.append('')
				attrs = divs.find_all('td', class_='nfo')
				for k in attrs:
					try:
						k = k.find().text
					except:
						try:
							k = k.text
						except:
							pass
					k_list.append(((k.encode('ascii', 'ignore')).decode('utf-8')).replace('\n', ''))
				data = {}
				for g in range(0, len(k_list)):
					data[i_list[g]] = k_list[g]
				good_data.append(data)
				with open(exp_file, 'w') as file:
					json.dump(good_data, file, indent=4, separators=(',', ':'))
				break
			except:
				input('\nСмените IP и нажмите ENTER')

# Point of entry
dPath = input('Введите путь к папке для сохранения (в формате C:/.../): ')
if dPath == '':
	dPath = ''
	print('Вы не указали путь. Назначен стандарнтый путь')
pName = input('Введите название .json файла: ')
if dPath == '':
	dPath = 'GSM_Q'
	print('Вы не указали название. Назначено стандарнтное название GSM_Q')
exp_file = dPath + pName + '.json'
print('Результаты будут сохранены в ' + exp_file + '\nПроцесс пошёл')
all_ = input('Парсить все товары?(Y/N): ')
if all_ == 'Y':
	all_ = True
	from_who = 0
elif all_ == 'N':
	all_ = False
else:
	all_ = True
	from_who = 0
browser = webdriver.Firefox()
links = parsModels(parsPages(sections))
if all_ == False:
	from_who = int(input('\nНайдено ' + str(len(links)) + ' товаров. С какого начать? (0 - первый): '))
	if from_who == '':
		from_who = 0
parsAttributes(links[from_who:])
print('[Этап 3] Завершён')
browser.quit()
print('Парсинг завершён')
while True:
	pass