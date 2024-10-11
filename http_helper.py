import requests
import validators
import time
from request_result import RequestResult
from time_passed import TimePassed

class HTTPHelper(object):
    @staticmethod
    def get_url(url) -> str:
        start_time = time.time()
        httpResponse = requests.get(url, timeout=3)
        elapsed_time = time.time() - start_time
        print(f"Tempo para GET em {url}: {elapsed_time:.2f} segundos")
        
        if httpResponse.status_code == 200:
                return httpResponse.text

    @staticmethod
    def is_valid_url(url):
        return validators.url(url) 
    
    @staticmethod
    def get_url_content(url) -> RequestResult:
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
                

        except Exception as ex:
            rr.success = False
            rr.data = str(ex)

        return rr