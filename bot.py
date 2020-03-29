import random

import discord

from mockingbird.settings import BOT_TOKEN


client = discord.Client()


@client.event
async def on_message(message):
    # Skip over messages sent from Mockingbird itself and messages that do not start with !mb
    if message.author == client.user or not message.content.startswith("!mb choose"):
        return

    channel = message.channel
    online_members = [
        member
        for member in channel.members
        if not member.bot and member.status == discord.Status.online
    ]
    random_member = random.choice(online_members)
    await channel.send(f"I choose {random_member.name}!")


client.run(BOT_TOKEN)
