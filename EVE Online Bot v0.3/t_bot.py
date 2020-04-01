#Этот файл является исходником из другой программы, переделать абсолютно всё!
#токен 893292055:AAEZNOmWoOmLuO7ga_EB7riisjN_EoWOFuk

import telebot
from tools import *

bot = telebot.TeleBot('893292055:AAEZNOmWoOmLuO7ga_EB7riisjN_EoWOFuk')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'Alt+Tab')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет, хозяин')
	elif message.text.lower() == 'пока':
		bot.send_message(message.chat.id, 'Пока, хозяин')
	elif message.text.lower() == 'alt+tab':
		atab()

bot.polling()

