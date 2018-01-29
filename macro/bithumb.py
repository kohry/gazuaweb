import requests 
import json
import pymysql

# MySQL Connection 연결
# conn = pymysql.connect(host='localhost', user='tester', password='', db='testdb', charset='utf8')

r = requests.get('https://api.bithumb.com/public/ticker/ALL')


['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP', 'BCH', 'XMR', 'ZEC', 'QTUM', 'BTG', 'EOS']

dict = json.loads(r.text)
print(dict['status'])
print(dict['data']['BTC']['average_price'])
