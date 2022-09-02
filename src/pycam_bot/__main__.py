"""Main module of pycam_bot"""

# std import
import argparse
import configparser
import logging
import pathlib
import sys

# project import
#from . import bot, routines
from . import bot

# 3rd party import


logger = logging.getLogger(__name__)


def main(args=None) -> int:
    """Main function of pycam_bot"""

    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="PyCam_Bot")

    parser.add_argument("-c", "--config", type=pathlib.Path, help="Configuration file")
    parser.add_argument("-v", "--verbose", action="count", default=0)

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(format="%(levelname)s: %(message)s", level=args.verbose * 10)

    # Read configuration
    logger.info("Parse configuration")
    config = configparser.ConfigParser()
    config.read(args.config)

    # Start bot
    logger.info("Init bot")
    cam_bot = bot.Bot(config["DEFAULT"]["access_token"])
    logger.info("Run bot")
    cam_bot.run()

    return 0


sys.exit(main())
