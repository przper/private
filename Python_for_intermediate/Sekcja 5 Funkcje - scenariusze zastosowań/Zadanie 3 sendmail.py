"""
LAB - Wysylanie maili z Pythona

Podążając za instrukcjami z tej lekcji wyślij sobie maila z Pythona.
Jeśli nie masz konta na GMAIL, może się okazać, że będzie trzeba używać
lekko zmodyfikowanych parametrów funkcji. Rozważ w takim przypadku,
czy nie lepiej założyć sobie dodatkowe "robocze" konto GMAIL.
"""

import smtplib

mailFrom = 'Your automation process'
mailTo = ['avan.radien@gmail.com','przemyslaw.perzyna@gmail.com']
mailSubject = 'Automation process'
mailBody = '''Hello

This message was created automatically. Please do not respond.

Have a good day!'''
message="""From {}
Subject: {}

{}
""".format(mailFrom,mailSubject,mailBody)

user = 'avan.radien@gmail.com'
password = 'eNdd^4%q'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mailTo,message)
    server.close()
    print("mail sent succesfully")
except:
    print("error during sending mail")