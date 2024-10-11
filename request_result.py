class RequestResult(object):

    @property
    def success(self) -> bool:
        return self._success
    
    @success.setter
    def success(self, value: bool):
        self._success = value

    @property
    def error_message(self) -> str:
        return self._error_message
    
    @error_message.setter
    def error_message(self, value: str):
        self._error_message = value

    @property
    def data(self) -> str:
        return self._data
    
    @data.setter
    def data(self, value: str):
        self._data = value

    @property
    def url(self) -> str:
        return self._url
    
    @url.setter
    def url(self, value: str):
        self._url = value

    @property
    def response_time(self)->float:
        return self._response_time
    
    @response_time.setter
    def response_time(self,value:float):
        self._response_time = value
  
class RequestResultList(list):
    pass