#работает
import smtplib
from time import sleep
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar
import threading

Window.size = (800, 600)
#=========================================
class Container(GridLayout):
	progress = ObjectProperty()
	progress_value = ObjectProperty()
	#Взять отправочное мыло из файла
	def open_my(self):
		my_emails = open('my.txt').read().splitlines()
		return my_emails
	#Пароли к отправочному мылу
	def open_my_p(self):
		my_emails_p = open('my_p.txt').read().splitlines()
		print(my_emails_p)
		return my_emails_p
	#Взять мыло получателей
	def open_to(self):
		to_emails = open('to.txt').read().splitlines()
		print(to_emails)
		return to_emails
	#Начать спам
	def start(self):
		my_emails = self.open_my()
		my_emails_p = self.open_my_p()
		to_emails = self.open_to()

		self.progress.text = '0/' + str(len(my_emails))
		self.progress_value = 0

		to_subject = input('Subject: ')
		to_text = input('Text: ')

		for i in range(0, len(my_emails)):
			
			smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
			smtpObj.ehlo()
			smtpObj.starttls()
			try:
				smtpObj.login(my_emails[i], my_emails_p[i])
				smtpObj.sendmail(my_emails[i], to_emails[0], 'Subject: ' + to_subject + '\n' + to_text)
				print(my_emails[i] + ' done')
			except:
				continue
			smtpObj.quit()
			self.progress.text = str(i+1) + '/' + str(len(my_emails))
			#беда с прогрессбаром
			#x = (i+1) / len(my_emails)
			#self.progress_value.value = int(x)
		self.progress.text = 'Done! ' + str(i+1) + '/' + str(len(my_emails))
	#Открыть поток для начала спама
	def thr(self):
		t = threading.Thread(target = self.start, daemon = True)
		t.start()
	#Выйти из программы !!!Переделать в стоп спам!!!
	def stop(self):
		exit()
		#
	#

#=========================================
class MyApp(App):
	def build(self):
		return Container()
#=========================================
if __name__ == "__main__":
	MyApp().run()
#=========================================

