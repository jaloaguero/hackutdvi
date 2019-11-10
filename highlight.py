import unsortedMap
from bs4 import BeautifulSoup
import urllib.request
from newspaper import Article

d = unsortedMap.makeDictionary()
article = Article('https://cnn.com/2019/11/08/opinions/ok-boomer-callan-filipovic/index.html')
article.download()
article.parse()

s = str(article.text)

newstr = "mark {\n\tbackground: green;\n\tcolor: black;\n}\n<html>\n<header><title>Objectify</title></header>\n<body>\n"
for word in s.split():
    if word in d and d[word] > 0.75:
        newstr += "<mark>"
        newstr += str(word)
        newstr += "</mark>" + " "
        # under 75 and in dictionary
    else:
        newstr += str(word) + " "

newstr += "\n</body></html>"

#page = newstr.decode("utf8")

f = open("index.html", "w+")
f.write(newstr)
f.close()
