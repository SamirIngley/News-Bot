import nltk
import newspaper
from newspaper import Article
import collections

class Scraper:

    def __init__(self, url, keywords, num):

        self.url = url
        self.keywords = keywords
        self.num = num
        self.article_list = collections.deque()
        self.author_list = collections.deque()
        self.date_list = collections.deque()
        self.link_list = collections.deque()
        self.title_list = collections.deque()
        self.msg = ''
    
    def scraping(self):
        paper = newspaper.build(self.url, memoize_articles=False)
        print("size: ", paper.size())

        counter = 0
        scanum = int(self.num)
        first_hundred = paper.articles[:scanum]

        for article in first_hundred:
            new_article = Article(url=article.url, language="en")
            print(counter)
            try:
                new_article.download()
                new_article.parse()
                new_article.nlp()
                counter += 1
                # print(new_article.keywords)
                # print(new_article.url)
                for item in self.keywords.split(' '):
                    # print("KEY: ", item.lower())
                    for item2 in new_article.keywords:
                        print(item2.lower(), item.lower())
                        if item.lower() == item2.lower() and new_article.url not in self.link_list:
                            print("MATCH")
                            self.article_list.appendleft(new_article.summary)
                            self.author_list.appendleft(new_article.authors)
                            self.date_list.appendleft((new_article.publish_date))
                            self.link_list.appendleft((new_article.url))
                            self.title_list.appendleft((new_article.title))
            except:
                pass


        if len(self.article_list) == 0:
            self.msg = "No articles"

        print("MSG: ", self.msg)
        # return (self.msg, self.article_list, self.date_list, self.link_list, self.title_list)




# def scraper(url, keywords):
#     article_list = collections.deque()
#     date_list = collections.deque()
#     link_list = collections.deque()
#     title_list = collections.deque()

#     # url = request.form.get('url')
#     # keywords = request.form.get('keywords')
#     msg = ''

#     # print("url: ", url)
#     # print("keywords: ", keywords)
#     paper = newspaper.build(url, memoize_articles=False)
#     print("size: ", paper.size())

#     counter = 0
#     first_hundred = paper.articles[:20]

#     for article in first_hundred:
#         new_article = Article(url=article.url, language="en")
#         print(counter)
#         try:
#             new_article.download()
#             new_article.parse()
#             new_article.nlp()
#             counter += 1
#             # print(new_article.keywords)
#             # print(new_article.url)
#             for item in keywords.split(' '):
#                 # print("KEY: ", item.lower())
#                 for item2 in new_article.keywords:
#                     # print(item2.lower())
#                     if item.lower() == item2.lower() and new_article.url not in link_list:
#                         print("MATCH")
#                         article_list.appendleft(new_article.summary)
#                         date_list.appendleft((new_article.publish_date))
#                         link_list.appendleft((new_article.url))
#                         title_list.appendleft((new_article.title))
#         except:
#             pass


#     if len(article_list) == 0:
#         msg = "No articles"
#     print("MSG: ", msg)
#     return (msg, article_list, date_list, link_list, title_list)
