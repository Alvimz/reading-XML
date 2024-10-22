from old_files.verification import Verifications
import os
class Paths:
 
        
    
    
        
        
    def create_lib_html(path):  # cria a pasta para receber os html
        if not Verifications.this_file_exists(path):
            os.makedirs(path)
            print("Pasta criada com sucesso!")
            
        else:
            print("Pasta para os registros já existe!")
           
    def generate_html_path(path_lib):
        pasta_nome = "Resultado_xml"
        path_html_output =os.path.join(path_lib,pasta_nome)
         
        print('Link de output criado com sucesso!')
        return path_html_output

