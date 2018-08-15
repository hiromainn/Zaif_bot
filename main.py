import requests
from zaifapi import *
from time import sleep

key = "-"
secret = "-"



try:
    zaif_public = ZaifPublicApi()
    last_price = int(zaif_public.last_price('btc_jpy')["last_price"])
except last_price.status_code != 200:
    print("価格取得に失敗、再取得")
    sleep(5)
    last_price



pair = "btc_jpy" #取引したいペア
amount = input("購入枚数入れてください")#購入枚数
limit_sell = input("リミット価格を入れてください(基本は1000円程度をお勧め)")



def line_notify(message):
  line_notify_token = '-'
  line_notify_url = 'https://notify-api.line.me/api/notify'
  message = message
  payload = {'message': message}
  headers = {'Authorization': 'Bearer ' + line_notify_token}
  line_notify = requests.post(line_notify_url, data=payload, headers=headers)

def zaif_buytraed():
    zaif = ZaifTradeApi(key, secret)
    zaif.trade(currency_pair=pair,
               action='ask',
               amount=float(amount),
               price=last_price,
               limit=int(limit_sell))
    if zaif.trade.status_code != 200:
        return zaif

zaif_buytraed()



line_notify(str(amount) + "でリミット価格" + str(limit_sell) + "の注文が入りました")









