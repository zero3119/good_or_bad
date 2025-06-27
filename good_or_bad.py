import json
import requests
import pandas as pd
import sqlalchemy as db

APIKEY = ""
title = input("What movie rating would you like to know? ")
url = "https://www.omdbapi.com"

params = {'apikey': APIKEY, 't': title}

response = requests.get(url , params=params)
data = response.json()

data.pop("Ratings", None)

df = pd.DataFrame([data])

engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))

# print(data["Title"], data["imdbRating"])