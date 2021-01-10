from cogs.imports import *

class role(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dice", "dice roll"])
    async def roll(self,ctx):
        var = random.randint(1,6)
        embed = discord.Embed(title=f"""
        
            <:minecraftheart:795035007533842442> ***You Got A*** `{var}` <:minecraftheart:795035007533842442> 

        
        
        
        
        """, description="GG", colour=discord.Color.random())

        await ctx.send(embed=embed)     


def setup(client):
    client.add_cog(role(client))