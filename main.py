from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook, Workbook

"""
- Poderia em vez de usar listas, talvez SETS???
- Não fiz um verificador se é um link! ❌
- Usei as funções e classes! ✅
- Cria a planilha caso não a exista!✅ 



"""


class Logic:
    def __init__(self) -> None:
        self.links_raw = []  # lista para armazenar as tags diretamente do xml
        self.links_validated = []  # lista com os links válidos!
        self.links_error = []  # lista com os links errôneos

    def get_url_xml(self):  # pega linha por linha do xml e armazena na lista 'links_raw'
        with open("urls.xml", "r") as file:
            line = file.read()
        content = BeautifulSoup(line, "xml")

        for item in content.find_all("site"):  # salva apenas o link na lista
            self.links_raw.append(item.text)

        return self.links_raw  # retornando em lista com os valores

    def check_url(self):  # testa as urls e as separa se funfa ou não!
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
a.get_url_xml()
# print(a.requesition_links())
result_links, error_links = a.check_url()
a.add_link_xlsx()
print(result_links)
print(error_links)
