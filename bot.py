import discord
from discord.ext.commands import Bot

from mockingbird.decrypto import Decrypto
from mockingbird.random import Random
from mockingbird.settings import BOT_COMMAND_PREFIX, BOT_DESCRIPTION, BOT_TOKEN

intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = Bot(command_prefix=BOT_COMMAND_PREFIX, description=BOT_DESCRIPTION, intents=intents)


if __name__ == "__main__":
    bot.add_cog(Random())
    bot.add_cog(Decrypto())
    bot.run(BOT_TOKEN)
