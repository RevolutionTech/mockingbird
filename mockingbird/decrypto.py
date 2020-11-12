import random

from discord.ext import commands


class Decrypto(commands.Cog):
    """Generate random messages for the game Decrypto."""

    MESSAGE_ALPHABET = ["1", "2", "3", "4"]
    MESSAGE_LENGTH = 3

    @commands.command(help="Generate a random message for the game Decrypto.", brief="Generate message for Decrypto.")
    async def message(self, ctx):
        message_characters = random.sample(self.MESSAGE_ALPHABET, self.MESSAGE_LENGTH)
        message_text = ", ".join(message_characters)
        await ctx.author.send(message_text)
