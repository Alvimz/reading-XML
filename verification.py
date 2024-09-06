import os
import re
import requests
class Verifications:
        @staticmethod
        def file_size(path_xml):
            
            if os.path.getsize(path_xml) < 10 *1024 *1024:
                return True
            else:
                print('Arquivo muito pesado!')
                return False
        
        @staticmethod
        def empty_input(answer):
            if answer:
                
                
                return False
            print('Por favor, insira algo!')
            return True
        
        @staticmethod
        def this_file_exists(file):
            if os.path.exists(file):
                return True
            
        @staticmethod
        def this_path_works(path):
            pattern_path = r"^[a-zA-Z]:(\\|\/)[^<>:\"\/\\|?*\n]+(\\|\/)[^<>:\"\/\\|?*\n]+$"


            if re.match(pattern_path,path):
                return True
            else:
                
                print('Insira um diretório!')
            
        @staticmethod
        def this_urls_works(url):
            pattern_url = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(\.[a-zA-Z]{2,})(?:/.*)?"
            if re.match(pattern_url,url):
                return True
            
        @staticmethod
        def get_links(link):
            try:
                
                requests.get(link)
                return True
            except:
                return False
        @staticmethod
        def this_is_a_xml(path):
            pattern_path = r"^[a-zA-Z]:\\(?:[^<>:\"\/\\|?*\n]+\\)*[^<>:\"\/\\|?*\n]+\.(xml)$"
            if re.match(pattern_path,path):
                return True
            

