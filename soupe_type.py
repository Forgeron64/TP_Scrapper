from bs4 import BeautifulSoup

class Soupe:
    def __init__(self,value) -> None:
        self.value = value 
    
    def get_nom_videaste(self):
        res = self.value.find("span", itemprop="author").next.next['content']  
        return res
    
    def get_title(self):
        title = self.value.find("meta", itemprop="name")['content']
        return title
    
    def get_description(self):
        description = self.value.find("meta",itemprop="description")['content']  
        return description