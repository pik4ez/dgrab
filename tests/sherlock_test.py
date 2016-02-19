#!/usr/bin/env python3

import unittest
from sherlock import Sherlock
from downloaders.http import HttpDownloader
from downloaders.file import FileDownloader
from parsers.allmusic.album import AllmusicAlbumParser
from parsers.discogs.album import DiscogsAlbumParser


class SherlockTestCase(unittest.TestCase):
    def test_unknown(self):
        s = Sherlock()
        result = s.deduct('dontdnowdahellzthat')
        self.assertEqual((None, None), result)

    def test_allmusic(self):
        s = Sherlock()

        # Http. URI doesn't need normalization.
        result = s.deduct(
            'http://www.allmusic.com/album/all-wound-up-mw0001888339'
            )
        self.assertEqual(
            (
                HttpDownloader,
                AllmusicAlbumParser,
                'http://www.allmusic.com/album/all-wound-up-mw0001888339'
                ),
            result
            )

        # File. Uri should be normalized.
        result = s.deduct(
            'file:allmusic:/path/to/allmusic_album.html'
            )
        self.assertEqual(
            (
                FileDownloader,
                AllmusicAlbumParser,
                '/path/to/allmusic_album.html'
                ),
            result
            )

    def test_discogs(self):
        s = Sherlock()

        # Http. URI doesn't need normalization.
        result = s.deduct(
            'http://www.discogs.com/Pantera-Power-Metal/master/244264'
            )
        self.assertEqual(
            (
                HttpDownloader,
                DiscogsAlbumParser,
                'http://www.discogs.com/Pantera-Power-Metal/master/244264'
                ),
            result
            )
        result = s.deduct(
            'http://www.discogs.com/Pantera-Psycho-Holiday/release/3139636'
            )
        self.assertEqual(
            (
                HttpDownloader,
                DiscogsAlbumParser,
                'http://www.discogs.com/Pantera-Psycho-Holiday/release/3139636'
                ),
            result
            )

        # Https.
        result = s.deduct(
            'https://www.discogs.com/Nirvana-Nevermind/master/13814'
            )
        self.assertEqual(
            (
                HttpDownloader,
                DiscogsAlbumParser,
                'https://www.discogs.com/Nirvana-Nevermind/master/13814'
                ),
            result
            )

        # File. Uri should be normalized.
        result = s.deduct(
            'file:discogs:/path/to/discogs_album.html'
            )
        self.assertEqual(
            (
                FileDownloader,
                DiscogsAlbumParser,
                '/path/to/discogs_album.html'
                ),
            result
            )

    def test_clean_file_uri(self):
        s = Sherlock()

        # Known type and source, requires uri filtering.
        self.assertEqual(
            s.clean_file_uri('file:allmusic:/path/to/file.html'),
            '/path/to/file.html'
            )
        # Known type and source, no uri filtering required.
        self.assertEqual(
            s.clean_file_uri('http://allmusic.com/artist/album.html'),
            None
            )

        # Unknown type, known source.
        self.assertEqual(
            s.clean_file_uri('kyle:allmusic:/path/to/file.html'),
            None
            )

        # Known type, unknown source.
        self.assertEqual(
            s.clean_file_uri('file:abuzick:/path/to/file.html'),
            None
            )

        # Unknown type, unknown source.
        self.assertEqual(
            s.clean_file_uri('kyle:abuzick:/path/to/file.html'),
            None
            )

if __name__ == '__main__':
    unittest.main()
