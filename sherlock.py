import re
from actions.allmusic.discography import AllmusicDiscographyAction
from actions.allmusic.album import AllmusicAlbumAction


class Sherlock:
    """Finds appropriate action using deduction.

    Returns action method based on provided uri. Action is like a method
    of controller.
    """
    def deduct_action(self, uri):
        # TODO improve factory to scale better

        # Allmusic albums parser.
        regex_allmusic_albums = re.compile(
                '^http://www.allmusic.com/artist/.+?/discography$'
                )
        if regex_allmusic_albums.match(uri):
            return AllmusicDiscographyAction

        # Allmusic tracks parser.
        regex_allmusic_tracks = re.compile(
                '^http://www.allmusic.com/album/.+?$'
                )
        if regex_allmusic_tracks.match(uri):
            return AllmusicAlbumAction
