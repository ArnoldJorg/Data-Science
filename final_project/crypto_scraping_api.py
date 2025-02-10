import pandas as pd
import requests

# Set the base URL for the CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/bitcoin"

# Send a GET request to fetch the data
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Extract relevant details
    name = data["name"]
    symbol = data["symbol"]
    current_price = data["market_data"]["current_price"]["usd"]
    market_cap = data["market_data"]["market_cap"]["usd"]
    total_supply = data["market_data"]["total_supply"]
    circulating_supply = data["market_data"]["circulating_supply"]

    # Print the data in a clean format
    print(f"Cryptocurrency: {name} ({symbol.upper()})")
    print(f"Current Price (USD): ${current_price}")
    print(f"Market Cap (USD): ${market_cap}")
    print(f"Total Supply: {total_supply}")
    print(f"Circulating Supply: {circulating_supply}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# print 4 more coins and then push them onto my csv
