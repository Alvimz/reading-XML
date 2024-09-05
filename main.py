from bs4 import BeautifulSoup
import requests

import re
import os
from verification import verifications
"""

#recebedor de arquivo!
    #Verifica peso do arquivo! ✔️
    #criando uma pasta dentro da outra!✔️
    
    #testa se é um arquivo xml! ✔️
#verificador de link
    #verificar se tem a estrutura de um link e o adiciona na lista! ✔️
    #verificar espaços em brancos no xml e o add na lista! ✔️
     
#distribui os links em htmls
    #criação da pasta para inserção dos htmls!✔️
    #criação arquivo htmls com o resultado do get!❌
    #criação arquivo htmls verificados/errôneos! ✔️/❌
#inputs
    #verifica se o que o cara digitou é vazio✔️
    Criação de pasta chamada None!
"""


class Logic:
    def __init__(self) -> None:
        self.links_raw = []  # lista para armazenar as tags diretamente do xml

        self.links_validated = []  # lista com os links válidos!
        self.links_error = []  # lista com os links errôneos
        self.supose_path_xml = None  # path do xml!
        self.supose_path_lib = None  # path lib!
        self.pasta_name = "Resultado_xml"  # nome da pasta que será criada para armazenar o output!
        
        self.path_html_output = None  # path da pasta do output html

    
            
        
    
    def create_path_html(self):  # cria a pasta para receber os html
        if not os.path.exists(self.path_html_output) and self.supose_path_lib:
            os.makedirs(self.path_html_output)
            print("Pasta criada com sucesso!")
        else:
            print("Pasta para os registros já existe!")

    def get_paths_xml_lib_html(self):  # pega os diretórios para executa-los!
        self.supose_path_xml = input("Digite o diretório do arquivo XML: ")
        if verifications.xml_light_weight(self.supose_path_xml):
            
        
            
            if self.supose_path_xml.endswith(".xml") and self.empty_input:
                self.supose_path_lib = input("Digite agora onde deseja salvar a pasta de retorno do xml:")
                if not self.empty_input:
                    return self.supose_path_xml, self.supose_path_lib
                else:
                    print('Por favor, insira um diretório!')
                    
            else:
                print('Por favor, insira um arquivo XML!')
            
        
    @staticmethod
    def empty_input(answer):
        if answer:
            
            return False
        
        return True

    def get_line_from_xml(
        self,
    ):  # pega linha por linha do xml e armazena na lista 'links_raw'
        with open(self.supose_path_xml, "r") as file:
            line = file.read()
        content = BeautifulSoup(line, "xml")

        for item in content.find_all("site"):  # salva apenas o link na lista
            if item.text.strip() == "":
                continue
            self.links_raw.append(item.text)

        return self.links_raw  # retornando em lista com os valores

    def check_if_its_url(
        self,
    ):  # verifica se o link funciona , dividindo entre os funcionais e os não funcionais!
        pattern_url = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(\.[a-zA-Z]{2,})(?:/.*)?"

        for links in self.links_raw:
            if re.match(pattern_url, links):
                self.links_validated.append(links)

            else:
                self.links_error.append(links)

    def check_if_url_works_xml(self):  # testa as urls e as separa se funfa ou não!
        for urls in self.links_validated:
            try: #tirar esse try 🟨
                maybe_url = requests.get(urls)
                if maybe_url.status_code != 200:
                    self.links_error.append(urls)
                    self.links_validated.remove(urls)
                    

            except:
                ...
        print('Links adicionados aos seus devidos lugares!')

        return self.links_validated, self.links_error

        # cria a path para geração dos html!

    
    def generate_html_path(self):
        self.path_html_output = f"{self.supose_path_lib}/{self.pasta_name}"  # alterar para join futuramente!🟨
        return self.path_html_output

    def create_htmls_validated(self):  # cria os html verificados!
        pattern_link = r'[<>:"/\\|?*\x00-\x1F]'
        for links in self.links_validated:
            file_name = re.sub(pattern_link, "_", links[7:])
            file_path = os.path.join(self.path_html_output, f"{file_name}.html")
            if os.path.exists(file_path):
                pass
            else:
                with open(file_path, "w") as html_file:
                    html_file.write("<!DOCTYPE html>\n")
                    html_file.write("<html>\n")
                    html_file.write("<head>\n")
                    html_file.write("<title>Link Validado</title>\n")
                    html_file.write("</head>\n")
                    html_file.write("<body>\n")
                    html_file.write(f"<h1>Link Validado: {links}</h1>\n")
                    html_file.write("</body>\n")
                    html_file.write("</html>\n")


a = Logic()

a.get_paths_xml_lib_html()  # pegar os paths

a.generate_html_path()
a.create_path_html()
a.get_line_from_xml()  # pega as linhas do xml!
a.check_if_its_url()
#print(a.links_validated)
#print(a.links_error)


a.create_htmls_validated()  # empacando aqui!
