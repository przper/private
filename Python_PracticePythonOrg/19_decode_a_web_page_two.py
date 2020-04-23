"""
Using the requests and BeautifulSoup Python libraries,
print to the screen the full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages.
Your task is to print out the text to the screen so
that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use
the BeautifulSoup and requests libraries through
the solution of the exercise posted here.)

This will just print the full text of the article to the screen.
It will not make it easy to read, so next exercise we will learn
how to write this text to a .txt file.
"""

import requests
from bs4 import BeautifulSoup

url1 = 'https://fakty.interia.pl/polska/news-czy-czeka-nas-katastrofa-demograficzna,nId,3176491'
url2 = 'https://fakty.interia.pl/polska/news-czy-czeka-nas-katastrofa-demograficzna,nId,3176491,nPack,2'
url3 = 'https://fakty.interia.pl/polska/news-czy-czeka-nas-katastrofa-demograficzna,nId,3176491,nPack,3'

r1 = requests.get(url1)  # 'sucking' the html code from url; 'r' is short for 'response'
r2 = requests.get(url2)
r3 = requests.get(url3)
r_html = r1.text + r2.text + r3.text  # converting html code to string

soup = BeautifulSoup(r_html)
i = 0
for text in soup.find_all('p'):
    # print(i, 50 * '-')
    print(text.getText())
    #i += 1
