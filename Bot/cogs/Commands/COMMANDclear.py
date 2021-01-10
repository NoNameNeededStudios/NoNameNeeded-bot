from cogs.imports import *

class command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def clear(self,ctx, amount:int):
        if amount > 100:
            await ctx.send("Sorry i cant Clear that many messages")
        else:    
            await ctx.channel.purge(limit = amount+1)

def setup(client):
    client.add_cog(command(client))