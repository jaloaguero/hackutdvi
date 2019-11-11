from flask import Flask, render_template, url_for, request
import pymongo 
import json
import os
import ssl
from dotenv import load_dotenv
from filterNews import filter, d
from highlight import highlight

load_dotenv()

app = Flask(__name__)

client = pymongo.MongoClient(os.getenv('MONGO_SRV'), connect=False, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
articles = client.data.articles
known_news = [news['name'] for news in client.data.news.find()]

print(known_news)

@app.route('/')
def home():
  return render_template('homepage.html')

@app.route('/enter_url', methods=['GET', 'POST'])
def enter_url():
  if request.method == 'GET':
    return render_template('enter_url.html')
  else:
    highlight(request.form['url'], d)
    return render_template('highlighted_article.html')

@app.route('/sources')
def sources():
  return render_template('index.html')

@app.route('/<news>')
def article_list(news):
  news = news.upper()
  if news in known_news:
    news_articles = [article for article in articles.find({'source': news})]
    return render_template('article_page.html',
                           news=news,
                           news_articles=news_articles)
  else:
    return '404'

@app.route('/<news>/<article_url>')
def show_highlight(news, article_url):
  news = news.upper()
  article_url = articles.find_one({'title': article_url})['url']
  print(article_url)
  if news in known_news:
#     article_url = 'https://www.foxnews.com/us/man-arrested-for-stabbing-baby-trump-protest-balloon-at-alabama-lsu-game'
    highlight(article_url, d)
    return render_template('highlighted_article.html')
  else:
    return '404'

if __name__ == '__main__':
  app.run(debug=True)

