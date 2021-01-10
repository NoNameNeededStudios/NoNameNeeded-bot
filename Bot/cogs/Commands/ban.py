from cogs.imports import *

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self,ctx, user: discord.Member, *, reason="No reason provided"):
            if user.id == 786164164690706462:
                await ctx.send("Hey man, why u gotta be rude :(")
            elif user == ctx.author:
                await ctx.send("Umm.banning you in 5")
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
               
                  
                    await user.ban(reason=reason)
                    ban = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", colour =discord.color.random())
                    await ctx.message.delete()
                    await ctx.channel.send(embed=ban)
                    await user.send(embed=ban)   


def setup(client):
    client.add_cog(ban(client))