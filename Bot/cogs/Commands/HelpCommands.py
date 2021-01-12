from cogs.imports import *


em_colors = [discord.Color.red, discord.Color.blue ,  discord.Color.green, discord.Color.orange, discord.Color.gold, discord.Color.dark_orange, discord.Color.dark_blue, discord.Color.purple, discord.Color.dark_magenta]

class HelpCommands(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(aliases=["game", "game commands", "game_commands"])
    async def games(self,ctx):

        prefix = "n!"

        embed = discord.Embed(title="Game Command", description="All Game Commands")
        embed.add_field(name=f"Games",value=f"  \n > ***Guess|:grey_exclamation:*** do `{prefix}Guess (1-10)` to play this game,\n > \n > ***Rock Paper Scissors| ✂*** do `{prefix}rps <r/p/s>` To play some Rock Paper Scissors \n > \n > **Fight🥋** do `fight <@mention_user>` to fight a user")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["fun commnads", "fun_commands"])
    async def fun(self,ctx):
        prefix = "n!"

        embed = discord.Embed(title="Fun Command", description="All Fun Commands")
        embed.add_field(name=f"Fun",value=f" >  ***gay:rainbow_flag:*** do `{prefix}gay @mention_user` which shows the percentage of gay.\n > \n > ***echo:speaking_head:*** `{prefix}echo` the bot repeats what you say \n > \n > ***meme:frog:*** do `{prefix}meme` sends random memes\n > \n > ***idiot:woozy_face:*** do `{prefix}idiot` makes u look like an idiot\n > \n > ***slap:hand_splayed:*** do `{prefix}slap` slaps your avatar \n > \n > ***RickRoll<a:rickroll:792418332326363136>*** do `{prefix}rick/rrole` to rickroll someone \n > \n > ***gif<:E_:795035013657657374>*** do `gif <whatever you want to search for>` and get some cool gifs!")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["help Super Secert", "help ss"])
    async def ss(self,ctx):
        embed = discord.Embed(title="Secret Commands", description="All Weird Commands")
        embed.add_field(name="Super Secrert, lol no", value=" > ***8BALL:crystal_ball:*** do `n!8ball <the question>` to talk to a magic ball with magically answers \n > \n > ***kill:knife:*** do `n!kill <mention_member>` and kill them with some intersting ways \n > \n > ***ping <a:4a26aa20e8a54406b3b8a72b3d10132d:797114328956010515>*** do `n!ping` to find this bot's sexy ping! \n > \n > ***roll*** no emoji lol do `n!roll` and roll, this is the most useless command by far \n > \n > ServerInfo<:Info:798166430121984070> do `n!server info` to get that server info, also showing the owner is glitched, blame discord ")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["help reddit", "help r", "r/help"])
    async def reddit(self,ctx):
        embed = discord.Embed(title="Reddit Commands <:309459767758290944:798302035656572948>", description="All Reddit Commands")
        embed.add_field(name="Reddit", value=" > ***Submissions <:309459767758290944:798302035656572948>*** do `n!r/ <subbreddit> <top/new/hot>` to see a submission from that post \n > \n > ***r/search <:309459767758290944:798302035656572948>  *** do `n!r/search <subreddit> <what you want to search for>` to find a post in a subreddit related to what you want to find! \n > \n >  *** r/random <:309459767758290944:798302035656572948> *** Do `n!r/random` to find werid random reddit posts ")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)    


    @commands.command(aliases=["mods", "mod commands", "moderation commands"])
    async def mod(self,ctx):
        
        prefix = "n!"

        embed = discord.Embed(title="Mod Command", description="All Moderation Commands")
        embed.add_field(name="Moderation",value=f" > ***kick:foot:*** do`{prefix}kick<user>` kicks an user from the server\n > \n > ***ban:hammer:*** do `{prefix}ban<username>` bans an user from the server\n > \n > ***unban:x:*** do `{prefix}unban<username>` unbans an user from the server\n > \n > ***clear:scissors:*** do `{prefix}clear<number_of_message>` clears message from channel")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["help nsfw", "help porn"])
    async def nsfw(self,ctx):

        if ctx.guild.id == 739766442672783360:
            await ctx.send("enable NSFW for these commands")
        else:    

            embed = discord.Embed(title="NSFW",description="All NSFW Commands | NSFW must be on for these commands to work")
            embed.add_field(name="NSFW", value= f"> ***Dicks:eggplant:*** do `n!cock/dick` to find some nice cocks \n > \n > ***Boobs:cherries:*** do `n!boobs` to find some nice fuckable boobs \n > \n > ***Pussy:sweat_drops:*** do `n!pussy` to see that pussy! \n > \n > ***Ass:peach:*** do `n!ass` to get that horney ass \n > \n > ***Hentai***<a:animebooty:795035015372996628> do `n!hentai` for some...real anime sex")    
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
   
    @commands.command(aliases=["extras", "es", "esa"])
    async def extra(self,ctx):

        prefix = "n!"

        embed = discord.Embed(title="Extras Command", description="All Extra Commands")
        embed.add_field(name="Extras",value=f"> ***yt🔺*** do `{prefix}yt (youtube video name)` searchs for a youtube video\n > \n > ***echo:microphone2:*** do`{prefix}echo<what to echo>` the bot will say your message\n > \n > ***dm:mobile_phone:*** do `{prefix}dm <mention member to dm> <message context>` this will dm the member you want, please do not abuse this! \n > \n > ***whois*** do `{prefix}whois<mention member>` to show the information about a member \n > \n > ***temp:thermometer:*** do `{prefix}temp<city name>` to see the information about your city \n > \n > **tts<:5534_feelscrusademan:792843219758088201>** Send Text-To-Speech Messages. Usage: `{prefix}tts <language> <text>` | **DM VERSION** you can also dm people! `{prefix}ttsdm <mention user> <language> <text>`")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command()
    async def title_embed(self, ctx,*,message):
        ttl, sep, txt = message.partition(";")
        emb = discord.Embed(title = ttl, description = txt)
        await ctx.channel.purge(limit = 1)
        emb.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = emb)

    @commands.Cog.listener()
    async def on_message(self,message):
        
  
            prefix = "n!"
            if message.content == (f"n!help"):
                try:
                
                    em = discord.Embed(title= "NNN Commands", description="**[INVITE](https://discord.com/api/oauth2/authorize?client_id=786164164690706462&permissions=2147483639&scope=bot)** | **[DISCORD](https://dis.gd/threads)** | **[Support Server](https://discord.gg/gtmeu6h5aR)**")
                    em.add_field(name = "**Game Commands🎮**\n" ,value = f"Do `{prefix}games`")
                    em.add_field(name= "**Fun Commands💡**\n" ,value = f"Do `{prefix}fun`") 
                    em.add_field(name= "**NSFW Commands:peach:**\n" ,value = f"Do `{prefix}nsfw`") 
                    em.add_field(name="**Moderation Commands:tools:**\n",value = f"Do `{prefix}mod`")
                    em.add_field(name="**Reddit Commands** <:309459767758290944:798302035656572948> \n",value = f"Do `{prefix}r/help`")  
                    em.add_field(name="**Supa Secret Commands:question:**\n",value = f"Do `{prefix}ss`")
                    em.add_field(name="**Extras Commands**❓\n",value = f"Do `{prefix}es/extras`")  
                    em.set_footer(text=f"Requested by {message.author}", icon_url = message.author.avatar_url) 
                    await message.author.send(embed=em)      
                    
                    await message.add_reaction("<a:8584_verified_blue1:792846413909196831>")
                except:
                    em = discord.Embed(title= "NNN Commands", description="**[INVITE](https://discord.com/api/oauth2/authorize?client_id=786164164690706462&permissions=2147483639&scope=bot)** | **[DISCORD](https://dis.gd/threads)**")
                    em.add_field(name = "**Game Commands🎮**\n" ,value = f"Do `{prefix}games`")
                    em.add_field(name= "**Fun Commands💡**\n" ,value = f"Do `{prefix}fun`") 
                    em.add_field(name= "**NSFW Commands:peach:**\n" ,value = f"Do `{prefix}nsfw`") 
                    em.add_field(name="**Moderation Commands:tools:**\n",value = f"Do `{prefix}mod`")
                    em.add_field(name="**Supa Secret Commands:question:**\n",value = f"Do `{prefix}ss`") 
                    em.add_field(name="**Extras Commands**❓\n",value = f"Do `{prefix}es/extras`")  
                    em.set_footer(text=f"Requested by {message.author}", icon_url = message.author.avatar_url) 
                    await message.channel.send(embed=em)      
                    await message.add_reaction("<a:8584_verified_blue1:792846413909196831>")
                    
            else:
                pass          
                   

       
  
       


def setup(client):
    client.add_cog(HelpCommands(client))
