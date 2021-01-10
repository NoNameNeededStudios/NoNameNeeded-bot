from cogs.imports import *

class cOG(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self,ctx, user: discord.Member, *, reason="No reason provided"):
            if user.id == 786164164690706462:
                await ctx.send("Hey man, why u gotta be rude :(")
            elif user == ctx.author:
                await ctx.send("Umm.kicking you in 5")
                await sleep(1)
                await ctx.send("4")
                await sleep(1)
                await ctx.send("3")
                await sleep(1)
                await ctx.send("2")
                await sleep(1)
                await ctx.send("1")
                await sleep(1)
                await ctx.send("Hhaah u fell for it.i think")

            else: 
               
                   
                    await user.kick(reason=reason)
                    kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", colour =discord.color.random())
                    await ctx.message.delete()
                    await ctx.channel.send(embed=kick)
                    await user.send(embed=kick)   

def setup(client):
    client.add_cog(cOG(client))