import os
import re
class verifications:
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
            
            return True
        
        @staticmethod
        def this_file_exists(file):
            if os.path.exists(file):
                return True
            
        @staticmethod
        def this_a_path(path):
            pattern_path = r"^([a-zA-Z]:\\|\/)?((?:[^<>:\"\/\\|?*\n]+[\/\\]?)+)$"

            if re.match(pattern_path,path):
                return True
            print('Insira um diretório!')
            
        @staticmethod
        def this_urls_works(url):
            pattern_url = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(\.[a-zA-Z]{2,})(?:/.*)?"
            if re.match(pattern_url,url):
                return True
            
            