# Web Scrape Wikipedia
# written by Joe Manlove (maybe with substantial plagerism, can't recall source)
# created 8/5/2020
# revised 11/8/2020

import requests
from bs4 import BeautifulSoup

# Use the requests library to get the information from a website
request_results = requests.get('https://en.wikipedia.org/wiki/Hand_scraper')

# create a BeautifulSoup object from the text of the request and parse it as html
wiki_page = BeautifulSoup(request_results.text, "html.parser")

# To print the whole thing in the console
print(wiki_page.prettify())

# print just the paragraphs
for paragraph in wiki_page.select('p'):
    print(paragraph.getText())
