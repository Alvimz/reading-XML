from bs4 import BeautifulSoup
import requests

import re
import os

#recebedor de arquivo!
    #Verifica peso do arquivo! ❌
    #criando uma pasta dentro da outra!✔️
     
    #testa se é um arquivo xml! ✔️
#verificador de link
    #verificar se tem a estrutura de um link e o adiciona na lista! ❌
    #verificar espaços em brancos no xml e o add na lista! ✔️
     
#distribui os links em htmls
    #criação da pasta para inserção dos htmls!✔️
    #criação arquivo htmls com o resultado do get!❌
#inputs
    #verifica se o que o cara digitou é vazio❌
"""
Pessoa introduz um xml, ele pegará todos os links(tirando os espaços vazios , descartando os digitados errados, linhas em brancos, coisas que
forem links!), dará um get e salvará o retorno em um arquivo a parte!

"""


class Logic:
    
    def __init__(self) -> None:
        self.links_raw = []  # lista para armazenar as tags diretamente do xml
        
        self.links_validated = []  # lista com os links válidos!
        self.links_error = []  # lista com os links errôneos
        self.supose_path_xml = None #path do xml!
        self.supose_path_lib = None #path lib!
        self.pasta_name = 'Resultado_xml'
        self.path_html_final = None
        
        
    def create_path_html(self):#cria a pasta para receber os html
        
        
        if not os.path.exists(self.path_html_final):
            os.makedirs(self.path_html_final)
            print('Pasta criada com sucesso!')
        else:
            print('Pasta para os registros já existe!')
            
    def get_paths_xml_lib_html(self): #pega os diretórios para executa-los!
        self.supose_path_xml = input('Digite o diretório do arquivo XML!')
        if self.supose_path_xml.endswith('.xml'):
            self.supose_path_lib = input('Digite agora onde deseja salvar a pasta de retorno do xml! ')
            #🆘 adicionar testador de input!
            return self.supose_path_xml,self.supose_path_lib
            
            

    
    def empty_input():
        answer = input('>')
        if not answer:
            return True

            
        
        
    def get_line_from_xml(self):  # pega linha por linha do xml e armazena na lista 'links_raw'
        with open(self.supose_path_xml, "r") as file:
            line = file.read()
        content = BeautifulSoup(line, "xml")

        for item in content.find_all("site"):  # salva apenas o link na lista
            
            if item.text.strip() == '':
                continue
            self.links_raw.append(item.text)

        return self.links_raw  # retornando em lista com os valores
    
    def check_if_its_url(self): #verifica se o link funciona , dividindo entre os funcionais e os não funcionais!
        pattern_url = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(\.[a-zA-Z]{2,})(?:/.*)?'
            
        for links in self.links_raw:
                           
            if re.match(pattern_url,links):
                self.links_validated.append(links)
            
            else:
                       
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


        
        
        
        #cria a path para geração dos html!
    def generate_html_path(self):
        self.path_html_final = f'{self.supose_path_lib}/{self.pasta_name}'
        return self.path_html_final
    
    def create_htmls_validated(self):
        print(1,2,3)
        
            
            
            

    
  

a = Logic()

a.get_paths_xml_lib_html() #pegar os paths

a.generate_html_path()
a.create_path_html() 
a.get_line_from_xml() #pega as linhas do xml!
a.check_if_its_url()


a.create_htmls_validated() #empacando aqui!




