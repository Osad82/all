import telebot

# Подключение к токену
bot = telebot.TeleBot('959646861:AAHa92DPC1ln3Y4t4rH8QWKYg_g0F2RmAMI')

# Создание inline-клавиатуры
inline_1 = telebot.types.InlineKeyboardMarkup(row_width=1)
button_1 = telebot.types.InlineKeyboardButton(text='Привет', callback_data='hello')
inline_1.add(button_1)

# Реакция бота на команду /start
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Дарова', reply_markup=inline_1)

# 'Отсеивание' ненужных форматов
@bot.message_handler(content_types=['sticker', 'voice', 'audio', 'document',
								'photo', 'video', 'video_note', 'location'])
def goaway(message):
	pass

# Реакция бота на inline-сообщения
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.data == 'hello':
		bot.send_message(call.message.chat.id, 'Куку')
		bot.edit_message_reply_markup(chat_id=call.message.chat.id, 
									message_id=call.message.message_id)
			
bot.polling(none_stop=True)




