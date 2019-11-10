import pymongo 
from dotenv import load_dotenv
from filterNews import filter
import os
import ssl

load_dotenv()

client = pymongo.MongoClient(os.getenv('MONGO_SRV'), connect=False, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
articles = client.data.articles
article_list = ['https://www.wsj.com/articles/blackouts-wildfires-test-california-gov-newsom-in-his-first-crisis-11573398000',
                'https://www.vox.com/2019/11/8/20928604/jaime-harrison-south-carolina-senate-race-lindsey-graham']
for article in article_list:
  results = filter(article)
  articles.insert_one({'source': article[12:15].upper(), 'title': results[0], 'obj_score': results[1], 'url': article})


