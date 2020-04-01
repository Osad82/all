# -*- coding: cp1251 -*-
#by de_jure
#toolbox.py for main.py
#14.01.20(вечер) - 05.02.20

import sqlite3
import telebot


class order:
	login = None
	chat_id = None
	order = ''
	status_1 = None
	status_2 = False
	price = 0
	buf = None
	def Constructor(self, _login, _chat_id):
		self.login = _login
		self.chat_id = _chat_id

def find_order(message, orders):
	try:
		for i in orders:
			if i.chat_id == message.from_user.id:
				return i
				break
		else:
			x = 'Not in list'
			return x		
	except:
		x = 'Not in list'
		return x

'''Клавиатуры.
send_phone -- отправка боту номера телефона пользователя.

mainmenu0 -- главное меню простого пользователя(if admin_rank == 0). 

mainmenu1 -- главное меню модератора(if admin_rank == 1).

mainmenu2 -- главное меню администратора(if admin_rank == 2).

modermenu -- панель модератора.

adminmenu -- панель администратора.

potablemenu0 -- выбор напитка.

espressosize -- размеры для эспрессо.

sugarqu -- выбор сахара.

potablemenu1 -- меню напитков после первого заказа.

allok -- клавиатура подтверждения

'''
class board:
	# Меню добавок
	dopmenu0 = telebot.types.ReplyKeyboardMarkup(True, True, row_width=2)
	dopmenu0.row('Готово', 'Отмена')
	dopmenu0.add('Сахар', 'Сироп')
	dopmenu0.add('Сахарозаменитель', 'Корица')
	#
	end1 = telebot.types.ReplyKeyboardMarkup(True, row_width=1)
	end1.row('Разорвать связь')
	# Отправка номера телефона.
	send_phone = telebot.types.ReplyKeyboardMarkup(True, True)
	button_phone = telebot.types.KeyboardButton(text='Отправить номер телефона', request_contact=True)
	send_phone.add(button_phone)
	# Главное меню простого пользователя(if admin_rank == 0).
	mainmenu0 = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
	mainmenu0.add('Меню', 'Создать заказ')
	mainmenu0.row('Моя статистика')
	# Главное меню модератора(if admin_rank == 1).
	mainmenu1 = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
	mainmenu1.add('Меню', 'Создать заказ')
	mainmenu1.row('Моя статистика')
	mainmenu1.row('Модер. меню')
	# Главное меню администратора(if admin_rank == 2).
	mainmenu2 = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
	mainmenu2.add('Меню', 'Создать заказ')
	mainmenu2.row('Моя статистика')
	mainmenu2.row('Админ. меню')
	# Модерпанель
	modermenu = telebot.types.ReplyKeyboardMarkup(True)
	modermenu.row('Принять смену', 'Сдать смену', 'Отмена')
	# Админпанель
	adminmenu = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
	adminmenu.row('Кол-во пользователей')
	adminmenu.row('Модераторы Online')
	adminmenu.add('Список администраторов', 'Список модераторов') 
	adminmenu.add('Добавить администратора', 'Добавить модератора') 
	adminmenu.add('Удалить администратора', 'Удалить модератора')
	adminmenu.row('Разбан')
	adminmenu.row('Отмена')
	# Меню напитков
	potablemenu0 = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
	potablemenu0.row('Избранный')
	potablemenu0.add('Эспрессо', 'Американо')
	potablemenu0.add('Капучино', 'Латте')
	potablemenu0.add('Какао', 'Горячий Шоколад')
	potablemenu0.add('Чай', 'Флэт Уайт')
	potablemenu0.row('Отмена')
	# Эспрессо размер
	espressosize = telebot.types.ReplyKeyboardMarkup(True)
	espressosize.row('Стандарт', 'Доппио')
	# Американо размер
	americanosize = telebot.types.ReplyKeyboardMarkup(True)
	americanosize.row('Стандарт', 'Доппио')
	# SML размеры
	smlsize = telebot.types.ReplyKeyboardMarkup(True)
	smlsize.row('Маленький', 'Средний', 'Большой')
	# Кол-во сахара
	sugarqu = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
	sugarqu.row('Без сахара')
	sugarqu.add('1', '2', '3', '4')
	sugarqu.row('Отмена')
	# Меню напитков, после первого заказа
	potablemenu1 = telebot.types.ReplyKeyboardMarkup(True, True, row_width=2)
	potablemenu1.add('Готово', 'Отмена')
	potablemenu1.row('Сохранить в избранное')
	potablemenu1.add('Эспрессо', 'Американо')
	potablemenu1.add('Капучино', 'Латте')
	potablemenu1.add('Какао', 'Горячий Шоколад')
	potablemenu1.add('Чай', 'Флэт Уайт')
	# Подтверждение
	allok = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
	allok.add('Всё верно', 'Отмена')


