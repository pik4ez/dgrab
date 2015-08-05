from abc import ABCMeta, abstractmethod


class AbstractAction(object):
    __metaclass__ = ABCMeta


    @abstractmethod
    def run(self, data):
        pass
