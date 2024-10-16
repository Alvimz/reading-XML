from concurrent.futures import ThreadPoolExecutor
from http_helper import HTTPHelper
from report import Report
class PoolRequest:
    def __init__(self) -> None:
        self.executor = ThreadPoolExecutor(max_workers=3)
        self.threads_ = list()
        self.report = Report()
    
    def pool_request(self,request_list):
        for url in request_list:
            _thread = self.executor.submit(self.process_url,url)
            self.threads_.append(_thread)
            
    def process_url(self,url):
        content_url = HTTPHelper.get_url_content(url)
        self.report.add_item(content_url)
    
    def wait_complet(self):
        self.executor.shutdown(wait=True)
        