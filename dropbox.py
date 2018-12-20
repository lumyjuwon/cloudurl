from cloud import Cloud
from bs4 import BeautifulSoup
import requests
import re


class DropBox(Cloud):

    def confirm_url(self, url):
        url_split = url.split("/")
        if url_split[2] == 'www.dropbox.com' and url_split[3] == 's':
            self.url = url
            self.request = requests.get(self.url)

    def file_size(self, size_type=None):
        # return self.conversion_size(file, size_type)
        pass

if __name__ == "__main__":
    db = DropBox("https://www.dropbox.com/s/1rrmsgk8sv6n9xs/Dropbox%20%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0.pdf?dl=0")
    # print(db.file_size('T'))
    # print(db.file_size('G'))
    # print(db.file_size('M'))
    # print(db.file_size('K'))
    # print(db.file_size('B'))
