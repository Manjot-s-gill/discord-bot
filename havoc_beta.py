from discord.ext import commands
from discord.ext.commands import Bot
import time
import os
import ClanInfo  # Self-made library used to write requested JSON data to 'clanInfo.txt' file.
import asyncio


client = commands.Bot(command_prefix='h')

@client.event
async def on_ready():
    print('Bot is functional')


@client.command()
async def claninfo(ctx):
    ClanInfo.clan_info()          # Self-made library used to write requested JSON data to 'clanInfo.txt' file.

    # Changing directory to read the claninfo file
    os.chdir("a:\Programming\Python")
    f = open('clanInfo.txt', 'r')
    data = '```'+ f.read() + '```'
    f.close()

    # Sending initial message of clan information
    message = await ctx.send(data)
    await asyncio.sleep(2)

    """Created infinite loop to keep editing the previous sent message after certain interval! 
    Used 'await asyncio.sleep()' | so that it will not block the execution entirely and let other commands run untill it's in sleep mode."""

    while(True):
        ClanInfo.clan_info()
        
        os.chdir("a:\Programming\Python")
        f = open('clanInfo.txt', 'r')
        data = '```'+ f.read() + '```'
        f.close()
        
        await message.edit(content=data)
        await asyncio.sleep(20)
        
@client.command()
async def test(ctx):
    await ctx.send("this is working")

client.run('Your Discord App token')

