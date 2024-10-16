from request_result import RequestResult, RequestResultList
import os
from typing import List

class Report(object):

    def __init__(self) -> None:
        self.__report:List[RequestResult] = list()
        
        
    def add_item(self, rr: RequestResult):
        rr.processed = False
        self.__report.append(rr)

    def add_items(self, RequestResultList):
        self.__report.extend(RequestResultList)


    def print(self):
        for result in  self.__report:
            print("Worked? %s/t URL: %s " % (result.success, result.url ))

    def save(self)->str:
        time_list=list()
        for obj in self.__report:
            if obj.response_time !=0:
                time_list.append(obj.response_time)
        avg = sum(time_list)/len(time_list)
        print(f'Average time: {avg:.3f}')        
