from bs4 import BeautifulSoup
import requests

class Logic:
    def __init__(self) -> None:
        self.search_tag= [] #lista para armazenar as tags
        
    def get_site_xml(self): #pega linha por linha do xml e armazena na lista 'search_tag'
        with open("urls.xml", "r") as file:
            line = file.read()
        content = BeautifulSoup(line,'xml')
        
        for item in content.find_all('site'): #salva apenas o link na lista
            self.search_tag.append(item.text)
        
        return self.search_tag #retornando em lista com os valores
    
    def requesition_links(self):
        result_code = []
        for links in self.search_tag:
            result = requests.get(links)
            result_code.append(result.status_code)
        return result_code
        
        

a = Logic()
print(a.get_site_xml())
print(a.requesition_links())

