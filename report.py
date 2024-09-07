from request_result import RequestResult, RequestResultList


class Report(object):

    def __init__(self) -> None:
        self.__report = list()
    
    def add_item(self, rr: RequestResult):
        self.__report.append(rr)

    def add_items(self, RequestResultList):
        self.__report.extend(RequestResultList)


    def print(self):
        for result in  self.__report:
            print("Worked? %s/t URL: %s " % (result.success, result.url ))

    def save(self):
        pass