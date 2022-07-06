import disnake
from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="See Bot latency")
    async def Ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Client Latency: {round(self.client.latency * 1000)} ms")


def setup(client):
    client.add_cog(Ping(client))
