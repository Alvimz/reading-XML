import requests
import validators
import time
from request_result import RequestResult
from time_passed import TimePassed

class HTTPHelper(object):
    @staticmethod
    @TimePassed
    def get_url(url) -> str:
        httpResponse = requests.get(url, timeout=3)
        
        if httpResponse.status_code == 200:
                return httpResponse.text

    @staticmethod
    def is_valid_url(url):
        return validators.url(url) 
    
    @staticmethod
    def get_url_content_and_time(url) -> RequestResult:
        rr = RequestResult()
        rr.success = True
        rr.url = url
        rr.response_time = 0
        
        try:
            if not HTTPHelper.is_valid_url(url):
                rr.success = False
                rr.error_message = "URL is not valid"
            else:
                rr.data = HTTPHelper.get_url(url)
                rr.response_time = HTTPHelper.get_url.execution_time



        except Exception as ex:
            rr.success = False
            rr.data = str(ex)

        return rr