import argparse

from utils.config import config


def cli_opt():
    parser = argparse.ArgumentParser(description=f"Batch testing stream media unlock status. "
                                                 f"StairUnlocker v{config['VERSION']}")
    parser.add_argument("-u", "--url",
                        action="store",
                        dest="subURL",
                        default="",
                        help="Load config from subscription url"
                        )
    parser.add_argument("-t", "--token",
                        action="store",
                        dest="token",
                        default="",
                        help="The github token"
                        )
    parser.add_argument("-g", "--gist",
                        action="store",
                        dest="gistURL",
                        default="",
                        help="The gist api URL"
                        )
    args = parser.parse_args()
    if args.subURL:
        config['subURL'] = args.subURL
    if args.token:
        config['token'] = args.token
        config['localFile'] = False
    if args.gistURL:
        config['gistURL'] = args.gistURL
