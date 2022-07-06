import disnake
from disnake.ext import commands


class Whois(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="Check who is ->")
    @commands.guild_only()
    async def whois(self, inter: disnake.ApplicationCommandInteraction,
                    user: disnake.User = commands.Param(description="Mention a User")):
        whois_embed = disnake.Embed(title=user.name, description=user.mention, colour=user.colour.green())
        whois_embed.add_field(name="ID", value=user.id, inline=True)
        whois_embed.set_thumbnail(url=user.avatar.url)
        whois_embed.set_footer(icon_url=inter.author.avatar.url, text=f"Requested by: {inter.author.display_name}")
        await inter.response.send_message(embed=whois_embed)


def setup(client):
    client.add_cog(Whois(client))
