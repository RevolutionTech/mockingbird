from discord.ext.commands import Bot

from mockingbird.random import Random
from mockingbird.settings import BOT_TOKEN, BOT_COMMAND_PREFIX, BOT_DESCRIPTION

bot = Bot(command_prefix=BOT_COMMAND_PREFIX, description=BOT_DESCRIPTION)


if __name__ == "__main__":
    bot.add_cog(Random())
    bot.run(BOT_TOKEN)
