import random

import discord
from discord.ext import commands


class Random(commands.Cog):
    """Choose random players and form random teams."""

    @staticmethod
    def random_partition(lst, num_partitions):
        division = len(lst) / num_partitions
        random.shuffle(lst)
        return [
            lst[round(division * i) : round(division * (i + 1))]
            for i in range(num_partitions)
        ]

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
        if online_members:
            random_member = random.choice(online_members)
            await ctx.send(f"I choose {random_member.name}!")
        else:
            await ctx.send(
                "I don't understand how this could be possible, but no one is online..."
            )

    @commands.command(
        help="Divide the active members of the channel into teams.",
        brief="Choose random teams.",
    )
    async def teams(self, ctx, num_teams=2):
        online_members = self.get_online_members(ctx)
        if len(online_members) >= num_teams:
            random_teams = self.random_partition(online_members, num_teams)
            teams_str = "\n".join(
                [
                    f"Team {i}: {', '.join([member.name for member in team])}"
                    for i, team in enumerate(random_teams, 1)
                ]
            )
            await ctx.send(f"Okay, here are the teams:\n\n{teams_str}")
        else:
            await ctx.send(
                "Unfortunately there aren't enough members online to form teams."
            )
