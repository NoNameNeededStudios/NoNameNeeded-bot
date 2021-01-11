from cogs.imports import *


class dms(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=["message", "dm user"])
    async def dm(self,ctx,member:disord.Member=None,*, dm):
        if member == None:
            await ctx.author.send("Mention someone to dm dummy")
        elif member.id == ctx.author.id:
            await ctx.author.send("no")
        else:
            await member.send(dm)    

    