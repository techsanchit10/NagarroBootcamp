# 3. Go through the available public apis listed here: https://github.com/toddmotto/public-apis. Select any 2 of your favorite APIs and write a python script to:

# 	- collect data from those APIs
# 	- save the data in a file (json/txt file)


import requests
import json

urlAPI_weather = "https://api.darksky.net/forecast/2f2f55c8ef03397c1715468a4ee7b1cd/37.8267,-122.4233"
urlAPI_currency = "https://api.exchangeratesapi.io/latest"

req_weather = requests.get(urlAPI_weather, verify=False)

with open("weather_content.json", 'w') as f:
	k = json.loads(req_weather.text)
	# print(k['timezone'])
	f.write(json.dumps(k,indent =2))
	print("Weather File updated!")

	

req_currency = requests.get(urlAPI_currency, verify = False)

with open("currency_content.json",'w') as f:
	l = json.loads(req_currency.text)
	f.write(json.dumps(l,indent =2))
	print("Currency File updated!")
