from cogs.imports import *

class DEV(commands.Cog):

    def __init__(self, client):
        self.client = client


    DEV_IDS = ["730505256953446422", "621397007332016145", "597139650590670859", "759129467414380554",
     "726528714292330586", "692051505188044850", "269030651989065731", "619440876451528707",
      "723799589110415362", "797138695596670978", "692051505188044850"]

    @commands.command()
    async def raise_error(self,ctx):
        
        for i in DEV_IDS:
            if i in ctx.author.id:
            

                await ctx.send("Error Raised")
                embed = discord.Embed(title="lol", description="GAY",color=discord.Colour.random)
            else:
                await ctx.send("You cannot use this command \n Only Developers Can")    





def setup(client):
    client.add_cog(DEV(client))        