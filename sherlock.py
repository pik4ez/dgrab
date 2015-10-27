import re
from downloaders.http import HttpDownloader
from downloaders.file import FileDownloader
from parsers.allmusic.album import AllmusicAlbumParser
from parsers.discogs.album import DiscogsAlbumParser


class Sherlock:
    def deduct(self, uri):
        """Finds appropriate action using deduction.

        Returns action method based on provided uri. Action is like a method
        of controller.
        """
        # Allmusic album parser, http downloader.
        regex_allmusic_album = re.compile(
                '^http://www.allmusic.com/album/.+?$'
                )
        if regex_allmusic_album.match(uri):
            return (HttpDownloader, AllmusicAlbumParser, uri)

        # Allmusic album parser, file downloader.
        regex_allmusic_album = re.compile(
                '^file:allmusic:.+?$'
                )
        if regex_allmusic_album.match(uri):
            return (
                FileDownloader,
                AllmusicAlbumParser,
                self.clean_file_uri(uri)
                )

        # Discogs album parser, http downloader.
        regex_discogs_album = re.compile(
                '^http://www.discogs.com/.+?/(master|release)/\d+$'
                )
        if regex_discogs_album.match(uri):
            return (HttpDownloader, DiscogsAlbumParser, uri)

        # Discogs album parser, file downloader.
        regex_discogs_album = re.compile(
                '^file:discogs:.+?$'
                )
        if regex_discogs_album.match(uri):
            return (
                FileDownloader,
                DiscogsAlbumParser,
                self.clean_file_uri(uri)
                )

        # Neither parser nor downloader found.
        return (None, None)

    def clean_file_uri(self, uri):
        """Removes all routing prefixes from file URI."""
        if not uri.startswith('file:'):
            return None
        return self.remove_source_prefix(uri[5:])

    def remove_source_prefix(self, uri):
        """Removes routing source prefix from URI."""
        sources = ['allmusic', 'discogs']
        for source in sources:
            if uri.startswith("%s:" % source):
                return uri[(len(source) + 1):]
        return None
