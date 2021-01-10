from cogs.imports import *


Bank = "./Jsons/mainbank.json"
Pets = "./Jsons/pets.json"
em_colors = [discord.Colour.red, discord.Colour.blue ,  discord.Colour.green, discord.Colour.orange, discord.Colour.gold, discord.Colour.dark_orange, discord.Colour.dark_blue, discord.Colour.purple, discord.Colour.dark_magenta]

search = ("AIzaSyCPgBJXR3moe7iHV6CJLLFZdrPmD8I8AdM")    
app_id = '4RPXT4-4VYAXX3Q6G'
wolf = wolframalpha.Client(app_id)  

class EXCLUSIVE(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(aliases=["cont", "contu"])
    async def contribution(self,ctx, member:discord.Member, *, contribution ):
        if ctx.guild.id != 793226316862062593:
            pass
        else:
            if ctx.author.id == 730505256953446422 or 597139650590670859 or 419300759679533077 or 736820906604888096 or 621397007332016145:
                channel = self.client.get_channel(793925155768238120)
                await channel.send(f"{member.mention} **Did a Contribution \n Contribution:** {contribution}")
                await ctx.message.delete()
            else:
                await ctx.message.delete()
                await ctx.send("You cant use that!", delete_after=4)    


    @commands.command(aliases=["approve", "apply"])
    async def accept(self,ctx, member:discord.Member, *, role):
        if ctx.guild.id != 793226316862062593:
            pass
        else:
            if ctx.author.id == 730505256953446422 or 597139650590670859 or 419300759679533077 or 736820906604888096 or 621397007332016145:
                channel = self.client.get_channel(793925223518175242)
                await channel.send(f"{member.mention} **was approved by** {ctx.author.mention} **as a** `{role}`")
                await member.send(f"You **were approved by** {ctx.author.mention} **as a** `{role}`")
                await ctx.message.delete()
            else:
                await ctx.message.delete()
                await ctx.send("You cant use that!", delete_after=4)   

    @commands.command(aliases=["decline", "deny"])
    async def remove(self,ctx, member:discord.Member, *, reason):
        if ctx.guild.id != 793226316862062593:
            pass
        else:
            if ctx.author.id == 730505256953446422 or 597139650590670859 or 419300759679533077 or 736820906604888096 or 621397007332016145:
                channel = self.client.get_channel(793925223518175242)
                await channel.send(f"{member.mention} **was declined by** {ctx.author.mention} **because** {reason}")
                await member.send(f"You **were declined by** {ctx.author.mention} **because** {reason}")
                await ctx.message.delete()
            else:
                await ctx.message.delete()
                await ctx.send("You cant use that!", delete_after=4)               




   
                

                

def setup(client):
    client.add_cog(EXCLUSIVE(client))