import discord

from discord.ext import commands

BotPrefix = "URBotPrefix"
Token = "your bot token"

bot = commands.Bot(command_prefix = BotPrefix)

@bot.event
async def on_ready():
    await print(f"{bot.user} is online")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!)
		   
bot.run(token)
