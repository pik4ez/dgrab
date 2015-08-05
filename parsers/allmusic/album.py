from bs4 import BeautifulSoup
from parsers.abstract_parser import AbstractParser


class AllmusicAlbumParser(AbstractParser):
    # FIXME add album information: artist, title, year
    def parse(self, data):
        result = {}
        soup = BeautifulSoup(data, 'html.parser')
        rows = soup.find_all('tr', class_='track')
        if rows:
            result['tracks'] = []
        for row in rows:
            track = {}

            # Extract title.
            title = row\
                    .find('td', class_='title-composer')\
                    .find('div', class_='title')\
                    .a\
                    .string
            title = self.normalize_whitespaces(title)
            track['title'] = title

            # Extract duration.
            # Switch format from "X:XX" string to number of seconds.
            duration = row.find('td', class_='time')
            duration.find('meta').decompose()
            duration = duration.string.strip().rsplit(':')
            duration = int(duration[0]) * 60 + int(duration[1])
            track['duration'] = duration

            result['tracks'].append(track)
        return result
