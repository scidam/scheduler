#coding: utf-8
from __future__ import print_function

import sys, os, re
from datetime import date, time

sys.path.append('/home/scidam/webapps/bgicms242/bgi')
os.environ['DJANGO_SETTINGS_MODULE']='bgi.settings'

from bgi.scheduler.fixtures.datareg import data
from bgi.scheduler.models import ScheduleName, ScheduleDates, ScheduleTimes
from django.contrib.auth import get_user_model
import random
from string import letters
import time as time_module

import smtplib

from email.mime.text import MIMEText
from email.utils import formatdate


CDIR = os.path.dirname(os.path.abspath(__file__))


usermodel = get_user_model()


letter_template = """
Здравствуйте, {}!

Для вас была создана регистрационная форма
в рамках проекта "Сам по следам".

Данные для авторизации:
=======================

Путь для авторизации: http://botsad.ru/admin-reg/
Имя пользователя: {}
Пароль: {}

Вы можете сменить пароль после авторизации.

Перечень зарегистрированных участников
доступен по ссылке (необходима авторизация): http://botsad.ru/admin-reg/

Регистрационная форма также доступна на сайте БСИ ДВО РАН по ссылке: http://botsad.ru/reg/{}

Код для интеграции формы на Ваш сайт:

<!-- Начало кода {} -->
<iframe src="http://botsad.ru/reg/{}" width="600" height="300" align="center">Ваш браузер не поддерживает плавающие фреймы!</iframe>
<!-- Конец кода {} -->


Это письмо сегенрировано автоматически. Отвечать на него не нужно.

"""

theme_template = "Регистрационная форма (Сам по следам). Данные для входа в панель администрирования."

# -------- email authentification data
MAIL_PASS = ''
MAIL_LOGIN = 'no-reply@botsad.ru'  # These data will be erased


# -------- utility function
timepat = re.compile('\d\d:\d\d')


def parse_times(s):
    pats = timepat.findall(s)
    times = [(int(item.split(':')[0]), int(item.split(':')[1])) for item in pats]
    result = [time(hour=t[0], minute=t[1]) for t in times]
    return result


# --------------- Loading & processing the data ---------

for item in data:
    # -------------- evaluating data item, sending mail after completion....
    if item['dateonly']:
        maxnum = 2000
    else:
        maxnum = 5

    um, _ = usermodel.objects.get_or_create(username=item['username'], is_staff=True)

    if 'objpk' in item:
        schm = ScheduleName.objects.get(pk=int(item['objpk']))
    else:
        schm, _ = ScheduleName.objects.get_or_create(name=item['name'], user=um, maxnumber=maxnum)

    for d in item['dates']:
        mo = int(d['month'])
        for day in d['days']:
            schd,_ = ScheduleDates.objects.get_or_create(name=schm, user=um, date=date(year=2019, month=mo, day=int(day)), dateonly=item['dateonly'])
            if item['dateonly']:
                ScheduleTimes.objects.get_or_create(date=schd, user=um, time=time(hour=11, minute=0, second=0))
            else:
                for t in parse_times(item['times']):
                    ScheduleTimes.objects.get_or_create(date=schd, user=um, time=t)

    # -------------------------------------------------------
    # sending email
    passw = ''.join([random.choice(letters) for k in range(5)])
    um.set_password(passw)
    um.email = item['email']
    um.save()
    letter = letter_template.format(item['name'], item['username'],
                                    passw, item['slug'], item['name'],
                                    item['slug'], item['name'])

    smtp = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    smtp.login(MAIL_LOGIN, MAIL_PASS)
    msg = MIMEText(letter, "plain", "utf-8")
    msg['Date'] = formatdate(localtime=True)
    msg["Subject"] = theme_template.format(item['name'])
    msg["To"] = 'kislov@botsad.ru'  # TODO : item['email'] instead
    msg["From"] = MAIL_LOGIN
    print('=' * 30)
    print("Sending the message")
    print(msg.as_string())
   # smtp.sendmail('biomorphology@botsad.ru', [tomail], msg.as_string())
    smtp.quit()
    time_module.sleep(random.randint(10, 30))
