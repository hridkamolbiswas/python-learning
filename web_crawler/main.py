import requests
from bs4 import BeautifulSoup


weblink = "https://stackoverflow.com/"

page = requests.get(weblink).text
soup = BeautifulSoup(page, 'lxml')

article = soup.find('div', id =  "content")


print(article.p)
#print(article.prettify())