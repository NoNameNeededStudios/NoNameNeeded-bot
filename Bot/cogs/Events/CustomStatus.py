from cogs.imports import *


em_colors = [discord.Colour.red, discord.Colour.blue ,  discord.Colour.green, discord.Colour.orange, discord.Colour.gold, discord.Colour.dark_orange, discord.Colour.dark_blue]


class LoopingStatus(commands.Cog):

    def __init__(self, client):
        self.client = client

  

    async def status(self):
        while True:
            await self.client.wait_until_ready()
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(self.client.guilds)} Servers'))
            await sleep(5)
            await self.client.change_presence(activity=discord.Game(name=f'Minecraft'))
            await sleep(5)
            await self.client.change_presence(activity=discord.Game(name=f'Step-Dream'))
            await sleep(5)
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Mr Beast's Rewind"))
            await sleep(5)
            await self.client.change_presence(activity=discord.Game(name='PING for PREFIX'))
            await sleep(5)
            await self.client.change_presence(activity=discord.Game(name='Dream Moaning'))
            await sleep(5)  
            

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client.user} has Awoken!')
        await self.client.loop.create_task(self.status())




def setup(client):
    client.add_cog(LoopingStatus(client))
