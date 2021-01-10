from cogs.imports import *

em_colors = [discord.Colour.red, discord.Colour.blue ,  discord.Colour.green, discord.Colour.orange, discord.Colour.gold, discord.Colour.dark_orange, discord.Colour.dark_blue]


class CommandEvents(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self,ctx):
        print("Bot Has Been Activated - Please Double Check Everything")
        member = 730505256953446422
        await member.send("Bot is online!")
        

       

 
def setup(client):
    client.add_cog(CommandEvents(client))   