import json
import requests
from actions.abstract_action import AbstractAction
from parsers.allmusic.album import AllmusicAlbumParser


class AllmusicAlbumAction(AbstractAction):
    def run(self, args):
        # Get raw data by uri.
        response = requests.get(args.uri, headers={
            'User-Agent': 'Mozilla/5.0'
            })
        if response.status_code != requests.codes.ok:
            print('Failed to read uri.')
            return

        # Parse data using allmusic:album parser.
        parser = AllmusicAlbumParser()
        album = parser.parse(response.text)
        if not album:
            print('Failed to get album data by uri.')
            return

        # Convert result to json.
        album = json.dumps(album, separators=(',', ':'))

        # Print result.
        print(album)
