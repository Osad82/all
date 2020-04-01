# -*- coding: cp1251 -*-
#by de_jure
#main.py
#14.01.20(вечер) - 05.02.20

import datetime
import time
import sqlite3
import telebot
from toolbox import *


bot = telebot.TeleBot('979495669:AAGw92_pC3Wf_lruyVC_ganYndDddokf9Yo')
warns_max = 3
menu = '☕️☕️☕️☕️☕️\nЭспрессо 14/22\nАмерикано 14/24\nКапучино 23/25/28\nЛатте 24/28/32\nРаф 30/37/45' + \
							'\nКакао 20/25/30\nФлэт Уайт 35\nЧай 15\nГорячий шоколад 23/28/33\n☕️☕️☕️☕️☕️'
modersid_online = []
modersid = []
adminsid = []
password = '6896343'
orders = []
orders_2 = []
global addadmin, addmoder, deladmin, orderspersm
addadmin = False
addmoder = False
deladmin = False
orderspersm = 0
global communication_id, communication_id_moder
global unban
unban = False
communication_id = None
communication_id_moder = None
db.createdb()
db.mdrsim(modersid)
db.admsim(adminsid)


# Загрузка цен из файла
file = open('price.txt', 'r')
prices = {}
f = file.read().splitlines()
for line in f:
	k = line.split('=')[0]
	a = line.split('=')[1]
	prices[k] = a
file.close()

# Открытие файла для логов
log_data = str(datetime.datetime.today().strftime("%d%m%Y_%H%M%S"))
log = open('logs/log_' + log_data + '.txt', 'a')
log.write(str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + ' [BOT] Я включился\n')
print(str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + ' [BOT] Я включился')
log.close()

# Взять меню
#file_menu = open('menu.txt', 'r')
#menu = file_menu.read()
#file_menu.close()



'''Главные функции
/start, регистрация, авторизация, 'меню', 'моя статистика', 'отмена'.

'''
class main:
	# Проверка регистрации пользователя
	@bot.message_handler(commands=['start'])
	def start(message):
		if db.finduser(message) == None:
			bot.send_message(message.chat.id, 'Поделитесь своим номером, чтобы пройти регистрацию.\n' +\
				'Обещаем не звонить ночью🙈', \
				reply_markup=board.send_phone)
		else:
			if db.whatwrns(message) < warns_max:
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
			else:
				bot.send_message(message.from_user.id, 'Ваш аккаунт заблокирован😡. Обратитесь к модератору.')
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
	# Отсекание стикеров
	@bot.message_handler(content_types=['sticker', 'voice', 'audio', 'document', 'photo', 'video', 'video_note', \
		'location'])
	def goaway(message):
		pass
	
	# Получение номера телефона и регистрация пользователя
	@bot.message_handler(content_types=['contact'])
	def read_contact_phone(message):
		if db.finduser(message) == None:
			if message.contact.phone_number[0] == '+':
				message.contact.phone_number = message.contact.phone_number[1:]
			db.createuser(message)
			bot.send_message(message.from_user.id, 'Регистрация успешно завершена😅')
			if db.whatwrns(message) < warns_max:
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
			else:
				bot.send_message(message.from_user.id, 'Ваш аккаунт заблокирован😡. Обратитесь к модератору.')
		else:
			bot.send_message(message.from_user.id, 'Вы уже зарегистрированы')
			if db.whatwrns(message) < warns_max:
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
			else:
				bot.send_message(message.from_user.id, 'Ваш аккаунт заблокирован😡. Обратитесь к модератору.')
	# Кнопка 'Меню'
	@bot.message_handler(func=lambda message: message.text.lower() == 'меню')
	def show_menu(message):
		try:
			db.ordrsqu(message)
			bot.send_message(message.chat.id, menu)
		except:
			pass
	# Кнопка 'Моя статистика'
	@bot.message_handler(func=lambda message: message.text.lower() == 'моя статистика')
	def mystats(message):
		try:
			bot.send_message(message.chat.id, '📊Статистика📊\n\n' + 
								'Мой ID-номер: ' + str(message.from_user.id) + 
								'\nВсего сделано заказов: ' + str(db.ordrsqu(message)) + 
								'\nМои выговоры: ' + str(db.whatwrns(message)) + 
								'\n\n')
		except:
			pass
	# Кнопка 'Отмена'
	@bot.message_handler(func=lambda message: message.text.lower() == 'отмена')
	def cencel(message):
		try:
			try:
				orders.remove(find_order(message, orders))
			except:
				pass
			bot.send_message(message.from_user.id, '☹️')
			db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass


