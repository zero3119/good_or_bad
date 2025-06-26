import requests

APIKEY = ""
title = input("What movie rating would you like to know? ")
url = "https://www.omdbapi.com"

params = {'apikey': APIKEY, 't': title}


response = requests.get(url , params=params)
data = response.json()
print(data["Title"], data["imdbRating"])