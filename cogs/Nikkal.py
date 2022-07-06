import disnake
from disnake.ext import commands


class Nikkal(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="Most Popular Game in Schools")
    async def nikkal(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Kunthal!")


def setup(client):
    client.add_cog(Nikkal(client))
