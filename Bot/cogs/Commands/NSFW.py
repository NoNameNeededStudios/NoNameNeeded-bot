from cogs.imports import *


Bank = "./Jsons/mainbank.json"
Pets = "./Jsons/pets.json"
em_colors = [discord.Colour.red, discord.Colour.blue ,  discord.Colour.green, discord.Colour.orange, discord.Colour.gold, discord.Colour.dark_orange, discord.Colour.dark_blue, discord.Colour.purple, discord.Colour.dark_magenta]

search = ("AIzaSyCPgBJXR3moe7iHV6CJLLFZdrPmD8I8AdM")    
app_id = '4RPXT4-4VYAXX3Q6G'
wolf = wolframalpha.Client(app_id)  

class ExtrasNSFW(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['sex'])
    async def porn(self,ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
        
   
      
  #logic
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/sex/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/porn/hot/.json?limit=100"

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
        else:
            await ctx.send("enable NSFW for these commands")    


    @commands.command(pass_context=True, aliases=["booty"])
    async def ass(self,ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
        
   
      
  #logic
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/ass/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/booty/hot/.json?limit=100"

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
        else:
            await ctx.send("enable NSFW for these commands")    

   

    


    @commands.command(pass_context=True, aliases=["hentai sex", "anime sex"])
    async def hentai(self,ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
        
   
      
  #logic
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/hentai/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/hentai/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0,25)
                    url = res['data']['children'][meme]['data']['url']

                      
                        

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title="Enjoy", description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(text=f"Requested by {ctx.author} | Made by voidy with horny in mind", icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=embed)
                        

                    elif str(url)[-3:] == "gif":
                        embed = discord.Embed(title="Enjoy", description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send("enable NSFW for these commands")        

    @commands.command(pass_context=True, aliases=['dicks', "penis", "dick"])
    async def cock(self,ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
        
   
      
  #logic
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/cock/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/penis/hot/.json?limit=100"

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
        else:
            await ctx.send("enable NSFW for these commands")      


    @commands.command(pass_context=True, aliases=['pussy', "squirting"])
    async def vegina(self,ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
        
   
      
  #logic
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/squirting/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/squirting/hot/.json?limit=100"

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
        else:
            await ctx.send("enable NSFW for these commands")  

    @commands.command(pass_context=True, aliases=['tittes', "boob"])
    async def boobs(self,ctx):
        '''fetches a random meme and shows it'''
        if ctx.channel.is_nsfw():
        
   
      
  #logic
            if random.randint(0, 1) == 1:
                meme_url = "https://www.reddit.com/r/boobs/hot/.json?limit=100"
            else:
                meme_url = "https://www.reddit.com/r/boobs/hot/.json?limit=100"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(meme_url) as r:
                    res = await r.json()
                    meme = random.randint(0,25)
                    url = res['data']['children'][meme]['data']['url']

                    title = res["data"]["children"][meme]["data"]["title"]    
                        

                    if str(url)[-3:] != "gif":
                        embed = discord.Embed(title=title, description="‎")
                        embed.set_image(url=url)
                        embed.set_footer(text=f"Requested by {ctx.author} | Made by voidy with horny in mind", icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=embed)
                        

                    elif str(url)[-3:] == "gif":
                        embed = discord.Embed(title=title, description="")
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
        else:
            await ctx.send("enable NSFW for these commands")                                                         

     
def setup(client):
    client.add_cog(ExtrasNSFW(client)) 