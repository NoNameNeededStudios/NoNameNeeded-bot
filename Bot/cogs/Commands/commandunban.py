from cogs.imports import *

class unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True) 
    async def unban(self,ctx, *, member):
           
             
                try:
                   
                    banned_users = await ctx.guild.bans()
                    member_name, member_discriminator = member.split("#")

                    for ban_entry in banned_users:
                        user = ban_entry.user

                        if (user.name, user.discriminator) == (member_name, member_discriminator):
                            await ctx.guild.unban(user)
                            unban = discord.Embed(title=f"UNBAN", description=f"Unbanned {user.mention}", colour =discord.color.random())
                            await ctx.send(embed=unban)
                except:
                    await ctx.send("<a:rickroll:792418332326363136> No i dont think i will.because they don't exist. <a:alert:791986335770476604>") 


def setup(client):
    client.add_cog(unban(client))