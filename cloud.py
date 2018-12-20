from abc import *
from bs4 import BeautifulSoup
from exceptions import *
import requests
import re


class Cloud(metaclass=ABCMeta):
    def __init__(self, url):
        self.url = url
        self.request = requests.get(self.url)
        self.confirm_request_url()
        self.confirm_url(self.url)

    def conversion_size(self, file, size_type=None):
        size = int(file['size'])
        unit = file['unit']
        standard_unit = {'B': 0, 'K': 10, 'M': 20, 'G': 30, 'T': 40}
        if size_type is not None:
            if unit == size_type:
                return size
            else:
                if size_type not in standard_unit.keys():
                    raise SizeTypeError(size_type)
                else:
                    transformed_size = size * pow(2, standard_unit[unit] - standard_unit[size_type])
                    return transformed_size
        else:
            return size

    def get_html(self):
        document = BeautifulSoup(self.request.content, 'html.parser')
        return document

    def confirm_request_url(self):
        if self.request.status_code == 200:
            if self.request.url != self.url:
                self.url = self.request.url
        else:
            raise InvalidURLError(self.url)

    @abstractmethod
    def file_size(self, size_type):
        pass

    @abstractmethod
    def confirm_url(self, url):
        pass
