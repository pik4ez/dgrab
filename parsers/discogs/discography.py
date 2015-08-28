from bs4 import BeautifulSoup
from parsers.abstract_parser import AbstractParser


class DiscogsDiscographyParser(AbstractParser):
    def parse(self, data):
        raise Exception('not implemented')
