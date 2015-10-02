import json
import requests
from actions.abstract_action import AbstractAction
from parsers.discogs.album import DiscogsAlbumParser


class DiscogsAlbumAction(AbstractAction):
    def run(self, args):
        # Get raw data by uri.
        response = requests.get(args.uri, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:30.0)\
                    Gecko/20100101 Firefox/30.0'
            })
        if response.status_code != requests.codes.ok:
            print('Failed to read uri.')
            return

        # Parse data using discogs:album parser.
        parser = DiscogsAlbumParser()
        album = parser.parse(response.text)
        if not album:
            print('Failed to get album data by uri.')
            return

        # Convert result to json.
        album = json.dumps(album, separators=(',', ':'))

        # Print result.
        print(album)
