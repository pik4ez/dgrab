import re
from bs4 import BeautifulSoup
from parsers.abstract_parser import AbstractParser


class DiscogsAlbumParser(AbstractParser):
    def parse(self, data):
        album = {}
        soup = BeautifulSoup(data, 'html.parser')

        # Extract artist, title and year.
        album['artist'] = soup\
            .find('h1')\
            .span\
            .a\
            .string
        album['artist'] = self.normalize_whitespaces(album['artist'])
        album['title'] = soup\
            .find('h1')\
            .find_all('span')[2]\
            .string
        album['title'] = self.normalize_whitespaces(album['title'])
        album['year'] = self.get_year(soup)

        # Extract tracks.
        rows = soup\
            .find('div', id='tracklist')\
            .find_all('tr', class_='tracklist_track')
        if rows:
            album['tracks'] = []
        for row in rows:
            track = {}

            # Extract track title.
            title = row\
                .find('td', class_='tracklist_track_title')\
                .find('span', class_='tracklist_track_title')\
                .string
            title = self.normalize_whitespaces(title)
            track['title'] = title

            # Extract track duration.
            # Switch format from "X:XX" string to number of seconds.
            duration = row\
                .find('td', class_='tracklist_track_duration')\
                .span\
                .string
            duration = duration.string.strip().rsplit(':')
            duration = int(duration[0]) * 60 + int(duration[1])
            track['duration'] = duration

            album['tracks'].append(track)

        return {'albums': [album]}

    def get_year(self, soup):
        year = self.get_year_year(soup)
        if not year:
            year = self.get_year_released(soup)
        if not year:
            return None
        # Extract four digits from string.
        return [int(s) for s in year.split() if s.isdigit() and len(s) == 4][0]

    def get_year_year(self, soup):
        """Tries to extract year from 'Year:' block"""
        try:
            year = soup\
                .find('div', class_='profile')\
                .find(text='Year:')\
                .parent\
                .find_next('div', class_='content')\
                .a\
                .string\
                .strip()
            return year
        except AttributeError:
            pass

    def get_year_released(self, soup):
        """Tries to extract year from 'Released:' block"""
        try:
            year = soup\
                .find('div', class_='profile')\
                .find(text='Released:')\
                .parent\
                .find_next('div', class_='content')\
                .a\
                .string\
                .strip()
            return year
        except AttributeError:
            pass
