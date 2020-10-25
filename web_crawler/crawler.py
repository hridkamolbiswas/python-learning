import requests
from bs4 import BeautifulSoup

class Crawler:

    WEBSITE = "StackOverFlow"

    def __init__(self, weblink):
        self.page = requests.get(weblink).text
        self.soup = BeautifulSoup(self.page, 'lxml')
        
        
    def __str__(self):
        return f"{weblink}"

    def return_soup(self):
        return self.soup


if __name__=='__main__':
    weblink = "https://stackoverflow.com/"
    ob = Crawler(weblink) 
    print(ob)
    print('-'*50)
    #print(Crawler.page)
    print(ob.soup.prettify())