from bs4 import BeautifulSoup
from parsers.abstract_parser import AbstractParser


class AllmusicDiscographyParser(AbstractParser):
    def parse(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        result = {}
        rows = soup\
                .find('section', class_='discography')\
                .find('table')\
                .find_all('tr')
        if rows:
            result['albums'] = []
        for row in rows:
            album = {}
            try:
                # Extract title.
                title = row\
                        .find('td', class_='title')\
                        .find(
                                lambda tag: tag.name == 'a'
                                and tag.has_attr('data-tooltip')
                                )\
                        .string\
                        .strip()
                title = self.normalize_whitespaces(title)
                album['title'] = title

                # Extract year.
                album['year'] = row\
                        .find('td', class_='year')\
                        .string\
                        .strip()
                album['year'] = int(album['year'])

                result['albums'].append(album)
            except AttributeError:
                pass
        return result
