import asyncio
import requests 
from bs4 import BeautifulSoup

PREFIX = 'localhost'
# PREFIX = 'gazuagazua.com'

def getJSON_chainz(symbol, q) :
    r = requests.get(f'http://chainz.cryptoid.info/{symbol}/api.dws?q={q}')
    return r.content

# 다음을 이용하는 메서드
def getExchangeRate(country) : 
    r = requests.get(f'http://finance.daum.net/exchange/exchangeDetail.daum?code={country}')
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="hyenCost").get_text()
    
def insertChaninz(symbol, f) :
    content = getJSON_chainz(symbol, f)
    r = requests.post( f'http://{PREFIX}/insert.php', data = {'table' : f"table_{f}" ,'symbol':symbol, 'jsondata':content} )
    print(f"insert chainz [table_{f},{symbol}] response : {r.text}")

def updateExchangeRate() :
    usd = getExchangeRate("USD")
    jpy = getExchangeRate("JPY")
    hkd = getExchangeRate("HKD")
    eur = getExchangeRate("EUR")
    r = requests.post( f'http://{PREFIX}/update_exchange.php', data = {'table' : f"table_exchange", 'usd':usd, 'jpy':jpy, 'hkd':hkd, 'eur':eur } )
    print(f"insert chainz [table_exchange] response : {r.text}")

def callFunctions() :
    insertChaninz("btc",  "rich")
    updateExchangeRate()

callFunctions()


#init
# print(getJSON_chainz("btc", "rich"))
# print(getJSON_chainz("grs", "rich"))
# print(exchangeRate("JPY"))






# addresses: returns a JSON object with the number of known and non-zero addresses (with funds)
# circulating: returns the number of circulating coins (minus reserve, Prime holdings...)
# getblockcount: returns the current block height as a plain text string
# getdifficulty: returns the difficulty as a plain text string
# hashrate: returns the hashrate in GH/s (when supported, blockchain.info API compatible)
# nethashps: returns the hashrate in H/s (when supported)
# netmhashps: returns the hashrate in MH/s (when supported)
# rich: returns the rich list top 1000 (JSON format)
# summary: returns summary information for all explorers
# ticker.btc: returns the last market ticker in BTC, as tracked by the explorer, only one market is tracked and this value can be several minutes behind the market. Use market APIs directly for more accurate quotations.
# ticker.usd: returns the last market ticker in USD, as tracked by the explorer and BitPay rate, only one market is tracked and this value can be several minutes behind the market. Use market APIs directly for more accurate quotations.
# totalbc: returns the outstanding number of coins in satoshis (x 1e8, for compatibility with blockhain.info API)
# totalcoins: returns the outstanding number of coins
# addressfirstseen: returns the date and time of the block in which the address was first seen, or a string begining with "ERROR:" otherwise.
# getbalance: returns the balance of the address. For incorrect addresses or addresses never seen on the network, the returned balance is zero. Can be delayed by up to 6 hours unless you specify an API Key.
# getreceivedbyaddress: returns the amount received by the address (sum of vout). For incorrect addresses or addresses never seen on the network, the returned amount is zero. Can be delayed by up to 1 hour.
# richrank: returns the rich list rank for the address.
# getblockhash: takes a height parameter and returns corresponding block hash.
# getblockheight: takes a hash parameter and returns corresponding block height.
# Pass the transaction hash in the t parameter.

# lasttxs: returns the last ten transactions (with at least one confirmation), excluding coinbase and stake transactions
# txinfo: returns summary information about a transaction (confirmations, fees, inputs & output addresses and amounts).