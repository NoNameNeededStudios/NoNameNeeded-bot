from cogs.imports import *

import os
class whois(commands.Cog):

    def __init__(self, client):
        self.client = client



    
    @commands.command(aliases=["who is", "user"]) #whois command
    async def whois(self,ctx, user: discord.Member =None):
        User= user or ctx.author
        avatar = User.avatar_url
       
        
        roles = User.roles
        list_names = [role.mention for role in roles]
        
    
        if User.bot:
            isbot = 'Yes'
        else:
            isbot = 'No'

        joined = User.joined_at.strftime("%a, %d %B %Y , %I :%M %p UTC")
        ct = User.created_at.strftime("%a, %d %B %Y , %I :%M %p UTC")
        embed = discord.Embed(title=f'Discord Whois Complete', description=f'`Who is {user}`', colour=discord.Colour.random(), inline=False)
        embed.set_thumbnail(url = user.avatar_url)
        embed.add_field(name='Is this user a `bot`?', value=f'**`{isbot}`**',inline=False)
        embed.add_field(name="Joined This Server at", value=f"Joined this server at `{joined}`", inline=False)

        embed.timestamp = ctx.message.created_at
        embed.set_footer(text = f"Asked by **{ctx.author}**")

        embed.add_field(name='Account Creation Date', value=f'**`{ct}`**', inline=False)
  
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)    


def setup(client):
    client.add_cog(whois(client))