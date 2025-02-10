import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.co.uk/news/articles/c9vmym2jvy9o"
response = requests.get(url)

bs_html = BeautifulSoup(response.text, "html.parser")

article = bs_html.find("article", {"class": "ssrcss-15tkd6i-ArticleWrapper e1nh2i2l3"})

article_text = article.get_text()

print(article_text)
