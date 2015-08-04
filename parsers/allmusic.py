from bs4 import BeautifulSoup


class Allmusic():
    def parse_albums_list(self, file_path):
        # FIXME implement
        pass


    def parse_album(self, file_path):
        album = {}
        with open(file_path) as f:
            soup = BeautifulSoup(f, 'html.parser')
            rows = soup.find_all('tr', class_='track')
            album['tracks'] = []

            for row in rows:
                track = {}

                # Extract title.
                track['title'] = row\
                        .find('td', class_='title-composer')\
                        .find('div', class_='title')\
                        .a\
                        .string\
                        .strip()

                # Extract duration.
                # Switch format from "X:XX" string to number of seconds.
                duration = row.find('td', class_='time')
                duration.find('meta').decompose()
                duration = duration.string.strip().rsplit(':')
                duration = int(duration[0]) * 60 + int(duration[1])
                track['duration'] = duration

                album['tracks'].append(track)

        return album
