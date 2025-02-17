import time

import matplotlib.pyplot as plt
import pandas as pd
import requests

coins = ["bitcoin", "ethereum", "binancecoin", "ripple", "solana"]

base_url = "https://api.coingecko.com/api/v3/coins/"

crypto_data = []

for coin in coins:
    url = f"{base_url}{coin}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        price = data["market_data"]["current_price"]["usd"]
        market_cap = data["market_data"]["market_cap"]["usd"]
        volume = data["market_data"]["total_volume"]["usd"]

        crypto_data.append([name, price, market_cap, volume])
    else:
        print(f"Error fetching data for {coin}")

    # found a waiting library because I realised it takes about half a second for some of the prices to be fetched sometimes
    # set to 1 second
    time.sleep(1)

print("this is the data", crypto_data)

df = pd.DataFrame(
    crypto_data, columns=["Name", "Price (USD)", "Market Cap", "24h Volume"]
)

print(df)

df.to_csv("coins_currency_data.csv", encoding="utf-8")
