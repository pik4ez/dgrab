from abc import ABCMeta, abstractmethod


class AbstractParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, data):
        pass

    def normalize_whitespaces(self, s):
        return ' '.join(s.split())