'''Функции администрации
Админпанель, модерпанель, кол-во пользователей, добавление модератора и администратора, удаление модератора и
администратора, список всех модеров/админов, принятие и сдача смены модератора.

'''
class adm:
	# Открывает админпанель
	@bot.message_handler(func=lambda message: message.text.lower() == 'админ. меню')
	def admin_menu(message):
		if message.from_user.id in adminsid:
			bot.send_message(message.chat.id, 'adminpanel', reply_markup = board.adminmenu)
	# Открывает модерпанель
	@bot.message_handler(func=lambda message: message.text.lower() == 'модер. меню')
	def moder_menu(message):
		if message.from_user.id in modersid:
			bot.send_message(message.chat.id, 'moderpanel', reply_markup = board.modermenu)
		else:
			if message.from_user.id in adminsid:
				bot.send_message(message.chat.id, 'Вы не являетесь модератором', reply_markup = board.mainmenu2)
	# Отображает кол-во пользователей
	@bot.message_handler(func=lambda message: message.text.lower() == 'кол-во пользователей')
	def urskolvo(message):
		if message.from_user.id in adminsid:
			bot.send_message(message.chat.id, 'Всего пользователей: ' + str(db.kolvo()))
	# Отображает кол-во модераторов онлайн
	@bot.message_handler(func=lambda message: message.text.lower() == 'модераторы online')
	def modonline(message):
		if message.from_user.id in adminsid:
			bot.send_message(message.chat.id, 'Модераторов Online: ' + str(len(modersid_online)))
	# Добавление модератора
	@bot.message_handler(func=lambda message: message.text.lower() == 'добавить модератора')
	def add_moder(message):
		if message.from_user.id in adminsid:
			global addmoder
			addmoder = True
			bot.send_message(message.chat.id, 'Введите номер телефона нового модератора' \
																	'(в формате 380*********)')
	# Добавление администратора
	@bot.message_handler(func=lambda message: message.text.lower() == 'добавить администратора')
	def add_admin(message):
		if message.from_user.id in adminsid:
			global addadmin
			addadmin = True
			bot.send_message(message.chat.id, 'Введите номер телефона нового администратора' \
																	'(в формате 380*********)')
	# Удаление с поста администратора/модератора.
	@bot.message_handler(func=lambda message: message.text.lower() in ['удалить администратора',
																		'удалить модератора'])
	def del_admin(message):
		if message.from_user.id in adminsid:
			global deladmin
			deladmin = True
			bot.send_message(message.chat.id, 'Введите номер телефона этого человека' \
																	'(в формате 380*********)')
	# Разбан
	@bot.message_handler(func=lambda message: message.text.lower() == 'разбан')
	def unban(message):
		if message.from_user.id in adminsid:
			global unban
			unban = True
			bot.send_message(message.chat.id, 'Введите ID этого человека')
	# Отображает список администраторов.
	@bot.message_handler(func=lambda message: message.text.lower() == 'список администраторов')
	def adminlist(message):
		if message.from_user.id in adminsid:
			db.showall(message, bot, 2)
	# Отображает список модераторов.
	@bot.message_handler(func=lambda message: message.text.lower() == 'список модераторов')
	def adminlist(message):
		if message.from_user.id in adminsid:
			db.showall(message, bot, 1)
	# Принятие смены.
	@bot.message_handler(func=lambda message: message.text.lower() == 'принять смену')
	def acceptsm(message):
		if message.from_user.id in modersid:
			if message.from_user.id in modersid_online:
				bot.send_message(message.chat.id, 'Вы уже вышли на смену')
			else:
				modersid_online.append(message.from_user.id)
				bot.send_message(message.chat.id, 'Вы вышли на смену', reply_markup = board.mainmenu1)
				msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
					' [MODER ' + str(message.from_user.id) + '] Вышел на смену'
				log = open('logs/log_' + log_data + '.txt', 'a')
				log.write(msg + '\n')
				log.close()
				print(msg)
	# Сдача смены
	@bot.message_handler(func=lambda message: message.text.lower() == 'сдать смену')
	def acceptsm(message):
		if message.from_user.id in modersid:
			if message.from_user.id in modersid_online:
				global orderspersm
				modersid_online.remove(message.from_user.id)
				bot.send_message(message.chat.id, 'Вы сдали смену', reply_markup = board.mainmenu1)
				bot.send_message(message.chat.id, 'Выполнено заказов: ' + str(orderspersm), \
					reply_markup = board.mainmenu1)
				msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
					' [MODER ' + str(message.from_user.id) + '] Сдал смену'
				log = open('logs/log_' + log_data + '.txt', 'a')
				log.write(msg + '\n')
				log.close()
				print(msg)
				if len(modersid_online) == 0:
					orderspersm = 0
			else:
				bot.send_message(message.chat.id, 'Вы не выходили на смену')
	# Разрыв связи модератора с пользователем
	@bot.message_handler(func=lambda message: message.text.lower() == 'разорвать связь')
	def endconnect(message):
		global communication_id_moder, communication_id
		if message.from_user.id in modersid:
			try:
				if message.from_user.id == communication_id_moder:
					bot.send_message(communication_id, 'Модератор закрыл чат')
					msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
						' [MODER ' + str(communication_id_moder) + \
						'] Прервал связь с ' + str(communication_id)
					log = open('logs/log_' + log_data + '.txt', 'a')
					log.write(msg + '\n')
					log.close()
					print(msg)
					communication_id = None
					communication_id_moder = None
					bot.send_message(message.from_user.id, 'Связь разорвана', reply_markup=board.mainmenu1)
				elif message.from_user.id in modersid:
					bot.send_message(message.from_user.id, 'Связь разорвана', reply_markup=board.mainmenu1)
			except:
					bot.send_message(message.from_user.id, 'Связь разорвана', reply_markup=board.mainmenu1)


