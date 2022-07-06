import disnake
from disnake.ext import commands
from EnvVariables import TOKEN, GUILD

client = commands.Bot(intents=disnake.Intents.all(), command_prefix="!", test_guilds=[GUILD])


@client.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("Updates are coming soon!!!")


client.load_extensions("./cogs")

client.run(TOKEN)
