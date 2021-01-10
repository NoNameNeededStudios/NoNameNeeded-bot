from cogs.imports import *



search = ("AIzaSyCPgBJXR3moe7iHV6CJLLFZdrPmD8I8AdM")    
app_id = '4RPXT4-4VYAXX3Q6G'
wolf = wolframalpha.Client(app_id)  

class command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calc(self,ctx,*,ques):
       
        res = wolf.query(ques) 
        answer = next(res.results).text 
        em = discord.Embed(title = f"question ="+ ques +"",
                        description = f"answer ="+ answer+ "",
                        color= discord.color.random())
        await ctx.send(embed = em)

def setup(client):
    client.add_cog(command(client))