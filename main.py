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

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/cnn')
def cnn():
  result = []
  for article in articles.find({'source': 'CNN'}):
    article['_id'] = str(article['_id'])
    result.append(article)
  return json.dumps(result)

if __name__ == '__main__':
  app.run(debug=True)

