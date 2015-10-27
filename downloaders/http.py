import sys
import requests
from downloaders.abstract_downloader import AbstractDownloader


class HttpDownloader(AbstractDownloader):
    def download(self, uri):
        """Gets raw data by uri."""
        response = requests.get(uri, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:30.0)\
                    Gecko/20100101 Firefox/30.0'
            })
        if response.status_code != requests.codes.ok:
            print('Failed to read uri.')
            return
        return response.text
