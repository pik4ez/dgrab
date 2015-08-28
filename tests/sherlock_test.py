#!/usr/bin/env python3

import unittest
from sherlock import Sherlock
from actions.allmusic.discography import AllmusicDiscographyAction
from actions.allmusic.album import AllmusicAlbumAction
from actions.discogs.discography import DiscogsDiscographyAction
from actions.discogs.album import DiscogsAlbumAction

class SherlockTestCase(unittest.TestCase):
    def test_allmusic_discography(self):
        s = Sherlock()
        expected = AllmusicDiscographyAction
        result = s.deduct_action(
                'http://www.allmusic.com' + \
                        '/artist/godsmack-mn0000665860/discography'
                )
        self.assertEqual(expected, result)


    def test_allmusic_album(self):
        s = Sherlock()
        expected = AllmusicAlbumAction
        result = s.deduct_action(
                'http://www.allmusic.com/album/all-wound-up-mw0001888339'
                )
        self.assertEqual(expected, result)


    def test_discogs_discography(self):
        s = Sherlock()
        expected = DiscogsDiscographyAction
        result = s.deduct_action(
                'http://www.discogs.com/artist/85885-Pantera'
                )
        self.assertEqual(expected, result)


    def test_discogs_album(self):
        s = Sherlock()
        expected = DiscogsAlbumAction
        result = s.deduct_action(
                'http://www.discogs.com/Pantera-Power-Metal/master/244264'
                )
        self.assertEqual(expected, result)
        result = s.deduct_action(
                'http://www.discogs.com/Pantera-Psycho-Holiday/release/3139636'
                )
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
