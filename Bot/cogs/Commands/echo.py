from cogs.imports import *

class command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def echo(self,message, *, content:str, name="echo.repeat2.410"):
    
        await message.channel.purge(limit=1)
        em = discord.Embed(title="echo", description=content, colour = discord.color.random ())


        await message.send(embed= em)


def setup(client):
    client.add_cog(command(client))