import random

import pandas as pd
import requests
from bs4 import BeautifulSoup

wikiurl = "https://en.wikipedia.org/wiki/Bitcoin"

response = requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
bs_html = BeautifulSoup(response.text, "html.parser")

tabledata = bs_html.find("table", {"class": "infobox"})

# read the table data
df = pd.read_html(str(tabledata))

# convert list to pandas dataframe
df = pd.DataFrame(df[0])
print(df.head())

# write the data to a .csv file
df.to_csv("bitcoin_info.csv", sep="\t", encoding="utf-8")

# the data is not structured well so cleaning data wouldn't make sense
