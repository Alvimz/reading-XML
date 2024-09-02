from bs4 import BeautifulSoup

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
    

        

a = Logic()
print(a.get_site_xml())

