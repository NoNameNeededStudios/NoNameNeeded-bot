from cogs.imports import *

class GIF(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=["gif", "gifs"])
    async def giphy(self,ctx, *, search):
        embed = discord.Embed(colour=discord.Colour.random())
        session = aiohttp.ClientSession()

        if search == '':
            response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=M2qAHmCN3yF5zCY1Uf3ougrsg9UvXDv1')
            data = json.loads(await response.text())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=M2qAHmCN3yF5zCY1Uf3ougrsg9UvXDv1&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        await session.close()

        await ctx.send(embed=embed)



        #!dosent need a file so i put it here
    @commands.command(pass_context=True,aliases=["frespect", "respect", "F"])
    async def f(self,ctx):
        await ctx.message.delete()
        mesg = await ctx.send(f"{ctx.author.mention} has paid their respects <:F_:797049974360637441>")
        await mesg.add_reaction("<:F_:797049974360637441>")



        #!TTS WAS BEING GAY SOOO
  
    
    @commands.command(aliases = ["tts"])
    async def text_to_speech(self,ctx,lang:str= 'en',*,message:str):
        
        
        mytext = message
        language = lang
        try:
            myobj = gTTS(text=mytext, lang=language, slow=False)
            obj = io.BytesIO()
            myobj.write_to_fp(obj)
            obj.seek(0)
            file = discord.File(obj, 'listen.mp3')
            
            em = discord.Embed(title = "Text to speech",description= message,color = discord.Colour.red()).set_footer(text = f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        except:
            mytext = lang + mytext
            language = "en"
            myobj = gTTS(text=mytext, lang=language, slow=False)
            obj = io.BytesIO()
            myobj.write_to_fp(obj)
            obj.seek(0)
            file = discord.File(obj, f'{mytext}.mp3')
            await ctx.send(f"{ctx.author.mention} please use a support langauge, this has been made to english", delete_after=4)
            
            em = discord.Embed(title = "Text to speech",description= message,color = discord.Colour.red()).set_footer(text = f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
            

        #myobj.save("welcome.mp3") 
        
        #os.system("mpg321 welcome.mp3")

        await ctx.send(file = file)       

def setup(client):
    client.add_cog(GIF(client))

