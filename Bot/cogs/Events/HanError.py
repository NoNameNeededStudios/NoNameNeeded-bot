from cogs.imports import *

class ERROR_HANDLER(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'Sorry but you can only use this command after **{round(error.retry_after)} seconds**')

        elif isinstance(error, commands.CommandInvokeError):
     
            embed = discord.Embed(title = "Error",description =f"Something Sus Happened!",color = discord.color.random())
            await ctx.send(embed=embed)  
            
            if ctx.guild.id == 793226316862062593:
                channel = self.client.get_channel(795959496039333908)
                await channel.send(error)
                raise error  
            else:
                raise error    

        elif isinstance(error, commands.MissingPermissions):
           
            embed = discord.Embed(title = "Error",description =f"Sorry you do not have permissions to use this command!",color = discord.color.random())
            await ctx.send(embed=embed)   

        elif isinstance(error, MissingAnyRole):
          
            embed = discord.Embed(title = "Error",description =f"Sorry you do not have permissions to use this command!",color = discord.color.random())
            await ctx.send(embed=embed) 

        elif isinstance(error, MissingRequiredArgument):
           
            await ctx.send("Sorry. but it looks like your not doing the command right please enter all the required args")

        elif isinstance(error, CommandNotFound):
            
            embed = discord.Embed(title = "Error",description =f"Invalid command \n please use n!help for more info and commands",color =discord.color.random())
            await ctx.send(embed=embed)   

        elif isinstance(error, MemberNotFound):
         
            embed = discord.Embed(title = "Error",description =f"Member Not Found",color = discord.color.random())
            await ctx.send(embed=embed)  

        elif isinstance(error, MemberNotFound):
        
            embed = discord.Embed(title = "Error",description =f"Sorry it looks like you're missing something to do that command, or something went wrong!",color = discord.color.random())
            await ctx.send(embed=embed)                         
        else:
            raise error 

def setup(client):
    client.add_cog(ERROR_HANDLER(client))