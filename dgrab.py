#!/usr/bin/env python3

import sys
import argparse
import json
from sherlock import Sherlock


description="Discography grabber compatible with vkalbu."
usage = "dgrab <uri>"

args_parser = argparse.ArgumentParser(
        description=description,
        usage=usage
        )
args_parser.add_argument(
        'uri',
        help='Uri of albums list or tracks list web page.'
        )
args = args_parser.parse_args()


if __name__ == '__main__':
    sherlock = Sherlock()
    action = sherlock.deduct_action(args.uri)
    if action is None:
        sys.exit('Unsupported service.')
    action().run(args)
