from request_result import RequestResult, RequestResultList

#pesquisar melhor isso pq não entendi! 🟥🟥🟥🟥
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

    def save(self):
        
        for i,obj in enumerate(self.__report):
            file_name = f'Resultado{i+1}.html' 
            with open(file_name,'w') as f:
                
                
                f.write('<html>\n')
                f.write('<head>\n<title>Resultados</title>\n</head>\n')
                f.write('<body>\n')
                f.write(f'<h1>Relatório do link!</h1>\n')
                f.write(f'<p>URL: {obj.url}</p>\n')
                f.write(f'<p>Sucesso?: {obj.success}</p>\n')
                f.write('</body>\n')
                f.write('</html>')
                  
            print(f'Sucesso?{obj.success}')