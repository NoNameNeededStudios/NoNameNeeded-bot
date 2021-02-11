import discord
from discord.ext import commands
import random
import aiohttp


class ExtrasNSFW(commands.Cog):
    ALLOW_NSFW: str = f"enable NSFW for these commands"
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['sex'])
    async def porn(self, ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/sex/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/porn/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0, 25)
                    url = res['data']['children'][meme]['data']['url']

                    title = res["data"]["children"][meme]["data"]["title"]

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title=title, description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(
                            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)

                    else:
                        embed = discord.Embed(title=title, description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.ALLOW_NSFW}")

    @commands.command(pass_context=True, aliases=["booty"])
    async def ass(self, ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/ass/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/booty/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0, 25)
                    url = res['data']['children'][meme]['data']['url']

                    title = res["data"]["children"][meme]["data"]["title"]

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title=title, description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(
                            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)

                    else:
                        embed = discord.Embed(title=title, description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.ALLOW_NSFW}")

    @commands.command(pass_context=True, aliases=["hentai sex", "anime sex"])
    async def hentai(self, ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
            meme_url = "https://www.reddit.com/r/hentai/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0, 25)
                    url = res['data']['children'][meme]['data']['url']

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title="Enjoy", description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(
                            text=f"Requested by {ctx.author} | Made by voidy with horny in mind", icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)

                    else:
                        embed = discord.Embed(title="Enjoy", description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.ALLOW_NSFW}")

    @commands.command(pass_context=True, aliases=['dicks', "penis", "dick"])
    async def cock(self, ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/cock/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/penis/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0, 25)
                    url = res['data']['children'][meme]['data']['url']

                    title = res["data"]["children"][meme]["data"]["title"]

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title=title, description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(
                            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)

                    else:
                        embed = discord.Embed(title=title, description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.ALLOW_NSFW}")

    @commands.command(pass_context=True, aliases=['pussy', "squirting"])
    async def vegina(self, ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
            meme_url = "https://www.reddit.com/r/squirting/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0, 25)
                    url = res['data']['children'][meme]['data']['url']

                    title = res["data"]["children"][meme]["data"]["title"]

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title=title, description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(
                            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)

                    else:
                        embed = discord.Embed(title=title, description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.ALLOW_NSFW}")

    @commands.command(pass_context=True, aliases=['tittes', "boob"])
    async def boobs(self, ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
            meme_url = "https://www.reddit.com/r/boobs/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0, 25)
                    url = res['data']['children'][meme]['data']['url']

                    title = res["data"]["children"][meme]["data"]["title"]

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title=title, description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(
                            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)

                    else:
                        embed = discord.Embed(title=title, description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.ALLOW_NSFW}")


def setup(client):
    client.add_cog(ExtrasNSFW(client))
