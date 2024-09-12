from request_result import RequestResult, RequestResultList
import os


class Report(object):

    def __init__(self) -> None:
        self.__report = list()
        
        
    
    def add_item(self, rr: RequestResult): #especificando que a lista recebe valores do ResultRequest(data)!
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
                f.write(f'<h1>Relatório do link!</h1>\n')
                f.write(f'<p>URL: {obj.url}</p>\n')
                f.write(f'<p>Sucesso?: {obj.success}</p>\n')
                f.write('</body>\n')
                f.write('</html>')
                  
            print(f'Sucesso?{obj.success}')