'''Создание заказа
Создать заказ, выбор кофе, выбор размера и прибавка цены, выбор сахара, кнопка 'Готово', подтверждение заказа,
получение текстовых сообщений(ассорти).

Кофе:
Эспрессо
Американо
Капучино
Латте
Раф
Какао
Флэт Уайт
Чай
Горячий шоколад

Получение текстовых сообщений -- получение комментария или админ пароля, получение номера
телефона нового/удаляемого администратора или модератора.

Избранное и работа с ним

Callback для модераторов

'''
class crtorder:
	# Создать заказ.
	@bot.message_handler(func=lambda message: message.text.lower() == 'создать заказ')
	def crtor(message):
		try:
			if db.whatwrns(message) < warns_max:
				if len(modersid_online) != 0:
					zakaz = order()
					zakaz.Constructor(db.finduser(message)[1], message.from_user.id)
					zakaz.status_1 = 1
					orders.append(zakaz)
					bot.send_message(message.chat.id, 'Что желаете?😊', reply_markup = board.potablemenu0)
				else:
					bot.send_message(message.chat.id, 'В данный момент модераторов нет😴. Попробуйте позже')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
			else:
				bot.send_message(message.from_user.id, 'Ваш аккаунт заблокирован😡. Обратитесь к модератору.')
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Эспрессо.
	@bot.message_handler(func=lambda message: message.text.lower() == 'эспрессо')
	def espresso(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nЭспрессо'
						find_order(message, orders).buf = 'эспрессо'
						bot.send_message(message.chat.id, 'Какого размера?', reply_markup = board.espressosize)
						find_order(message, orders).status_1 = 2
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.espresso\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Американо.
	@bot.message_handler(func=lambda message: message.text.lower() == 'американо')
	def americano(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nАмерикано'
						find_order(message, orders).buf = 'американо'
						bot.send_message(message.chat.id, 'Какого размера?', reply_markup = board.americanosize)
						find_order(message, orders).status_1 = 2
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.americano\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Капучино.
	@bot.message_handler(func=lambda message: message.text.lower() == 'капучино')
	def capuchino(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nКапучино'
						find_order(message, orders).buf = 'капучино'
						bot.send_message(message.chat.id, 'Какого размера?', reply_markup = board.smlsize)
						find_order(message, orders).status_1 = 2
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.capuchino\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.smlsize)
		except:
			pass
	# Латте.
	@bot.message_handler(func=lambda message: message.text.lower() == 'латте')
	def latte(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nЛатте'
						find_order(message, orders).buf = 'латте'
						bot.send_message(message.chat.id, 'Какого размера?', reply_markup = board.smlsize)
						find_order(message, orders).status_1 = 2
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.latte\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Раф.
	@bot.message_handler(func=lambda message: message.text.lower() == 'раф')
	def raf(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nРаф'
						find_order(message, orders).buf = 'раф'
						bot.send_message(message.chat.id, 'Какого размера?', reply_markup = board.smlsize)
						find_order(message, orders).status_1 = 2
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.raf\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Какао.
	@bot.message_handler(func=lambda message: message.text.lower() == 'какао')
	def cacao(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nКакао'
						find_order(message, orders).buf = 'какао'
						bot.send_message(message.chat.id, 'Какого размера?', reply_markup = board.smlsize)
						find_order(message, orders).status_1 = 2
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.cacao\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Горячий шоколад.
	@bot.message_handler(func=lambda message: message.text.lower() == 'горячий шоколад')
	def hotcho(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nГорячий шоколад'
						find_order(message, orders).buf = 'горячий шоколад'
						bot.send_message(message.chat.id, 'Какого размера?', reply_markup = board.smlsize)
						find_order(message, orders).status_1 = 2
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.hotcho\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Флэт Уайт.
	@bot.message_handler(func=lambda message: message.text.lower() == 'флэт уайт')
	def flatwhite(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nФлэт Уайт'
						find_order(message, orders).buf = 'флэт уайт'
						find_order(message, orders).price += int(prices['flatwhite'])
						bot.send_message(message.chat.id, 'Желаете добавок?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.flatwhite\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Чай.
	@bot.message_handler(func=lambda message: message.text.lower() == 'чай')
	def tea(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).order += '\nЧай'
						find_order(message, orders).buf = 'чай'
						find_order(message, orders).price += int(prices['tea'])
						find_order(message, orders).status_1 = 3
						bot.send_message(message.chat.id, 'Желаете добавок?😊', reply_markup = board.dopmenu0)
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.tea\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			print(222)
	# Выбор размера.
	@bot.message_handler(func=lambda message: message.text.lower() == 'маленький')
	def switch_size_small(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 2:
						find_order(message, orders).order += ' ' + message.text
						if find_order(message, orders).buf == 'капучино':
							find_order(message, orders).price += int(prices['capuchino_s'])
						elif find_order(message, orders).buf == 'латте':
							find_order(message, orders).price += int(prices['latte_s'])
						elif find_order(message, orders).buf == 'раф':
							find_order(message, orders).price += int(prices['raf_s'])
						elif find_order(message, orders).buf == 'какао':
							find_order(message, orders).price += int(prices['cacao_s'])
						elif find_order(message, orders).buf == 'горячий шоколад':
							find_order(message, orders).price += int(prices['hotcho_s'])
						bot.send_message(message.chat.id, 'Желаете добавок?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.switch_size_small\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() == 'средний')
	def switch_size_medium(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 2:
						find_order(message, orders).order += ' ' + message.text
						if find_order(message, orders).buf == 'капучино':
							find_order(message, orders).price += int(prices['capuchino_m'])
						elif find_order(message, orders).buf == 'латте':
							find_order(message, orders).price += int(prices['latte_m'])
						elif find_order(message, orders).buf == 'раф':
							find_order(message, orders).price += int(prices['raf_m'])
						elif find_order(message, orders).buf == 'какао':
							find_order(message, orders).price += int(prices['cacao_m'])
						elif find_order(message, orders).buf == 'горячий шоколад':
							find_order(message, orders).price += int(prices['hotcho_m'])
						bot.send_message(message.chat.id, 'Желаете добавок?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.switch_size_medium\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() == 'большой')
	def switch_size_large(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 2:
						find_order(message, orders).order += ' ' + message.text
						if find_order(message, orders).buf == 'капучино':
							find_order(message, orders).price += int(prices['capuchino_l'])
						elif find_order(message, orders).buf == 'латте':
							find_order(message, orders).price += int(prices['latte_l'])
						elif find_order(message, orders).buf == 'раф':
							find_order(message, orders).price += int(prices['raf_l'])
						elif find_order(message, orders).buf == 'какао':
							find_order(message, orders).price += int(prices['cacao_l'])
						elif find_order(message, orders).buf == 'горячий шоколад':
							find_order(message, orders).price += int(prices['hotcho_l'])
						bot.send_message(message.chat.id, 'Желаете добавок?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.switch_size_large\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() == 'стандарт')
	def switch_size_standart(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 2:
						find_order(message, orders).order += ' ' + message.text
						if find_order(message, orders).buf == 'эспрессо':
							find_order(message, orders).price += int(prices['espresso'])
						elif find_order(message, orders).buf == 'американо':
							find_order(message, orders).price += int(prices['americano'])
						bot.send_message(message.chat.id, 'Желаете добавок?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.switch_size_standart\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() == 'доппио')
	def switch_size_dop(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 2:
						find_order(message, orders).order += ' ' + message.text
						if find_order(message, orders).buf == 'эспрессо':
							find_order(message, orders).price += int(prices['espresso_dop'])
						elif find_order(message, orders).buf == 'американо':
							find_order(message, orders).price += int(prices['americano_dop'])
						bot.send_message(message.chat.id, 'Желаете добавок?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.switch_size_dop\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Добавки
	@bot.message_handler(func=lambda message: message.text.lower() == 'сахар')
	def sugar_switch(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 3:
						find_order(message, orders).status_1 = 'sugar'
						bot.send_message(message.from_user.id, 'Сколько?', reply_markup=board.sugarqu)
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.sugar\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() == 'сахарозаменитель')
	def sugarzam_switch(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 3:
						find_order(message, orders).status_1 = 'sugarzam'
						bot.send_message(message.from_user.id, 'Сколько?', reply_markup=board.sugarqu)
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.sugarzam\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() == 'сироп')
	def syrup_switch(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 3:
						find_order(message, orders).status_1 = 'syrup'
						bot.send_message(message.from_user.id, 'Какой?')
						find_order(message, orders).price += 4
						find_order(message, orders).status_1 = 22
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.syrup_switch\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() == 'корица')
	def cinnamon(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 3:
						find_order(message, orders).order += ', Корица'
						bot.send_message(message.chat.id, 'Вы заказали:\n' + \
							find_order(message, orders).order + '\n\nК оплате: ' + \
							str(find_order(message,orders).price) + ' грн.')
						bot.send_message(message.chat.id, 'Что-то ещё?😊', reply_markup = board.dopmenu0)
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.cinnamon\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	@bot.message_handler(func=lambda message: message.text.lower() in ['без сахара', '1', '2', '3', '4'])
	def sugar_sugarzam(message):
		try:
			if db.ordrsqu(message) != None:
				try:
					if find_order(message, orders).status_1 == 'sugar':
						find_order(message, orders).order += ', Сахар: ' + message.text
						bot.send_message(message.chat.id, 'Вы заказали:\n' + \
							find_order(message, orders).order + '\n\nК оплате: ' + \
							str(find_order(message,orders).price) + ' грн.')
						bot.send_message(message.chat.id, 'Что-то ещё?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
					elif find_order(message, orders).status_1 == 'sugarzam':
						find_order(message, orders).order += ', Сахарозаменитель: ' + message.text
						bot.send_message(message.chat.id, 'Вы заказали:\n' + \
							find_order(message, orders).order + '\n\nК оплате: ' + \
							str(find_order(message,orders).price) + ' грн.')
						bot.send_message(message.chat.id, 'Что-то ещё?😊', reply_markup = board.dopmenu0)
						find_order(message, orders).status_1 = 3
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.sugar_sugarzam\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Кнопака 'Готово'
	@bot.message_handler(func=lambda message: message.text.lower() == 'готово')
	def done(message):
		try:
			if db.whatwrns(message) < warns_max:
				try:
					if find_order(message, orders).status_1 == 1:
						find_order(message, orders).status_2 = True
						bot.send_message(message.chat.id, 'Введите коментарий к заказу(и укажите, пожалйста, \
						время прибытия🥺)')
						find_order(message, orders).status_1 = 10
					elif find_order(message, orders).status_1 == 3:
						find_order(message, orders).status_1 = 1
						bot.send_message(message.from_user.id, 'Желаете ещё напиток?😊', \
							reply_markup=board.potablemenu1)				
				except:
					orders.remove(find_order(message, orders))
					bot.send_message(message.chat.id, 'Ошибка crtorder.done\nПопробуйте ещё раз')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
			else:
				bot.send_message(message.from_user.id, 'Ваш аккаунт заблокирован😡. Обратитесь к модератору.')
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Подтверждение правильности заказа
	@bot.message_handler(func=lambda message: message.text.lower() == 'всё верно')
	def vsyook(message):
		try:
			if db.whatwrns(message) < warns_max:
				if find_order(message, orders).status_1 == 10:
					if len(modersid_online) != 0:
						bot.send_message(message.chat.id, 'Заказ принят. Хорошего дня!😉👍')
						#=================
						for m_id in modersid_online:
							inline_1 = telebot.types.InlineKeyboardMarkup(row_width=1)
							button = telebot.types.InlineKeyboardButton(text='Принять', \
								callback_data=str(message.from_user.id))
							inline_1.add(button)
							bot.send_message(m_id, db.finduser(message)[1] + ' [o:' + str(db.finduser(message)[3]) \
								+ '/w:' + str(db.finduser(message)[4]) + '] создал заказ:\n' + \
									find_order(message, orders).order + '\n\nК оплате: ' +
								str(find_order(message, orders).price) + ' грн.', reply_markup = inline_1)
						#=================
						msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
							' [USER  ' + str(message.from_user.id) + ']' \
							' Создал заказ:\n' + \
							'================================================================================' + \
							find_order(message, orders).order + '\n\nК оплате: ' + \
							str(find_order(message, orders).price) + ' грн.\n' + \
							'================================================================================'
						log = open('logs/log_' + log_data + '.txt', 'a')
						log.write(msg + '\n')
						log.close()
						print(msg)
						orders_2.append(str(message.from_user.id))
						orders.remove(find_order(message, orders))
						global orderspersm
						orderspersm =+ 1
						db.ordrsqu(message, 1)
						db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
					else:
						bot.send_message(message.chat.id, 'В данный момент модераторов нет😴. Попробуйте позже')
						db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
			else:
				bot.send_message(message.from_user.id, 'Ваш аккаунт заблокирован😡. Обратитесь к модератору.')
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Загрузить из избранного
	@bot.message_handler(func=lambda message: message.text.lower() == 'избранный')
	def favorite(message):
		try:
			if db.ordrsqu(message) != None:
				if db.getfavorite(message) != False:
					find_order(message, orders).order = db.getfavorite(message)
					find_order(message, orders).price = db.getfavorite_price(message)
					bot.send_message(message.chat.id, 'Вы заказали:\n' + \
								find_order(message, orders).order + '\n\nК оплате: ' + \
								str(find_order(message,orders).price) + ' грн.')
					bot.send_message(message.chat.id, 'Что-то ещё?😊', reply_markup = board.potablemenu1)
					find_order(message, orders).status_1 = 1
				else:
					bot.send_message(message.chat.id, 'У вас ещё нет избранного😕')
					db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Сохранить в избранное
	@bot.message_handler(func=lambda message: message.text.lower() == 'сохранить в избранное')
	def infavorite(message):
		try:
			if db.whatwrns(message) < warns_max:
				if db.ordrsqu(message) != None:
					db.infavorite(message, find_order(message, orders).order)
					db.infavorite_price(message, find_order(message, orders).price)
					bot.send_message(message.chat.id, 'Сохранено👌', reply_markup = board.potablemenu1)
			else:
				bot.send_message(message.from_user.id, 'Ваш аккаунт заблокирован😡. Обратитесь к модератору.')
				db.whatarnk(message, bot, board.mainmenu0, board.mainmenu1, board.mainmenu2)
		except:
			pass
	# Полученме текстовых сообщений.
	@bot.message_handler(func=lambda message: True, content_types=['text'])
	def send_text(message):
		try:
			if db.ordrsqu(message) != None:
				global communication_id, communication_id_moder, unban
				if find_order(message, orders) == 'Not in list':
					# Добавление себя в админы через пароль
					if message.text == password:
						db.addme(message)
						db.admsim(adminsid)
						msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
							' [USER  ' + str(message.from_user.id) + '] Ввел админ пароль'
						log = open('logs/log_' + log_data + '.txt', 'a')
						log.write(msg + '\n')
						log.close()
						print(msg)
					# Обратная связь
					elif communication_id != None:
						if message.from_user.id == communication_id_moder:
							bot.send_message(communication_id, 'Сообщение от вашего модератора:\n' + message.text)
							msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
								' [MODER ' + str(communication_id_moder) + \
								'] Написал ' + str(communication_id) + ': ' + message.text
							log = open('logs/log_' + log_data + '.txt', 'a')
							log.write(msg + '\n')
							log.close()
							print(msg)
						elif str(message.from_user.id) == str(communication_id):
							bot.send_message(communication_id_moder, 'Сообщение от ' + communication_id + \
								':\n' + message.text)
							msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
								' [USER  ' + str(communication_id) + \
								'] Написал ' + str(communication_id_moder) + ': ' + message.text
							log = open('logs/log_' + log_data + '.txt', 'a')
							log.write(msg + '\n')
							log.close()
							print(msg)
					# Добавление нового админа/модера(только для админов)
					elif message.from_user.id in adminsid:
						global addadmin
						global addmoder
						global deladmin
						if addadmin == True:
							if db.admadd(message) == True:
								db.admsim(adminsid)
								msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
									' [ADMIN ' + str(message.from_user.id) + \
									'] Назначил ' + message.text + ' администратором'
								log = open('logs/log_' + log_data + '.txt', 'a')
								log.write(msg + '\n')
								log.close()
								print(msg)
								bot.send_message(message.chat.id, 'Администратор добавлен. ' + \
												'Ему нужно ввести /start для начала работы.')
							else:
								bot.send_message(message.chat.id, 'Ошибка. Пользователь должен зарегестрироваться')
							addadmin = False
						elif addmoder == True:
							if db.modadd(message) == True:
								db.mdrsim(modersid)
								msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
									' [ADMIN ' + str(message.from_user.id) + \
									'] Назначил ' + message.text + ' модератором'
								log = open('logs/log_' + log_data + '.txt', 'a')
								log.write(msg + '\n')
								log.close()
								print(msg)
								bot.send_message(message.chat.id, 'Модератор добавлен. ' + \
												'Ему нужно ввести /start для начала работы.')
							else:
								bot.send_message(message.chat.id, 'Ошибка. Пользователь должен зарегестрироваться')
							addmoder = False
						elif deladmin == True:
							if db.admormoddel(message, adminsid, modersid, modersid_online) == True:
								db.mdrsim(modersid)
								db.admsim(adminsid)
								msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
									' [ADMIN ' + str(message.from_user.id) + \
									'] Снял ' + message.text + ' с должности'
								log = open('logs/log_' + log_data + '.txt', 'a')
								log.write(msg + '\n')
								log.close()
								print(msg)
								bot.send_message(message.chat.id, 'Удалён')
							else:
								bot.send_message(message.chat.id, 'Ошибка. Пользователя не существует')
							deladmin = False
						elif unban == True:
							try:
								db.unban_bd(int(message.text))
								unban = False
								msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
										' [ADMIN ' + str(message.from_user.id) + \
										'] Разбанил ' + str(message.text)
								log = open('logs/log_' + log_data + '.txt', 'a')
								log.write(msg + '\n')
								log.close()
								print(msg)
								bot.send_message(message.from_user.id, message.text + ' разбанен')
								bot.send_message(int(message.text), 'Вас разбанили😌')
							except:
								bot.send_message(message.from_user.id, 'Ошибка')
				else:
					try:
						if find_order(message, orders).status_1 == 22:
							find_order(message, orders).order += ', Сироп: ' + message.text
							find_order(message, orders).status_1 = 3
							bot.send_message(message.chat.id, 'Вы заказали:\n' + \
							find_order(message, orders).order + '\n\nК оплате: ' + \
							str(find_order(message,orders).price) + ' грн.')
							bot.send_message(message.from_user.id, 'Что-то ещё?😊', reply_markup=board.dopmenu0)
						# Комментарий к заказу
						elif find_order(message, orders).status_2 == True:
							find_order(message, orders).order += '\n\nКомментарий:\n' + message.text
							bot.send_message(message.chat.id, 'Ваш заказ:\n' + \
								find_order(message, orders).order + '\n\nК оплате: ' + \
								str(find_order(message,orders).price) + ' грн.', reply_markup = board.allok)
							find_order(message, orders).status_2 = False
					except:
						pass
		except:
			pass
	# Callback
	@bot.callback_query_handler(func=lambda call: True)
	def callback_inline(call):
		if call.message.chat.id in modersid_online:
			for u in orders_2:
				if call.data == u:
					bot.send_message(u, 'Модератор ' + str(call.message.chat.id) + ' принял ваш заказ😉')
					inline_2 = telebot.types.InlineKeyboardMarkup(row_width=1)
					button3 = telebot.types.InlineKeyboardButton(text='Готово', \
						callback_data='done'+str(u))
					button1 = telebot.types.InlineKeyboardButton(text='Связь', \
						callback_data='communication'+str(u))
					button2 = telebot.types.InlineKeyboardButton(text='Удалить', \
						callback_data='delete' + str(u))
					inline_2.add(button3, button1, button2)
					bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, \
						reply_markup=inline_2)
					msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
						' [MODER ' + str(call.from_user.id) + \
						'] Принял заказ от ' + u
					log = open('logs/log_' + log_data + '.txt', 'a')
					log.write(msg + '\n')
					log.close()
					print(msg)
					break
				elif call.data == 'communication' + u:
					global communication_id, communication_id_moder
					communication_id = u
					communication_id_moder = call.message.chat.id
					bot.send_message(call.message.chat.id, 'Связь с ' + u + ' установлена',\
						reply_markup=board.end1)
					bot.send_message(u, '‼️‼️‼️Модератор ' + str(call.message.chat.id) + ' открыл чат с вами‼️‼️‼️\n' + \
						'Вы можете писать ему сообщения пока чат открыт(но стикеры он не получит, он наказан😝)')
					msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
						' [MODER ' + str(call.from_user.id) + \
						'] Связался с ' + u
					log = open('logs/log_' + log_data + '.txt', 'a')
					log.write(msg + '\n')
					log.close()
					print(msg)
					break
				elif call.data == 'done' + u:
					bot.send_message(u, 'Ваш заказ готов!😎☕️')
					msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
						' [MODER ' + str(call.from_user.id) + \
						'] Приготовил заказ для ' + u
					log = open('logs/log_' + log_data + '.txt', 'a')
					log.write(msg + '\n')
					log.close()
					print(msg)
					inline_3 = telebot.types.InlineKeyboardMarkup(row_width=1)
					button1 = telebot.types.InlineKeyboardButton(text='Связь', \
						callback_data='communication'+ str(u))
					button2 = telebot.types.InlineKeyboardButton(text='Удалить', \
						callback_data='delete' + str(u))
					button3 = telebot.types.InlineKeyboardButton(text='+Варн', \
						callback_data='warn' + str(u))
					inline_3.add(button3, button1, button2)
					bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, \
						reply_markup=inline_3)
					break
				elif call.data == 'delete' + u:
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, \
						text = str(u) + ' удалён')
					orders_2.remove(u)
					msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
						' [MODER ' + str(call.from_user.id) + \
						'] Удалил заказ от ' + u
					log = open('logs/log_' + log_data + '.txt', 'a')
					log.write(msg + '\n')
					log.close()
					print(msg)
					break
				elif call.data == 'warn' + u:
					db.pluswarn(u, 1)
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, \
						text = str(u) + ' не забрал заказ')
					bot.send_message(u, 'Вам выдан выговор😡')
					msg = str(datetime.datetime.today().strftime("|%H:%M:%S|%d/%m/%Y|")) + \
						' [MODER ' + str(call.from_user.id) + \
						'] Выдал варн ' + u
					log = open('logs/log_' + log_data + '.txt', 'a')
					log.write(msg + '\n')
					log.close()
					print(msg)
					break

bot.polling(none_stop=True)
