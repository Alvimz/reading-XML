from bs4 import BeautifulSoup

class Logic:
    def __init__(self) -> None:
        self.search_tag= [] #lista para armazenar as tags
    
    #pega linha por linha do xml e armazena na lista 'search_tag'
    
    def get_site_xml(self):
        with open("urls.xml", "r") as file:
            line = file.read()
        content = BeautifulSoup(line,'xml') 
        self.search_tag = content.find_all('site') #procurando por tag
        return self.search_tag #retornando em lista com os valores
    
    def remove_tag(self):
        for item in self.search_tag:
            print(item.text)
        ...
        

a = Logic()

a.get_site_xml()
a.remove_tag()

