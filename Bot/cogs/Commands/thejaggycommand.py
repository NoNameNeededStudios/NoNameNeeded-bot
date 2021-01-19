from cogs.imports import *

class jagggy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["space", "s p a c e"])
    async def jaggy(self,ctx,*,kaggy):

        if "@" in kaggy:
            await ctx.send("No Mentions or @s")
        else:
            word = kaggy
            result = " ".join(word)
            await ctx.send(result)

def setup(client):
    client.add_cog(jagggy(client))