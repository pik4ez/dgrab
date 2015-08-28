#!/usr/bin/env python3

import unittest
import os
from parsers.discogs.discography import DiscogsDiscographyParser
from parsers.discogs.album import DiscogsAlbumParser


class DiscogsTestCase(unittest.TestCase):
    def test_get_album(self):
        parser = DiscogsAlbumParser()
        file_path = os.path.dirname(__file__) + '/fixtures/discogs_album.html'
        with open(file_path, 'r') as f:
            data = f.read()
        f.close()
        result = parser.parse(data)
        expected = {'albums': [{
                'artist': 'Pantera',
                'title': 'Power Metal',
                'year': 1988,
                'tracks': [
                    {'title': 'Rock The World', 'duration': 210},
                    {'title': 'Power Metal', 'duration': 235},
                    {'title': 'We\'ll Meet Again', 'duration': 230},
                    {'title': 'Over And Out', 'duration': 315},
                    {'title': 'Proud To Be Loud', 'duration': 240},
                    {'title': 'Down Below', 'duration': 160},
                    {'title': 'Death Trap', 'duration': 240},
                    {'title': 'Hard Ride', 'duration': 255},
                    {'title': 'Burnnn!', 'duration': 225},
                    {'title': 'P*S*T* 88', 'duration': 168}
                    ]}]}
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
