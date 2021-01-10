from cogs.imports import *

class meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['memes'])
    async def meme(self,ctx):
        '''fetches a random meme and shows it'''

        if random.randint(0, 1) == 1:
            meme_url = "https://www.reddit.com/r/dankmemes/new.json?sort=top/?t=all"
        else:
            meme_url = "https://www.reddit.com/r/dankmemes/new.json?sort=hot"

        async with aiohttp.ClientSession() as cs:
            async with cs.get(meme_url) as r:
                res = await r.json()
                meme = random.randint(0,25)
                url = res['data']['children'][meme]['data']['url']

                title = res["data"]["children"][meme]["data"]["title"]    
                    

                if str(url)[-3:] != "gif":
                    embed = discord.Embed(title=title, description="‎")
                    embed.set_image(url=url)
                    embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    

                elif str(url)[-3:] == "gif":
                    embed = discord.Embed(title=title, description="")
                    embed.set_image(url=url)
                    await ctx.send(embed=embed)


def setup(client):
    client.add_cog(meme(client))