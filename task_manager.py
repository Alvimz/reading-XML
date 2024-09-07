from file_helper import FileHelper

class TaskManager(object):
    def __init__(self) -> None:
        self._file_path = None
        self._http_request_limit = 0

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        # Verification
        FileHelper.check_file_exist(value)
        self._file_path = value


    @property
    def http_request_limit(self):
        return self._http_request_limit
    
    @http_request_limit.setter
    def http_request_limit(self, value):
        self._http_request_limit = value


    def start(self):
        file_content = FileHelper.get_xml_content(self.file_path)
        urls = file_content.findall("site")
        for url in urls:
            print (url.text)


    def get_url_content(url):
        pass