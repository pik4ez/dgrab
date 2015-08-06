#!/usr/bin/env python3

import unittest
import os
from parsers.allmusic.discography import AllmusicDiscographyParser
from parsers.allmusic.album import AllmusicAlbumParser


class AllmusicTestCase(unittest.TestCase):
    def test_get_discography(self):
        parser = AllmusicDiscographyParser()
        file_path = os.path.dirname(__file__) + \
                '/fixtures/allmusic_discography.html'
        with open(file_path, 'r') as f:
            data = f.read()
        f.close()
        result = parser.parse(data)
        expected = {'albums': [
            {'title': 'All Wound Up', 'year': 1998},
            {'title': 'Godsmack', 'year': 1998},
            {'title': 'Awake', 'year': 2000},
            {'title': 'Faceless', 'year': 2003},
            {'title': 'The Other Side', 'year': 2004},
            {'title': 'IV', 'year': 2006},
            {'title': 'The Oracle', 'year': 2010},
            {'title': 'Live & Inspired', 'year': 2012},
            {'title': '1000hp', 'year': 2014}
            ]}
        self.assertEqual(expected, result)


    def test_get_album(self):
        parser = AllmusicAlbumParser()
        file_path = os.path.dirname(__file__) + '/fixtures/allmusic_album.html'
        with open(file_path, 'r') as f:
            data = f.read()
        f.close()
        result = parser.parse(data)
        expected = {'albums': [{
                'artist': 'Godsmack',
                'title': 'All Wound Up',
                'year': 1998,
                'tracks': [
                    {'title': 'Moon Baby', 'duration': 262},
                    {'title': 'Immune', 'duration': 287},
                    {'title': 'Time Bomb', 'duration': 236},
                    {'title': 'Keep Away', 'duration': 306},
                    {'title': 'Situation', 'duration': 331},
                    {'title': 'Stress', 'duration': 302},
                    {'title': 'Bad Religion', 'duration': 219},
                    {'title': 'Get Up, Get Out!', 'duration': 330},
                    {'title': 'Now or Never', 'duration': 304},
                    {'title': "Goin' Down", 'duration': 209},
                    {'title': 'Voodoo', 'duration': 279},
                    {'title': 'Whatever', 'duration': 205}
                    ]}]}
        self.assertEqual(expected, result)


    def test_get_release_year(self):
        parser = AllmusicAlbumParser()
        result = parser.get_release_year('July 28, 1998')
        expected = 1998
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
