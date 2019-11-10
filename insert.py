import pymongo 
from dotenv import load_dotenv
from filterNews import filter
import os
import ssl

load_dotenv()

client = pymongo.MongoClient(os.getenv('MONGO_SRV'), connect=False, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
articles = client.data.articles
article_list = ['https://www.pbs.org/wgbh/frontline/article/artificial-intelligence-work-jobs-robots-v-humans/',
                'https://www.pbs.org/wgbh/frontline/article/no-danger-to-paradise-911-callers-were-told-as-the-deadly-camp-fire-approached/']
for article in article_list:
  results = filter(article)
  if results:
    articles.insert_one({'source': article[12:15].upper(), 'title': results[0], 'obj_score': results[1], 'url': article})


