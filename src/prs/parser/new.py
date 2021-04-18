from abc import ABC, abstractclassmethod
import requests
from bs4 import BeautifulSoup as BS

class Parser(ABC):
    @abstractclassmethod
    def get_data(self): ...#get all lnks from page
       
    @abstractclassmethod
    def process_data(self): ...

    @abstractclassmethod
    def save_data(self): ...

class ParserLinks(Parser):
    _url = "https://www.lse.co.uk/news/archive.html?page={}"
    def __init__(self, num_page):
        self._num_page = num_page
        self._links= []

    def get_data(self):
        response = requests.get(self._url.format(self._num_page))
        #print(dir(response))
        if response.status_code == 200:
            self.dom = BS(response.text, "html.parser")
        else:
            raise ValueError("Was returned {0}".format(response.status_code))

         
        #print(response.text)

    def process_data(self):
        try:
            container = self.dom.find("div", class_= "wrapper-3-col__center")
            
        except AttributeError:
            raise AttributeError("srazy det_data!")
        
        container = container.find("div", class_ = "news__archive")
        links = container.find_all("a", class_ = "news__story-title-link")
        self._links = [a["href"] for a in links]
        #print(links)
        
    def save_data(self):
        

class ParserNews(Parser):
    
    def get_data(self): ...#get all lnks from page
       
    
    def process_data(self): ...

    
    def save_data(self): ...


if __name__ == "__main__":
    link_parser = ParserLinks(num_page=31372)
    link_parser.get_data()
    link_parser.process_data()
    


