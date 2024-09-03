from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook, Workbook

#recebedor de arquivo!
    #testa se é um arquivo xml! ✔️
#verificar se tem a estrutura de um link!
#verificar espaços em brancos no xml! ✔️

class Logic:
    def __init__(self) -> None:
        self.links_raw = []  # lista para armazenar as tags diretamente do xml
        self.links_validated = []  # lista com os links válidos!
        self.links_error = []  # lista com os links errôneos
        self.supose_path_xml = None
        

    def file_tester_xml(self):
        self.supose_path_xml = input('Digite o diretório do arquivo XML!')
        if '.xml'in self.supose_path_xml:
            return True,self.supose_path_xml
        return False,None
    
    def check_empty_line_xml(self):
        if self.supose_path_xml != None:
            with open(self.supose_path_xml,'r') as file:
                for linha in file:
                    if linha.strip() == '':
                        continue
                return True
        else:
            return False
        
        
    def get_url_xml(self):  # pega linha por linha do xml e armazena na lista 'links_raw'
        with open("urls.xml", "r") as file:
            line = file.read()
        content = BeautifulSoup(line, "xml")

        for item in content.find_all("site"):  # salva apenas o link na lista
            self.links_raw.append(item.text)

        return self.links_raw  # retornando em lista com os valores

    def check_url_xml(self):  # testa as urls e as separa se funfa ou não!
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
print(a.file_tester_xml())
print(a.check_empty_line_xml())
# a.get_url_xml()
# print(a.requesition_links())
# result_links, error_links = a.check_url_xml()
# a.add_link_xlsx()
# print(result_links)
# print(error_links)
