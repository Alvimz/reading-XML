from bs4 import BeautifulSoup
import requests

class Logic:
    def __init__(self) -> None:
        self.search_tag= [] #lista para armazenar as tags
        self.result_code = []
        
    def get_site_xml(self): #pega linha por linha do xml e armazena na lista 'search_tag'
        with open("urls.xml", "r") as file:
            line = file.read()
        content = BeautifulSoup(line,'xml')
        
        for item in content.find_all('site'): #salva apenas o link na lista
            self.search_tag.append(item.text)
        
        return self.search_tag #retornando em lista com os valores
    
    def requesition_links(self): #fazer requisição dos links
        self.result_code = []
        for links in self.search_tag:
            result = requests.get(links)
            self.result_code.append(result.status_code)
        return self.result_code
    
    def check_url(self): #testa as urls
        checked_urls = []
        for urls in self.search_tag:
                      
            try:
                maybe_url = requests.get(urls)
                if maybe_url.status_code == 200:
                    checked_urls.append(urls)
                
                
            except:
                print(f'Url: {urls} < inválida!')
        return checked_urls, 'Urls verificadas e adicionadas!'
        
            
            
        
        
        
    
    

a = Logic()
print(a.get_site_xml())
#print(a.requesition_links())
print(a.check_url())

