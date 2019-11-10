import pymongo 
from dotenv import load_dotenv
from filterNews import filter
import os
import ssl

load_dotenv()

client = pymongo.MongoClient(os.getenv('MONGO_SRV'), connect=False, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
articles = client.data.articles
article_list = ['https://www.wsj.com/articles/blackouts-wildfires-test-california-gov-newsom-in-his-first-crisis-11573398000',
                'https://www.wsj.com/articles/trump-impeachment-inquiry-delves-into-idea-of-quid-pro-quo-11573300802',
                'https://www.wsj.com/articles/judge-says-u-s-womens-soccer-team-paid-less-per-game-than-men-11573253087',
                'https://www.npr.org/2019/11/10/777300611/skeptics-urge-bevin-to-show-proof-of-fraud-claims-warning-of-corrosive-effects',
                'https://www.npr.org/2019/11/10/777591098/like-getting-my-father-back-wwii-pow-s-art-returned-to-his-family',
                'https://www.npr.org/2019/11/10/776052182/who-will-decide-on-the-dalai-lamas-successor-his-supporters-or-beijing']
for article in article_list:
  results = filter(article)
  articles.insert_one({'source': article[12:15].upper(), 'title': results[0], 'obj_score': results[1], 'url': article})


