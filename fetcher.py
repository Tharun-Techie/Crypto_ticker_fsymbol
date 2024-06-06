from binance.client import Client

api_key = "Enter your api key"
api_secret = "xxx"

client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()
count = 0
for s in exchange_info['symbols']:
    if s['symbol'].endswith('USDT'):
        print(s['symbol']+',\n')
        count += 1
print(count)