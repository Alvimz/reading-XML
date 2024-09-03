from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook, Workbook
import re

#recebedor de arquivo!
    #Verifica peso do arquivo! ❌
    #testa se é um arquivo xml! ✔️
#verificador de link
    #verificar se tem a estrutura de um link e o adiciona na lista! ❌
    #verificar espaços em brancos no xml e o add na lista! ❌
    #reformular os códigos e tirar esse mundo de lista! ❌
"""
Pessoa introduz um xml, ele pegará todos os links(tirando os espaços vazios , descartando os digitados errados, linhas em brancos, coisas que
forem links!), dará um get e salvará o retorno em um arquivo a parte!

"""


class Logic:
    def __init__(self) -> None:
        self.links_raw = []  # lista para armazenar as tags diretamente do xml
        self.links_without_space = [] #lista dos links sem espaço!
        self.links_validated = []  # lista com os links válidos!
        self.links_error = []  # lista com os links errôneos
        self.supose_path_xml = None #path do xml!
        
    
    def path_tester_xml(self):#testa se é um xml o que a pessoa está introduzindo!
        self.supose_path_xml = input('Digite o diretório do arquivo XML!')
        if '.xml'in self.supose_path_xml:
            return True,self.supose_path_xml
        return False,None
    
    #checa se tem linhas vazias já salvando na lista raw!
    def check_empty_line_xml(self):
        if self.supose_path_xml != None: #corrigir isto 🟥
            
            for link in self.links_raw:
                if link.strip() == '':
                    continue
                self.links_without_space.append(link)
            return self.links_without_space
            
        
        
    def get_line_from_xml(self):  # pega linha por linha do xml e armazena na lista 'links_raw'
        with open(self.supose_path_xml, "r") as file:
            line = file.read()
        content = BeautifulSoup(line, "xml")

        for item in content.find_all("site"):  # salva apenas o link na lista
            
            self.links_raw.append(item.text)

        return self.links_raw  # retornando em lista com os valores
    
    def check_if_its_url(self):
        pattern_url = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+.com.*'
        for links in self.links_raw:
            try:
                
                if re.match(pattern_url,links):
                    self.links_validated.append(links)
                    return self.links_validated
            except:
                self.links_error.append(links)

    def check_if_url_works_xml(self):  # testa as urls e as separa se funfa ou não!
        for urls in self.links_raw:
            try:
                maybe_url = requests.get(urls)
                if maybe_url.status_code == 200:
                    self.links_validated.append(urls)

            except:
                self.links_error.append(urls)

        return self.links_validated, self.links_error

    def add_link_xlsx(self):  # passa os links para a planilha!
        try:
            # carrega a planilha caso ela não exista
            work_book = load_workbook("links.xlsx")
            workbook_active = work_book.active
        except:
            # cria a planilha!
            work_book = Workbook()
            workbook_active = work_book.active
        for link in self.links_validated:  # adiciona os links válidos
            workbook_active.append([link, "Link válido!"])
        for link in self.links_error:  # adiciona os links não válidos!
            workbook_active.append([link, "Link inválido!"])
        work_book.save("links.xlsx")
    
  

a = Logic()
a.path_tester_xml()
print(a.get_line_from_xml())
print('Acima direto do xml')
a.check_empty_line_xml()
print(a.links_without_space)

