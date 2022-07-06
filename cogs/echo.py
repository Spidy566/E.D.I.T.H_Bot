import disnake
from disnake.ext import commands


class Echo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="Echo the commands given")
    async def echo(self, inter: disnake.ApplicationCommandInteraction, word: str, number: int):
        await inter.response.send_message(word * number)


def setup(client):
    client.add_cog(Echo(client))
