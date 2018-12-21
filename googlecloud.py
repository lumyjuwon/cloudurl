from cloud import Cloud
from bs4 import BeautifulSoup
from exceptions import *
import requests
import re


class GoogleCloud(Cloud):

    def confirm_url(self, url):
        try:
            regex = re.compile("\w+")
            url_regex_list = regex.findall(url)
            if "download" in url_regex_list:
                return
            elif "view" in url_regex_list:
                self.view_to_download(url)
            elif "edit" in url_regex_list:
                self.view_to_download(url)
        except Exception:
            raise NotGoogleDriveUrl(self.url)

        html = str(self.get_html())
        if html.find("Not Found") != -1:
            raise NotFoundGoogleDriveUrl(self.url)

    def view_to_download(self, url):
        regex = re.compile("d/(.+)/")
        url_code = regex.findall(url)[0]
        self.url = "https://drive.google.com/uc?id=" + url_code + "&export=download"
        self.request = requests.get(self.url)

    def file_size(self, size_type=None):
        crawled_file = self.get_html().find_all('span', {'class': 'uc-name-size'})[0].find_all(text=True)[1].strip()[1:-1]
        file = {'size': crawled_file[0:-1], 'unit': crawled_file[-1]}
        return self.conversion_size(file, size_type)

    def direct_link(self):
        print("A")


if "__main__" == __name__:
    google = GoogleCloud("https://drive.google.com/file/d/1tn3KmCykFqw-qG6Nb55EBRlAJYFzL1kN/view")
    # print(google.file_size('S'))
    print(google.file_size('G'))
    # print(google.file_size('M'))
    # print(google.file_size('K'))
    # print(google.file_size('B'))
