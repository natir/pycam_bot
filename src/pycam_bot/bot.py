"""The bot it's self"""
# std import
import logging

# 3rd party import
from twitchio.ext import commands  # , sounds

# project import


logger = logging.getLogger(__name__)


class Bot(commands.Bot):
    def __init__(self, access_token: str):
        super().__init__(token=access_token, prefix="!", initial_channels=["cam_doc"])

        # self.music_player = sounds.AudioPlayer(callback=self.music_done)
        # self.event_player = sounds.AudioPlayer(callback=self.sound_done)

    async def event_ready(self):
        logger.info(f"Logged in as | {self.nick}")
        logger.info(f"User id is | {self.user_id}")

    async def music_done(self):
        logger.info("Finished playing song!")

    async def sound_done(self):
        logger.info("Finished playing sound!")

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.channel)
    @commands.command(aliases=("commands", "command"))
    async def help(self, ctx: commands.Context):
        await ctx.send(
            f"Liste des commandes disponible: {','.join(self.commands.keys())}"
        )

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.channel)
    @commands.command()
    async def twitter(self, ctx: commands.Context):
        await ctx.send("Retrouvé cam_doc sur twitter: https://twitter.com/CamaradeDr/")

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.channel)
    @commands.command()
    async def instagram(self, ctx: commands.Context):
        await ctx.send(
            "Retrouvé cam_doc sur instagram: https://www.instagram.com/camarade_docteur/"
        )

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.channel)
    @commands.command(aliases=("chroniques", "soundcloud"))
    async def chronique(self, ctx: commands.Context):
        await ctx.send(
            "Retrouvé les chronique de cam_doc sur soundcloud: https://soundcloud.com/pierre-marijon"
        )

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.channel)
    @commands.command()
    async def so(self, ctx: commands.Context, *, message: str):
        await ctx.send(
            f"Allez suivre {message} sur twitch.tv/{message} c'est fantastique, le follow est doux."
        )

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.channel)
    @commands.command()
    async def bonk(self, ctx: commands.Context):
        await ctx.send(f"{ctx.author.name} ici on est contre toutes les prisons")

    # @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.channel)
    # @commands.command()
    # async def sel(self, ctx: commands.Context, *, message: str):
    #     sound = sounds.Sound(source='sel.mp3')
    #     self.event_player.play(sound)
