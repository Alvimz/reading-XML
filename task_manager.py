from file_helper import FileHelper
from report import Report
from request_result import RequestResult, RequestResultList
from http_helper import HTTPHelper

class TaskManager(object):
    def __init__(self) -> None:
        self._file_path = None
        self._http_request_limit = 0

    @property #setando 'file_path' como privado! para utiliza-lo pelo set!
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        FileHelper.check_file_exist(value)
        self._file_path = value

    @property
    def http_request_limit(self):
        return self._http_request_limit
    
    @http_request_limit.setter
    def http_request_limit(self, value):
        self._http_request_limit = value


    def start(self):
        file_content = FileHelper.get_xml_content(self.file_path) #pq não pode ser o privado???
        urls = file_content.findall("site")
        report = Report() #confirmar isto! 
        print("---------------------------")
        print("Processing requests...")
        print("---------------------------")
        for url in urls:
            print(".")
            report.add_item(HTTPHelper.get_url_content(url.text)) 
        print("---------------------------")
        print("DONE - Processing requests.")
        print("---------------------------")
        report.print()
        

    