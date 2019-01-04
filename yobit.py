import requests



def get_btc():
	url 'https://yobit.net/api/2/btc_usd/ticker'
	response = requests.get(url).content.json()
	price = response['ticker']['last']
	return str(price) + '$'




get_btc()