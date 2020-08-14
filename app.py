# NLP 

# summarizes a news article
# nltk, newspaper3k
from flask import Flask, render_template, request, redirect, url_for
import os
from bson.objectid import ObjectId
import requests
import re

import nltk
import newspaper
from newspaper import Article
from PIL import Image

# from bs4 import BeautifulSoup
import scrape
import dog
# from scrape import scraper

app = Flask(__name__)


# article_list = list()

import collections 
# initializing deque


@app.route('/')
def index():
    """Return homepage."""

    return render_template('home.html')


@app.route('/update', methods=["POST"])
def update():

    url = request.form.get('url')
    keywords = request.form.get('keywords')
    num = request.form.get('num')

    my_article = scrape.Scraper(url, keywords, num)
    my_article.scraping()

    # print(my_article.article_list)
    # print(my_article.date_list)
    # print(my_article.link_list)
    # print(my_article.title_list)

    return  render_template('home.html', msg=my_article.msg, article_list=my_article.article_list, authors=my_article.author_list, date=my_article.date_list, link=my_article.link_list, title=my_article.title_list)
    



if __name__ == '__main__':
    app.run(debug=True)