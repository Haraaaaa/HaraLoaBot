import discord
import math
import sympy
import numpy
from discord.ext import commands
#import all of the cogs
#from main_cog import main_cog

#register the class with the bot
#from image_cog import image_cog
from music_cog import music_cog
#from bus_cog import bus_cog



bot = commands.Bot(command_prefix='!')

bot.remove_command('help')


#bot.add_cog(main_cog(bot))
#bot.add_cog(bus_cog(bot))
bot.add_cog(music_cog(bot))

@bot.command(name="버스비")
async def 버스비(ctx, a:int):
    b = a * 0.95
    
    c = math.floor(b / 1.95)
    d = math.floor(b / 2.95)
    e = math.floor(b / 3.95)

    embed=discord.Embed(title="버스비 계산기", color=0x00ff56)
    embed.add_field(name="[2인 분배금]", value=c, inline=True)
    embed.add_field(name="[3인 분배금]", value=d, inline=True)
    embed.add_field(name="[4인 분배금]", value=e, inline=True)

    await ctx.send(embed=embed)

@bot.command(name="경매")
async def 경매(ctx, a:int):
    b = a * 0.95
    
    c = math.floor(b / 4)
    d = math.floor(b / 8)

    e = c * 3
    f = d * 7


    embed=discord.Embed(title="경매 입찰금", color=0x00ff56)
    embed.add_field(name="4인 적정 입찰가", value=e, inline=True)
    embed.add_field(name="8인 적정 입찰가", value=f, inline=True)

    await ctx.send(embed=embed)



#async def echo(ctx, *args):
#    m_args = " ".join(args)
#    await ctx.send(m_args)

token = ""
with open("token.txt") as file:
    token = file.read()
bot.run(token)

#import os

#import all of the cogs
#from main_cog import main_cog
#from image_cog import image_cog
#from music_cog import music_cog

#bot = commands.bot(command_prefix='/')

#remove the default help command so that we can write out own
#bot.remove_command('help')

#register the class with the bot
#bot.add_cog(main_cog(bot))
#bot.add_cog(image_cog(bot))
#bot.add_cog(music_cog(bot))

#start the bot with our token
#bot.run(os.getenv("TOKEN"))

