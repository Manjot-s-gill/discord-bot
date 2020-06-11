from discord.ext import commands
from discord.ext.commands import Bot
import time
import os
import ClanInfo
import asyncio


client = commands.Bot(command_prefix='h')

@client.event
async def on_ready():
    print('Bot is functional')


@client.command()
async def claninfo(ctx):
    ClanInfo.clan_info()

    # Changing directory to read the claninfo file
    os.chdir("a:\Programming\Python")
    f = open('clanInfo.txt', 'r')
    data = '```'+ f.read() + '```'
    f.close()

    # Sending initial message of clan information
    message = await ctx.send(data)
    await asyncio.sleep(2)

    """Created infinite loop to keep to edit the previous sent message after certain interval! 
    Used 'await asyncio.sleep()' | so that it will not block the execution entirely and let other commands run untill it's in sleep mode."""

    while(True):
        ClanInfo.clan_info()
        
        os.chdir("a:\Programming\Python")
        f = open('clanInfo.txt', 'r')
        data = '```'+ f.read() + '```'
        f.close()
        
        await message.edit(content=data)
        print('worked')
        await asyncio.sleep(20)
        
@client.command()
async def test(ctx):
    await ctx.send("this is working")

client.run('NzE4NDQ0ODU4NTE5NTg0ODk4.Xto98Q.4gzALFZ_2zkhIbzPpiEpjzZrA4w')

