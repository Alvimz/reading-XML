from report import Report
from concurrent.futures import ThreadPoolExecutor
class PoolRequest:
    ...
    
    def process_request(self,request,path_save):
        report = Report()
        with ThreadPoolExecutor(max_workers=3) as executor:
            for obj in report.get_list(path_save):
                executor.submit(report.save,obj)