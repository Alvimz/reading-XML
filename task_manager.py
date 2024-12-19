from file_helper import FileHelper
from report import Report
from request_result import RequestResult, RequestResultList
from http_helper import HTTPHelper
from time_passed import TimePassed
from poolrequest import PoolRequest
import keyboard
from aps import Aps
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

    
        

    def start(self):
        file_content = FileHelper.get_xml_content(self.file_path) 
        urls = file_content.findall("site")
        report = Report()
        pool = PoolRequest()
        aps = Aps()
        print("---------------------------")
        print("Processing requests...")
        print("---------------------------")
        
        def process_url(urls_process):
            content_url = HTTPHelper.get_url_content(urls_process)
            report.add_item(content_url)
        aps.start(report.write_log,1)
        for url in urls:
            pool.run(process_url,url.text)
        pool.wait_4_complete()
        report.print()
        report.save()
        pool.shutdown()
        aps.stop()
            
        
        print("---------------------------")
        print("DONE - Processing requests.")
        print("---------------------------")
        
        
        
        

