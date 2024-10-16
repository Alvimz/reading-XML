from request_result import RequestResult, RequestResultList
import os
from typing import List

class Report(object):

    def __init__(self) -> None:
        self.__report:List[RequestResult] = list()
        
        
    def add_item(self, rr: RequestResult):
        self.__report.append(rr)

    def add_items(self, RequestResultList):
        self.__report.extend(RequestResultList)


    def print(self):
        for result in  self.__report:
            print("Worked? %s/t URL: %s " % (result.success, result.url ))

    def save(self,path):
        
        for i,obj in enumerate(self.__report):
            file_name = f'Resultado{i+1}.html'
            final_output_html = os.path.join(path,file_name)
            with open(final_output_html,'w') as f:
                f.write('<html>\n')
                f.write('<head>\n<title>Resultados</title>\n</head>\n')
                f.write('<body>\n')
                f.write(f'<h1>Link: {obj.url}</h1>\n')
                f.write(f'<p>Time to process: {obj.response_time}</p>\n')
                f.write(f'<p>Success?: {obj.success}</p>\n')
                f.write('</body>\n')
                f.write('</html>')
                  
