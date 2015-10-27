#!/usr/bin/env python3

import sys
import argparse
import json
from sherlock import Sherlock


description = "Discography grabber compatible with vkalbu."
usage = "dgrab <uri>"

args_parser = argparse.ArgumentParser(
        description=description,
        usage=usage
        )
args_parser.add_argument(
        'uri',
        help=(
            'Uri or file path of album web page. Examples:'
            'http://allmusic.com/some_artist/some_album.html'
            'http://discogs.com/another_artist/another_album.html'
            'file:allmusic:/path/to/some_album.html'
            'file:discogs:/path/to/another_album.html'
            )
        )
args = args_parser.parse_args()


if __name__ == '__main__':
    # Determine downloader and parser.
    sherlock = Sherlock()
    (downloader, parser, clean_uri) = sherlock.deduct(args.uri)
    if downloader is None:
        sys.exit((
            'Failed to find appropriate downloader.\n'
            'Read help to get list of supported URIs.'
            ))
    if parser is None:
        sys.exit((
            'Failed to find appropriate parser.\n'
            'Read help to get list of supported URIs.'
            ))

    # Fetch raw data by uri.
    raw_data = downloader().download(clean_uri)
    if (raw_data is None):
        sys.exit('Failed to get data from %s.' % (args.uri))

    # Parse data.
    album = parser().parse(raw_data)
    if not album:
        sys.exit('Failed to get album data from %s.' % (args.uri))

    # Convert result to json.
    album = json.dumps(album, separators=(',', ':'))

    # Print result.
    print(album)
