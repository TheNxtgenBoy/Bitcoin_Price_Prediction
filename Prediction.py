import requests, time
from time import strftime as stf
from time import gmtime as gmt

def get_5_day():
	url = 'https://coincodex.com/api/predictions/get_byshortname/bitcoin'
	r = list(requests.get(url).json()['predictionChart']['30D_5D'])
	[print(f'{stf("%D(%H:%M)", gmt(i[0]))} : {int(i[1])}, {int(i[3])}, {int(i[4])}') for i in r]

def get_7_day():
	url = 'https://coincodex.com/api/predictions/get_byshortname/bitcoin'
	r = list(requests.get(url).json()['predictionChart']['30D'])
	[print(f'{stf("%D(%H:%M)", gmt(i[0]))} : {int(i[1])}, {int(i[3])}, {int(i[4])}') for i in r]

get_5_day()
get_7_day()
