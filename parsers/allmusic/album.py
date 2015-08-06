from bs4 import BeautifulSoup
from parsers.abstract_parser import AbstractParser


class AllmusicAlbumParser(AbstractParser):
    def parse(self, data):
        album = {}
        soup = BeautifulSoup(data, 'html.parser')

        # Extract artist, title and year.
        album['artist'] = soup\
                .find('h3', id='album-artist-link')\
                .find('a')\
                .string
        album['artist'] = self.normalize_whitespaces(album['artist'])
        album['title'] = soup\
                .find('h2', class_='album-title')\
                .string
        album['title'] = self.normalize_whitespaces(album['title'])
        album['year'] = soup\
                .find('div', class_='release-date')\
                .find('span')\
                .string\
                .strip()
        album['year'] = self.get_release_year(album['year'])

        # Extract tracks.
        rows = soup.find_all('tr', class_='track')
        if rows:
            album['tracks'] = []
        for row in rows:
            track = {}

            # Extract track title.
            title = row\
                    .find('td', class_='title-composer')\
                    .find('div', class_='title')\
                    .a\
                    .string
            title = self.normalize_whitespaces(title)
            track['title'] = title

            # Extract track duration.
            # Switch format from "X:XX" string to number of seconds.
            duration = row.find('td', class_='time')
            duration.find('meta').decompose()
            duration = duration.string.strip().rsplit(':')
            duration = int(duration[0]) * 60 + int(duration[1])
            track['duration'] = duration

            album['tracks'].append(track)

        return {'albums': [album]}


    """Returns year from release date in allmusic format.
    
    Allmusic release date format: July 28, 1998.
    """
    def get_release_year(self, release_date):
        s = release_date.split(',')
        if not s[1]:
            return None
        return int(s[1].strip())
