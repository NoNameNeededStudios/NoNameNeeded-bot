from cogs.imports import *


class ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    
    @commands.command() 
    async def ping(self,ctx):
        embed = discord.Embed(title="Calcuating..", description="‎ ‎Calcuating Ping..",colour=discord.Color.random())
        msg = await ctx.send(embed=embed)
        await sleep(2)
        embedPING = discord.Embed(title="Pong!", description=f"‎{round(self.client.latency * 1000)}MS <a:4a26aa20e8a54406b3b8a72b3d10132d:797114328956010515>",colour=discord.Color.random())
        await msg.edit(embed=embedPING)


def setup(client):
    client.add_cog(ping(client))