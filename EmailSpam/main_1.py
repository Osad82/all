#работает
import smtplib
my_email = input('From(gmail): ')
my_password = input('Password: ')
to_email = input('Send to: ')
to_subject = input('Subject: ')
to_text = input('Text: ')
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(my_email, my_password)
smtpObj.sendmail(my_email, to_email, 'Subject: ' + to_subject + '\n' + to_text)
smtpObj.quit()
print('Complete')