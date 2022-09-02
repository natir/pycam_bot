"""Manage all routines"""

# std import

# 3rd party import
from twitchio.ext import routines

# project import


def run(messageable):
    """Run all available routines"""
    sub.start(messageable)


@routines.routine(minutes=15, iterations=1)
async def sub(messageable):
    messageable.send("Ne subbez pas ici mais plus tôt chez: foutu_pour_foutu")
