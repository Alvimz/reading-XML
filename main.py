from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook,Workbook

class Logic:
    def __init__(self) -> None:
        self.search_tag= [] #lista para armazenar as tags diretamente do xml
        self.result_links = [] #lista com os links válidos!
        self.error_links = [] #lista com os links errôneos
        
    def get_site_xml(self): #pega linha por linha do xml e armazena na lista 'search_tag'
        with open("urls.xml", "r") as file:
            line = file.read()
        content = BeautifulSoup(line,'xml')
        
        for item in content.find_all('site'): #salva apenas o link na lista
            self.search_tag.append(item.text)
        
        return self.search_tag #retornando em lista com os valores
    

    
    def check_url(self): #testa as urls e as separa se funfa ou não!
        
        for urls in self.search_tag:
                      
            try:
                maybe_url = requests.get(urls)
                if maybe_url.status_code == 200:
                    self.result_links.append(urls)
                
                
            except:
                self.error_links.append(urls)
                
        return self.result_links, self.error_links
        
    def add_link_xlsx(self):
        try:
            
            wb = load_workbook('links.xlsx')
            workbook_active = wb.active
        except:
            wb = Workbook()
            workbook_active= wb.active
        for link in self.result_links:
            workbook_active.append([link,'Link válido!'])
        for link in self.error_links:
            workbook_active.append([link,'Link inválido!'])
        wb.save('links.xlsx')
        
            
            
        
        
        
    
    

a = Logic()
a.get_site_xml()
#print(a.requesition_links())
result_links,error_links = a.check_url()
a.add_link_xlsx()
print(result_links)
print(error_links)

