# NLP 

# summarizes a news article
# nltk, newspaper3k
from flask import Flask, render_template, request, redirect, url_for
import os
from bson.objectid import ObjectId
import requests
import re

import nltk
from newspaper import Article
from PIL import Image

from bs4 import BeautifulSoup


app = Flask(__name__)


# article_list = list()

import collections 
# initializing deque


@app.route('/')
def index():
    """Return homepage."""

    return render_template('index.html')



@app.route('/updated', methods=["POST"])
def updated():
    article_list = collections.deque()
    date_list = collections.deque()
    link_list = collections.deque()
    title_list = collections.deque()
    msg = ''
    url = request.form.get('url')
    keys = request.form.get('keywords')
    
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # links = soup.findAll("li", {"a"})
    links = soup.select("li a", attrs={'href': re.compile("^http://")})
    # print(links)
    for link in links:
        # print("****** LINK: ", link.get('href'))
        # print("KEYS: ", keys)
        full_link = url+link.get('href')[3:]
        # print(full_link)
        article = Article(full_link, language="en")
        article.download()
        article.parse()
        article.nlp()
        # article_list.appendleft((article.authors))
        # article_list.appendleft((article.keywords))
        # article_list.appendleft((article.text))
        # print(article.keywords)
        if keys != '':
            for item in article.keywords:
                for item2 in keys.split(' '):
                    # print(item.lower(), item2.lower())
                    if item.lower() == item2.lower():
                        # print("MATCH ", item, item2)
                        if full_link in link_list:
                            continue
                        else:
                            article_list.appendleft((article.summary))
                            date_list.appendleft((article.publish_date))
                            link_list.appendleft((full_link))
                            title_list.appendleft((article.title))
        else:
            article_list.appendleft((article.summary))
            date_list.appendleft((article.publish_date))
            link_list.appendleft((full_link))
            title_list.appendleft((article.title))
        
    if len(article_list) == 0:
        msg = "No articles"

    print("MSG: ", msg)
    return render_template('index.html', msg=msg, article_list=article_list, date_list=date_list, link_list=link_list, title_list=title_list)
    

if __name__ == '__main__':
    app.run(debug=True)