# import random

import pandas as pd
import requests
from bs4 import BeautifulSoup

# get the response in the form of html
wikiurl = "https://en.wikipedia.org/wiki/AFC_Wimbledon"

# check the request was sucsessful (code 200)
response = requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
bs_html = BeautifulSoup(response.text, "html.parser")

# here we find any element with the table tag, there are some of these we dont want on this page.
# So we specify only tables using the "wikitable" class

tabledata = bs_html.find("table", {"class": "wikitable"})

# read the table data
df = pd.read_html(str(tabledata))

# convert list to pandas dataframe
df = pd.DataFrame(df[0])
print(df.head())

# write the data to a .csv file
df.to_csv("team_info.csv", sep="\t", encoding="utf-8")
