import json
import urllib.request
from actions.abstract_action import AbstractAction
from parsers.allmusic.album import AllmusicAlbumParser


class AllmusicAlbumAction(AbstractAction):
    def run(self, args):
        # Get raw data by uri.
        req = urllib.request.Request(args.uri, headers={
            'User-Agent': 'Mozilla/5.0'
            })
        data = urllib.request.urlopen(req).read()
        if not data:
            print('Failed to read uri.')
            return

        # Parse data using allmusic:album parser.
        parser = AllmusicAlbumParser()
        album = parser.parse(data)
        if not album:
            print('Failed to get album data by uri.')
            return

        # Convert result to json.
        album = json.dumps(album, separators=(',', ':'))

        # Print result.
        print(album)
