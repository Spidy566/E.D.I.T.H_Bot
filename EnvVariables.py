import json

with open("./data/config.json", "r") as c:
    config = json.load(c)
    c.close()

TOKEN = config["DISCORD_TOKEN"]
GUILD = 955012625475960843
