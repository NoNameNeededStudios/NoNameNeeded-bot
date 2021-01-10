from cogs.imports import *

class GameCommands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases = ['gay'])
    async def gaymeter(self,ctx, member : discord.Member = None):
        if member == None:
            member = ctx.message.author
         

        else:
            pass
            
        
        rangay = random.randrange(101)
        if rangay > 90:
                ctx.guild = ctx.guild
                user = ctx.author
                createrole = await ctx.guild.create_role(name="Gay")
                role = createrole
                await user.add_roles(role)
                await ctx.send(f"Looks like you got the gay role {member.mention}") #adds the role
        else:
            pass
        metergay = ':rainbow_flag:' * int(rangay/10) + ':white_square_button:' * int(10-rangay/10)
        embed = discord.Embed(
            title = 'GAYMETER',
            colour = discord.color.random()
        )
        embed.add_field(name=f"{member}'s Gaymeter:", value=f'{metergay} {rangay}%', inline = False)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)    



        #*Meme Meter

    @commands.command(aliases = ['mr', "memerate", "memer"])
    async def mememeter(self,ctx, member : discord.Member = None):
        if member == None:
            member = ctx.message.author
            

        else:
            pass
            
        rangay = random.randrange(101)
        if rangay > 90:
                ctx.guild = ctx.guild
                user = ctx.author
                createrole = await ctx.guild.create_role(name="Memey")
                role = createrole
                await user.add_roles(role)
                await ctx.send(f"Looks like you got the Memey role {member.mention}") #adds the role
        else:
            pass
        metergay = '🐸' * int(rangay/10) + ':white_square_button:' * int(10-rangay/10)
        embed = discord.Embed(
            title = 'MEME METER',
            colour = discord.color.random()
        )
        embed.add_field(name=f"{member}'s Meme meter:", value=f'{metergay} {rangay}%', inline = False)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(GameCommands(client))
        