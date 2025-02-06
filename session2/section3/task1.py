import pandas as pd
import requests
from bs4 import BeautifulSoup

# Wikipedia URL for Bitcoin
wikiurl = "https://en.wikipedia.org/wiki/Bitcoin"

# Get the response and parse the HTML
response = requests.get(wikiurl)
print(response.status_code)  # Check if request was successful

bs_html = BeautifulSoup(response.text, "html.parser")

# Find the infobox table
tabledata = bs_html.find("table", {"class": "infobox"})

# Extract key-value pairs manually
data = []
for row in tabledata.find_all("tr"):
    cells = row.find_all(["th", "td"])
    if len(cells) == 2:  # Ensure it's a key-value row
        key = cells[0].get_text(strip=True)
        value = cells[1].get_text(strip=True)
        data.append((key, value))

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Attribute", "Value"])

# Save to CSV
df.to_csv("bitcoin_info_cleaned.csv", index=False, sep="\t", encoding="utf-8")

# Print the cleaned data
print(df.head())
