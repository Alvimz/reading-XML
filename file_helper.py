import os
from lxml import etree

class FileHelper(object):

    def __init__(self) -> None:
        self._test = "Rene"

    @staticmethod
    def check_file_exist(file_path: str) -> None:
        if not os.path.isfile(file_path):
            raise Exception('File Path is invalid')    
        
    @staticmethod
    def get_xml_content(file_path: str) -> etree._Element:
        xml_content = None
        with open(file_path, "r") as file:
            file_content = file.read()
            xml_content = etree.fromstring(file_content)
        return xml_content