import matplotlib.pyplot as plt
import pandas as pd
import requests

url = "https://api.coingecko.com/api/v3/coins/solana/market_chart/range?vs_currency=usd&from=1735689601&to=1738368001&precision=1"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

prices_list = data["prices"]

df = pd.DataFrame(prices_list, columns=["date", "price in USD"])


df["date"] = pd.to_datetime(df["date"], unit="ms")

print(df.head())

df.to_csv("solana_jan_to_feb.csv", encoding="utf-8")
print(df.describe())


plt.plot(df["date"], df["price in USD"], label="Solana", color="blue")


plt.title("Solana Prices Jan to Feb")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()

plt.show()
