from flask import Flask, render_template, url_for
import pymongo 
import json
import os
import ssl
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = pymongo.MongoClient(os.getenv('MONGO_SRV'), connect=False, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
articles = client.data.articles
known_news = [news['name'] for news in client.data.news.find()]

print(known_news)

@app.route('/')
def home():
  return render_template('homepage.html')

@app.route('/sources')
def sources():
  return render_template('index.html')

@app.route('/<news>')
def article_list(news):
  news = news.upper()
  if news in known_news:
    news_articles = [article for article in articles.find({'source': news})]
    return render_template('article_page.html', news=news, news_articles=news_articles)
  else:
    return '404'

if __name__ == '__main__':
  app.run(debug=True)

