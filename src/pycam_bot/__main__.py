"""Main module of pycam_bot"""

# std import
import argparse
import configparser
import logging
import pathlib
import sys

# 3rd party import
from obswebsocket import obsws

# project import
from . import bot


logger = logging.getLogger(__name__)


def main(args=None) -> int:
    """Main function of pycam_bot"""

    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="PyCam_Bot")

    parser.add_argument("-c", "--config", type=pathlib.Path, help="Configuration file")
    parser.add_argument("-v", "--verbose", action="count", default=0)

    args = parser.parse_args()

    print(args.verbose)
    # Setup logging
    match args.verbose:
        case 0:
            log_level = logging.NOTSET
        case 1:
            log_level = logging.CRITICAL
        case 2:
            log_level = logging.ERROR
        case 3:
            log_level = logging.WARNING
        case 4:
            log_level = logging.INFO
        case _:
            log_level = logging.DEBUG



    logging.basicConfig(format="%(levelname)s: %(message)s", level=log_level)

    # Read configuration
    logger.info("Parse configuration")
    config = configparser.ConfigParser()
    config.read(args.config)

    # Start connexion with obs
    logger.info("Connect to obs")
    ws: obsws = obsws(config["obs"]["host"], config["obs"]["port"], config["obs"]["secret"])
    ws.connect()

    # Start bot
    logger.info("Init bot")
    cam_bot = bot.Bot(config["twitch"]["access_token"], )
    logger.info("Run bot")
    cam_bot.run()

    ws.disconnect()

    return 0


sys.exit(main())
