from cogs.imports import *

class rr(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["rick", "rrole"])
    async def rickroll(self,ctx, member:discord.Member):
        if member == ctx.author:
            await ctx.author.send("Why the fuck are you trying to rick roll yourself?||<a:rickroll:793915241058009128>||")
        elif member == None:
            await ctx.author.send("Why the fuck are you trying to rick roll nobody?||<a:rickroll:793915241058009128>||")    
        else:    
            await ctx.message.delete()
            await ctx.send(f"{member.mention} | {ctx.author.mention} sent you this: ||<a:rickroll:793915241058009128>||")     

def setup(client):
    client.add_cog(rr(client))