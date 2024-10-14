from file_helper import FileHelper
from report import Report
from request_result import RequestResult, RequestResultList
from http_helper import HTTPHelper
import threading

class TaskManager(object):
    def __init__(self) -> None:
        self._file_path = None
        self._http_request_limit = 0
        self._output_path = None
        self.final_html = None
        

    @property #getter
    def file_path(self):
        return self._file_path

    @file_path.setter #setter
    def file_path(self, value):
        FileHelper.check_file_exist(value)
        self._file_path = value

    @property
    def http_request_limit(self):
        return self._http_request_limit
    
    @http_request_limit.setter
    def http_request_limit(self, value):
        self._http_request_limit = value

#----------------
    @property
    def output_path(self):
        return self._output_path
    
    @output_path.setter
    def output_path(self,value):
        
        self._output_path = value
        self.final_html = FileHelper.create_folder_output(value) #aqui está vindo None!
        
        
        
        
#---------------

    def start(self):
        file_content = FileHelper.get_xml_content(self.file_path) #pq não pode ser o privado???
        urls = file_content.findall("site") #isto continua
        report = Report()  
        
        print("---------------------------")
        print("Processing requests...")
        print("---------------------------")
        for url in urls: #mudar esta estrutura ✋
            print(".")
            report.add_item(HTTPHelper.get_url_content(url.text))
            
        print("---------------------------")
        print("DONE - Processing requests.")
        print("---------------------------")
        report.print()
        report.save(self.final_html)
        

