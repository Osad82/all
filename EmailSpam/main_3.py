#работает
import smtplib
from time import sleep

#Взять отправочное мыло из файла
def open_my():
	my_emails = open('my.txt').read().splitlines()
	print(my_emails)
	return my_emails
#Пароли к отправочному мылу
def open_my_p():
	my_emails_p = open('my_p.txt').read().splitlines()
	print(my_emails_p)
	return my_emails_p
#Взять мыло получателей
def open_to():
	to_emails = open('to.txt').read().splitlines()
	print(to_emails)
	return to_emails

my_emails = open_my()
my_emails_p = open_my_p()
to_emails = open_to()

to_subject = input('Subject: ')
to_text = input('Text: ')


for i in range(0, len(my_emails)):
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	try:
		smtpObj.login(my_emails[i], my_emails_p[i])
	except:
		continue
	smtpObj.sendmail(my_emails[i], to_emails[0], 'Subject: ' + to_subject + '\n' + to_text)
	smtpObj.quit()
	print(my_emails[i] + ' done')




#print('Complete')

#factorio.fun@gmail.com
#asger000black@gmail.com
#qrupqrup
#george000black@gmail.com
#george18032001
#lemonoed23@gmail.com
#Gg_18032001