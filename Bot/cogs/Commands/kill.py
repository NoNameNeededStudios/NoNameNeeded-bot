from cogs.imports import *

class kill(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["kill", "destroy"])
    async def murder(self,ctx,member:discord.Member=None):
        if member == None:
            await ctx.send("oh shit, i cant kill air", delete_after=4)
        elif member.id == ctx.author.id:
            await ctx.send("....Why? why do you want to kill your self", delete_after=6)
        elif member.bot:
            await ctx.send("No, back off my kind!")
        else:
            user = ctx.author.mention
            memb = member.mention


            killdashmethods = [f"{user} bruhed {memb}", f"{user} memed {memb}", f"{user} shot {memb}", f"{memb} was walking down the road, until he saw, a giant fucking dick and it killed him", f"{memb} he said his dick was big, he lied, so he died", 'i ran out of ideas, so he just died', f"if i ever stop singing i will expload - {memb}'s last words", f"daddy he said, death he got", "no...he is my best friend :)", "eh maybe next time", "too lazy for that", f"{memb} was walking thru the woods until a landmine hit him!", f"{memb} was walking down the road until he got a car in his face", f"{user}: ***Omae wa mō shinde iru***. {memb}: ***Nāni?***, and he died"]


            kill = random.choice(killdashmethods)
            await ctx.send(kill)

def setup(client):
    client.add_cog(kill(client))