'''Работа с базой данных.
Для работы с базой данных бот использует библиотеку sqlite3.

createdb -- создание БД, если она не существует.
База данных имеет столбцы:
id(primary key) = уникальный id пользователя,
login(text) = номер телефона/никнейм пользователя,
user_id(integer) = Telegram ID пользователя,
orders(integer) = количество заказов пользователя,
warns(integer) = количество варнов(выговоров) пользователя,
rank(integer) = ранг пользователя(для крутых плюшек, но пока пусто),
admin_rank(integer) = привилегии пользователя(0 - стандарт, 1 - модератор, 2 - администратор),
who_add(text) = login того, кто последний выдал пользователю привилегию,
favorite(text) = избранный заказ пользователя.

createuser -- создание пользователя в БД.  Принимает значение message.

finduser -- поиск пользователя в БД.  Выводит всю строку пользователя из БД.  Если пользователь не найден -
возвращает None.

whatarnk -- возвращает админ ранг(admin_rank) пользователя и/или переход на соотвецтвенное меню(опционально).
Если нужно просто узнать ранг - указать только message, если нужно перейти в определённое меню - ввести все
параметры(message, bot, userkeyboard, moderkeyboard, adminkeyboard).

whatwrns -- возвращает выговоры(warns) пользователя.

ordrsqu -- возвращает количество заказов(orders) пользователя.  Если ввести n во вторым параметром - кол-во заказов
пользователя увеличится на n.

mdrsim -- находит в БД всех модераторов и возвращает их в список modersid.

admsim -- находит в БД всех администраторов и возвращает их в список adminsid.

modadd -- добавляет модератора по номеру телефона(login).

admadd -- добавляет администратора по номеру телефона(login).

kolvo -- возвращает количевство пользователей БД.

addme -- добавляет в админы человека, который ввел админ-пароль.

admormoddel -- удаляет администратора/модератора путём установки ему админ ранга на 0.

showall -- выводит список пользователей(в данной программе администраторов и модераторов).

'''
class db:
	# Создание базы данных, если она не существует.
	def createdb():
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, login TEXT, user_id INTEGER, orders INTEGER, warns INTEGER, rank INTEGER, admin_rank INTEGER, who_add TEXT, favorite TEXT, favorite_price INTEGER)')
		con.commit()
		cur.close()
		con.close()
	# Создание пользователя в БД.
	def createuser(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		data = [str(message.contact.phone_number), message.from_user.id, 0, 0, 0, 0, '-', '-', 0]
		con.execute('INSERT INTO users(login, user_id, orders, warns, rank, admin_rank, who_add, favorite, favorite_price) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
		print('Новый пользователь! ' + str(message.contact.phone_number))
		con.commit()
		cur.close()
		con.close()
	# Поиск пользователя по user_id в базе данных.  Возвращает список.  Если пользователь не найден -
	# возвращает значение None.
	def finduser(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT * FROM users WHERE user_id=?', [(message.from_user.id)])
		result = cur.fetchone()
		try:
			return list(result)
		except:
			return None
		cur.close()
		con.close()
	# Возвращает админ ранг(admin_rank) пользователя и/или переход на соотвецтвенное меню(опционально).
	def whatarnk(message, bot=None, user=None, moder=None, admin=None):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT admin_rank FROM users WHERE user_id=?', [(message.from_user.id)])
		res = cur.fetchone()
		result = res[0]
		if bot != None:
			if result == 0:
				bot.send_message(message.from_user.id, 'Главное меню:', reply_markup=user)
			elif result == 1:
				bot.send_message(message.from_user.id, 'Главное меню:', reply_markup=moder)
			elif result == 2:
				bot.send_message(message.from_user.id, 'Главное меню:', reply_markup=admin)
		else:
			return result
		cur.close()
		con.close()
	# Возвращает выговоры(warns) пользователя.
	def whatwrns(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT warns FROM users WHERE user_id=?', [(message.from_user.id)])
		res = cur.fetchone()
		result = res[0]
		cur.close()
		con.close()
		return result
	# Увеличить варн пользователя who на on
	def pluswarn(who, on):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT warns FROM users WHERE user_id=?', [(who)])
		res = cur.fetchone()
		result = res[0]
		data = [result + on, who]
		cur.execute('UPDATE users SET warns=? WHERE user_id=?', data)
		con.commit()
		cur.close()
		con.close()
	# Разбан
	def unban_bd(who):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		data = [0, who]
		cur.execute('UPDATE users SET warns=? WHERE user_id=?', data)
		con.commit()
		cur.close()
		con.close()
	# Возвращает количество заказов(orders) пользователя
	def ordrsqu(message, _set=0):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT orders FROM users WHERE user_id=?', [(message.from_user.id)])
		res = cur.fetchone()
		result = res[0]
		result += _set
		data = [result, message.from_user.id]
		cur.execute('UPDATE users SET orders=? WHERE user_id=?', data)
		con.commit()
		cur.close()
		con.close()
		return result
	# Импорт модераторов из БД в modersid
	def mdrsim(modersid):
			con = sqlite3.connect('Database.db')
			cur = con.cursor()
			cur.execute('SELECT user_id FROM users WHERE admin_rank=1')
			rows = cur.fetchall()
			modersid.clear()
			for row in rows:
				modersid.append(row[0])
			cur.close()
			con.close()
			return modersid
	# Импорт администраторов из БД в adminsid
	def admsim(adminsid):
			con = sqlite3.connect('Database.db')
			cur = con.cursor()
			cur.execute('SELECT user_id FROM users WHERE admin_rank=2')
			rows = cur.fetchall()
			adminsid.clear()
			for row in rows:
				adminsid.append(row[0])
			cur.close()
			con.close()
			return adminsid
	# Добавляет модера по номеру
	def modadd(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT * FROM users WHERE login=?', [(message.text)])
		result = cur.fetchone()
		if result != None:
			data = [1, result[1]]
			cur.execute('UPDATE users SET admin_rank=? WHERE login=?', data)
			data = [message.from_user.id, result[1]]
			cur.execute('UPDATE users SET who_add=? WHERE login=?', data)
			con.commit()
			return True
		else:
			return False
		cur.close()
		con.close()
	# Добавляет админа по номеру
	def admadd(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT * FROM users WHERE login=?', [(message.text)])
		result = cur.fetchone()
		if result != None:
			data = [2, result[1]]
			cur.execute('UPDATE users SET admin_rank=? WHERE login=?', data)
			data = [message.from_user.id, result[1]]
			cur.execute('UPDATE users SET who_add=? WHERE login=?', data)
			con.commit()
			return True
		else:
			return False
		cur.close()
		con.close()
	# Возвращает кол-во user-ов
	def kolvo():
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT * FROM users')
		rows = cur.fetchall()
		cur.close()
		con.close()
		return len(rows)
	# Добавляет в администраторы того, кто введет админ пароль
	def addme(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		data = [2, message.from_user.id]
		cur.execute('UPDATE users SET admin_rank=? WHERE user_id=?', data)
		data = ['myself', message.from_user.id]
		cur.execute('UPDATE users SET who_add=? WHERE user_id=?', data)
		con.commit()
		cur.close()
		con.close()
	# Удаляет администратора/модератора
	def admormoddel(message, admin, mod, mod_online):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT * FROM users WHERE login=?', [(message.text)])
		result = cur.fetchone()
		if result != None:
			data = [0, result[1]]
			cur.execute('UPDATE users SET admin_rank=? WHERE login=?', data)
			con.commit()
			try:
				admin.remove(result[2])
			except:
				pass
			try:
				mod.remove(result[2])
			except:
				pass
			try:
				mod_online.remove(result[2])
			except:
				pass
			return True
		else:
			return False
		cur.close()
		con.close()
	# Выводит список администраторов/модераторов
	def showall(message, bot, _rank):
		bot.send_message(message.chat.id, 'LOGIN/USER_ID/WHO_ADD')
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT * FROM users WHERE admin_rank=?', [(_rank)])
		rows = cur.fetchall()
		for row in rows:
			bot.send_message(message.chat.id, str(row[1]) + '/' + str(row[2]) + '/' + row[7])
		cur.close()
		con.close()
	# Возвращает избранное пользователя. Если его нет - возвращает False
	def getfavorite(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT favorite FROM users WHERE user_id=?', [(message.from_user.id)])
		row = cur.fetchone()
		if row[0] != '-':
			return row[0]
		else:
			return False
		cur.close()
		con.close()
	# Запись текущего заказа в избранный
	def infavorite(message, fav):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		data = [fav, message.chat.id]
		cur.execute('UPDATE users SET favorite=? WHERE user_id=?', data)
		con.commit()
		cur.close()
		con.close()
	# Получить цену избранного заказа
	def getfavorite_price(message):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		cur.execute('SELECT favorite_price FROM users WHERE user_id=?', [(message.from_user.id)])
		row = cur.fetchone()
		if row[0] != '0':
			return row[0]
		else:
			return False
		cur.close()
		con.close()
	# Запись цены текущего заказа в цену избранного
	def infavorite_price(message, price):
		con = sqlite3.connect('Database.db')
		cur = con.cursor()
		data = [price, message.chat.id]
		cur.execute('UPDATE users SET favorite_price=? WHERE user_id=?', data)
		con.commit()
		cur.close()
		con.close()
