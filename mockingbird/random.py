import random

import discord
from discord.ext import commands


class Random(commands.Cog):
    """Choose random players and form random teams."""

    @staticmethod
    def get_online_members(ctx):
        channel = ctx.message.channel
        online_members = [
            member
            for member in channel.members
            if not member.bot and member.status == discord.Status.online
        ]
        return online_members

    @commands.command(
        help="Choose a random player from one of the active members of the channel.",
        brief="Choose a random player.",
    )
    async def choose(self, ctx):
        online_members = self.get_online_members(ctx)
        random_member = random.choice(online_members)
        await ctx.send(f"I choose {random_member.name}!")
