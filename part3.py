__author__ = 'taylor'
# module to get info from site and parse into text
import requests
from bs4 import BeautifulSoup
def get_articles(url):
# pulls info from the url page
    source_code = requests.get(url)
# converts info into text
    plain_text = source_code.text
# parses text
    soup = BeautifulSoup(plain_text, "html.parser")
    i = 0
    date = []
    ur = []
    for article_name in soup.findAll('div', {'class': 'date'}):
        date.append(article_name.string)
        i += 1
        if i > 9:
            break
    i = 0
    for article_name in soup.findAll('div', {'class': 'title'}):
        for links in article_name.findAll('a'):
            ur.append(url + links.get('href'))
    i = 0
    j = 0
    for article_name in soup.findAll('div', {'class': 'title'}):
        title = article_name.findAll('a')
        type(title)
        i += 1
        print(i, "-", date[j], "-", title[0].text, "-", ur[j])
        j += 1
        if i > 9:
            break
get_articles('http://www.technewsworld.com/')
input("")
