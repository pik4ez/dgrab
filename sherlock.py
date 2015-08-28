import re
from actions.allmusic.discography import AllmusicDiscographyAction
from actions.allmusic.album import AllmusicAlbumAction
from actions.discogs.discography import DiscogsDiscographyAction
from actions.discogs.album import DiscogsAlbumAction


class Sherlock:
    """Finds appropriate action using deduction.

    Returns action method based on provided uri. Action is like a method
    of controller.
    """
    def deduct_action(self, uri):
        # TODO improve factory to scale better

        # Allmusic discography parser.
        regex_allmusic_discography = re.compile(
                '^http://www.allmusic.com/artist/.+?/discography$'
                )
        if regex_allmusic_discography.match(uri):
            return AllmusicDiscographyAction

        # Allmusic album parser.
        regex_allmusic_album = re.compile(
                '^http://www.allmusic.com/album/.+?$'
                )
        if regex_allmusic_album.match(uri):
            return AllmusicAlbumAction

        # Discogs discography parser.
        regex_discogs_discography = re.compile(
                '^http://www.discogs.com/artist/.+$'
                )
        if regex_discogs_discography.match(uri):
            return DiscogsDiscographyAction

        # Discogs album parser.
        regex_discogs_album = re.compile(
                '^http://www.discogs.com/.+?/(master|release)/\d+$'
                )
        if regex_discogs_album.match(uri):
            return DiscogsAlbumAction
