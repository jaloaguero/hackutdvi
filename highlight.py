import unsortedMap
from bs4 import BeautifulSoup
import urllib.request
from newspaper import Article

d = unsortedMap.makeDictionary()
article = Article('https://cnn.com/2019/11/08/opinions/ok-boomer-callan-filipovic/index.html')
article.download()
article.parse()

s = str(article.text)

html1 = """<!DOCTYPE HTML>
<!--
	Phase Shift by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
	<head>
		<title>Fact Filter</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<!--[if lte IE 8]><script src="css/ie/html5shiv.js"></script><![endif]-->
		<script src="static/js/jquery.min.js"></script>
		<script src="static/js/jquery.dropotron.min.js"></script>
		<script src="static/js/skel.min.js"></script>
		<script src="static/js/skel-layers.min.js"></script>
		<script src="static/js/init.js"></script>
		<link rel="stylesheet" href="/static/css/skel.css">
		<link rel="stylesheet" href="/static/css/style.css">
		<link rel="stylesheet" href="/static/css/style-wide.css">
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
	</head>
	<body>

		<!-- Wrapper -->
			<div class="wrapper style1">

				<!-- Header -->
					<div id="header" class="skel-panels-fixed">
						<div id="logo">
							<h1><a href="sources">Fact Filter</a></h1>
							<span class="tag">Stay Skeptical.</span>
						</div>
						<nav id="nav">
							<ul>
								<li class="active"><a href="#">Homepage</a></li>
								<li><a href="sources">Browse News Sources</a></li>
								<li><a href="enter_url">Check Specific Article</a></li>
							</ul>
						</nav>
					</div>
				<!-- Header -->

				<!-- Page -->

				<div id="page" class="container">"""

f = open("highlight_article.html", "w+")
f.write(html1)

newstr = "mark {\n\tbackground: green;\n\tcolor: black;\n}\n<html>\n<header><title>Objectify</title></header>\n<body>\n"
for word in s.split():
    if word in d and d[word] > 0.75:
        f.write("<mark>")
        f.write(str(word))
        f.write("</mark>" + " ")
        # under 75 and in dictionary
    else:
        f.write(str(word) + " ")

html2 = """					</div>

				<!-- /Page -->



	</div>



	<!-- Copyright -->
		<div id="copyright">
			<div class="container"> <span class="copyright">Design: <a href="http://templated.co">TEMPLATED</a> Images: <a href="http://unsplash.com">Unsplash</a> (<a href="http://unsplash.com/cc0">CC0</a>)</span>
				<ul class="icons">
					<li><a href="https://github.com/jaloaguero/hackutdvi" class="fa fa-github"><span>Github</span></a></li>
				</ul>
			</div>
		</div>

	</body>
</html>"""

f.write(html2)
f.close()