import random

import disnake
from disnake.ext import commands


class Toss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="Toss the coin!")
    @commands.guild_only()
    async def toss(self, inter: disnake.ApplicationCommandInteraction,
                   choice: str = commands.Param(choices=["Heads", "Tails"],
                                                description="Choose your choice Heads or Tails")):
        toss_embed = disnake.Embed(colour=inter.author.color.gold())
        a = "Heads" if (random.random()) else "Tails"
        if choice == a:
            toss_embed.add_field(name=a,value=f"{inter.author.display_name.capitalize()} Won!")
        else:
            toss_embed.add_field(name=a, value=f"{inter.author.display_name.capitalize()} Lose!")
        toss_embed.set_footer(icon_url=inter.author.avatar.url, text=f"Tossed by: {inter.author.display_name}")
        await inter.response.send_message(embed=toss_embed)


def setup(client):
    client.add_cog(Toss(client))
