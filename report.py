from request_result import RequestResult, RequestResultList
import os
from typing import List
from temporary_log import TemporaryLog
from aps import Aps
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

    def save(self):
        temporary_log = TemporaryLog()
        aps = Aps()
        for obj in self.__report:
            if obj.response_time !=0:
                temporary_log.get_numbers_report(obj.response_time)
        temporary_log.avg_report()
        aps.start(temporary_log.save_csv_log,2)
        temporary_log.save_csv_log()
              
