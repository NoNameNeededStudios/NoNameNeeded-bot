from cogs.imports import *

class serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["server info", "si", "SERVER", "server"])
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        if description == None or "None":
            description = "This server has no description"
        
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.random()
            )
      
        embed.add_field(name="Owner", value=f"Server Owner is: `{owner}` | owner cant be loaded..", inline=True)
        embed.add_field(name="Server ID", value=f"Server ID is: `{id}`", inline=True)
        embed.add_field(name="Region", value=f"Server Region is :`{region}`", inline=True)
        embed.add_field(name="Member Count", value=f"Server Member Count is: `{memberCount}`", inline=True)
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(serverinfo(client))