from bs4 import BeautifulSoup

class Logic:
    def get_site_xml():
        with open("urls.xml", "r") as file:
            line = file.read()
        content = BeautifulSoup(line,'xml') 
        search_tag = content.find_all('site') #procurando por tag
        return search_tag #retornando em lista os valores
        
    
a = Logic
lista_xml = a.get_site_xml()
print(lista_xml[1])