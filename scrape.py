
url = 'http://lite.cnn.com/en'

url2 = 'https://news.ycombinator.com/'

from bs4 import BeautifulSoup
import requests
import os
from bson.objectid import ObjectId

import nltk
from newspaper import Article
from PIL import Image


class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get(url).text

    def parse(self):
        soup = BeautifulSoup(self.markup, 'html.parser')
        links = soup.findAll("a")
        for link in links:
            print(link)
            # article = Article(link, language="en")
