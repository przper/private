"""
Use the BeautifulSoup and requests Python packages to print out
a list of all the article titles on the New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.onet.pl//'
r = requests.get(url)  # 'sucking' the html code from url; 'r' is short for 'response'
r_html = r.text  # converting html code to string
# print(type(r_html), r_html)

soup = BeautifulSoup(r_html)
i = 0
# print(soup.find_all(class_="title"))
for title in soup.find_all(class_="title"):
    i += 1
    print("ARTYKUŁ NR {}:".format(i),title.contents[0])
