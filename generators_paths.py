from verification import Verifications
import os
class Paths:
    def __init__(self) -> None:
        self.path_html_output = None
        
    @staticmethod    
    def create_path_html(path):  # cria a pasta para receber os html
        if not Verifications.this_file_exists(path):
            os.makedirs(path)
            print("Pasta criada com sucesso!")
            
        else:
            print("Pasta para os registros já existe!")
            
    def generate_html_path(self,path_lib):
        pasta_nome = "Resultado_xml"
        self.path_html_output=os.path.join(path_lib,pasta_nome)
          # alterar para join futuramente!🟨
        return self.path_html_output