import unsortedMap
from newspaper import Article

d = unsortedMap.makeDictionary()

def filter(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    # print(article.title)
    avg = 0
    count = 0
    # print(article.text)

    for word in article.text:
        if word in d:
            avg += d[word]
        count += 1
    
    # print("Score: " + str(avg / count))

    return (article.title, avg/count, url)

if __name__ == '__main__':
    filter('https://cnn.com/2019/11/09/politics/trump-balloon-alabama-lsu-football-game/index.html')
