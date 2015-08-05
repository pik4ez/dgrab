#!/usr/bin/env python3

import unittest
from sherlock import Sherlock
from actions.allmusic.discography import AllmusicDiscographyAction
from actions.allmusic.album import AllmusicAlbumAction

class SherlockTestCase(unittest.TestCase):
    def test_allmusic_discography(self):
        s = Sherlock()
        result = s.deduct_action(
                'http://www.allmusic.com' + \
                        '/artist/godsmack-mn0000665860/discography'
                )
        expected = AllmusicDiscographyAction
        self.assertEqual(result, expected)


    def test_allmusic_album(self):
        s = Sherlock()
        result = s.deduct_action(
                'http://www.allmusic.com/album/all-wound-up-mw0001888339'
                )
        expected = AllmusicAlbumAction
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
