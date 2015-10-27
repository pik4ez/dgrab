from abc import ABCMeta, abstractmethod


class AbstractDownloader(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def download(self, uri):
        pass
