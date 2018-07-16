import urllib
import json
from utils import utils
from decimal import *

grlcpriceurl = 'https://graviex.net//api/v2/tickers/mmbbtc.json'
dashpriceurl = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

utils = utils()
cursor = utils.get_mysql_cursor()

sql = "TRUNCATE TABLE rates"
cursor.execute(sql)

response = urllib.urlopen(grlcpriceurl)
data = json.loads(response.read())
grlcprice = round(Decimal(data[0]['last']),8)

response = urllib.urlopen(dashpriceurl)
data = json.loads(response.read())
dashprice = round(Decimal(data[0]['price_usd']),8)

sql = "INSERT INTO rates (pair,rate) VALUES (%s, %s)"
pair = "MMB/BTC"
rate = grlcprice/dashprice
cursor.execute(sql, (pair,rate,))

pair = "BTC/MMB"
rate = dashprice/grlcprice
cursor.execute(sql, (pair,rate,))
