#не работает
import smtplib
from time import sleep
#Блок записи отправного мыла
my_emails = []
indx = 0
while True:
		my_emails.append(str(input('[' + str(indx) + ']From(gmail): ')))
		my_emails.append(str(input('[' + str(indx) + ']Password: ')))

		menu = input('A lot?(+/-): ')
		if menu == '-':
			break
		indx =+ 1
print(my_emails)

#Блок записи мыла получателей
to_emails = []
indx = 0
while True:
	to_emails.append(str(input('[' + str(indx) + ']To (mail): ')))

	menu = input('A lot?(+/-): ')
	if menu == '-':
		break
	indx =+ 1
print(to_emails)

to_subject = input('Subject: ')
to_text = input('Text: ')

'''
#проблемно
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(my_emails[i], my_emails[i+1])
smtpObj.sendmail(my_emails[i], to_emails[0], 'Subject: ' + to_subject + '\n' + to_text)
smtpObj.quit()
'''



#print('Complete')

#factorio.fun@gmail.com
#asger000black@gmail.com
#qrupqrup
#george000black@gmail.com
#george18032001
#lemonoed23@gmail.com
#Gg_18032001