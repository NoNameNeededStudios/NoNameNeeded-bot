from cogs.imports import *



class yt(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(aliases= ['yt'])
    async def youtube(self,ctx,*,message):
  
        try:
            a = discord.Embed(title ="**Top Results for ** your search :", color = discord.color.random ())  
            await ctx.send(embed = a)          
            results = SearchVideos(message,mode="dict",max_results =1)
            print(results.result())
            d = discord.Embed(title ='**'+results.result()['search_result'][0]['title']+'**'+'\n'+"Channel : "+results.result()['search_result'][0]['channel']+'\n'+'Duration : '+str(results.result()['search_result'][0]['duration'])+'\n'+'Views : '+str(results.result()['search_result'][0]['views'])+'\n'+"Publish Time : " +str(results.result()['search_result'][0]['publishTime'])+'\n',color = discord.color.random ())
            await ctx.send(embed = d)
            await ctx.send('Link : '+results.result()['search_result'][0]['link']) 
        except Exception as e:
            print(e)
            c = discord.Embed(title ="No results found :sob:",color = discord.color.random ())
            await ctx.send(embed = c)

def setup(client):
    client.add_cog(yt(client))