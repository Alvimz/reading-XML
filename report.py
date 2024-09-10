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
        pass