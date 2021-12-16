import discord
import math
import sympy
import numpy
import random
from discord.ext import commands

class bus_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.a = int

    @commands.command(name="버스비")
    async def 버스비(ctx, a):
        b = a * 0.95
        
        c = math.floor(b / 1.95)
        d = math.floor(b / 2.95)
        e = math.floor(b / 3.95)
        await ctx.send(c)

    #def __init__(self, bot):    
    #    self.bot = bot
    #@commands.command(name="버스비")

    #async def 버스비(ctx, *arg):
    #    query = " ".join(arg)
    #async def calc(ctx, operation:str):
    #    await ctx.send(eval(operation))

    #    await ctx.send(query)

    #    b = math.floor(a * 0.95 / 1.95)
    #    c = math.floor(a * 0.95 / 2.95)
    #    d = math.floor(a * 0.95 / 3.95)
    ##    await ctx.send(a)
    #    await ctx.send(c)


#    @commands.command()
#    async def 경매(ctx, a:int):
#        b = a * 0.95 / 4 * 3
#        c = a * .95 / 8 * 7
#        await ctx.send(b)
#        await ctx.send(c)


    #async def 버스비(ctx, a):
#        b = a/3
     #  await ctx.send(b)
