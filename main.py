import discord
import datetime
import random


from discord.ext import commands
from random import choice
from discord import Color as c

BotName = 'YourBotName'
BotStatus = 'YourBotStatus'
BotPrefix = 'YourBotPrefix'


bot = commands.Bot(command_prefix = f'{BotPrefix}'

@bot.event()
async def on_ready():
                   
   await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{BotStatus}|| TechnicalError"))                
                   
   print('✅ Help Command Loaded')
   print('✅ Kick Command Loaded')               
   print('✅ Ban Command Loaded')               
   print('✅ Mute Command Loaded')
   print('✅ Unmute Command Loaded')
   print('✅ Poll Command Loaded')
   print('✅ Ping Command Loaded')
   print('✅ Guess Command Loaded')
   print('✅ Bot Status Updated')             
   Print('Bot Launched')
   print('Bot is ONLINE')
   print('Coded By TECHNICALERROR')
                   
                
                   
@bot.group(invoke_without_command=True)
async def help(ctx, member: discord.Member = None):
	member = ctx.author if not member else member
	members = ctx.message.author.name
  embed = discord.Embed(color = Color.red)
  embed.add_field(name = 'Help', value = f'> Help Command for this bot.\n > Prefix = {BotPrefix})
     
                  
