import os
import sys
from downloaders.abstract_downloader import AbstractDownloader


class FileDownloader(AbstractDownloader):
    def download(self, uri):
        with open(os.path.expanduser(uri), 'r') as f:
            return f.read()
