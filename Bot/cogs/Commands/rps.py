from cogs.imports import *


class rps(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command()
    async def rps(self,ctx, user_choice):
        rpsGame = ['rock', 'paper', 'scissors']
        playerchoices = ["r", "p", "s", "rock", "paper", "scissors"]
        pc_choice=(random.choice(rpsGame))
        if user_choice.lower() in playerchoices:
            await ctx.send(f'Choice: `{user_choice}`\nBot Choice: `{pc_choice}`')
        if user_choice.lower() not in playerchoices:
            await ctx.send('**Error** This command only works with rock, paper, or scissors or r/p/s.')
        elif user_choice=="rock" and pc_choice=="paper":       
            await ctx.send(f"looks likes i won!")

        elif user_choice=="paper" and pc_choice=="paper":
            await ctx.send("its a tie!")

        elif user_choice=="scissors" and pc_choice=="paper":
            await ctx.send(f"{ctx.author.mention} won!")

        elif user_choice=="rock" and pc_choice=="rock":       
            await ctx.send(f"it's a tie")

        elif user_choice=="paper" and pc_choice=="rock":
            await ctx.send(f"{ctx.author.mention} won!")

        elif user_choice=="scissors" and pc_choice=="rock":
            await ctx.send("looks likes i won!")

        elif user_choice=="rock" and pc_choice=="scissors":       
            await ctx.send(f"{ctx.author.mention} won!")

        elif user_choice=="paper" and pc_choice=="scissors":
            await ctx.send("looks likes i won!")

        elif user_choice=="scissors" and pc_choice=="scissors":
            await ctx.send("it's tie!")

        elif user_choice=="r" and pc_choice=="paper":       
            await ctx.send(f"looks like i won!")

        elif user_choice=="p" and pc_choice=="paper":
            await ctx.send(f"its a tie!")
            
        elif user_choice=="s" and pc_choice=="paper":
            await ctx.send(f"{ctx.author.mention} won!")

        elif user_choice=="r" and pc_choice=="rock":       
            await ctx.send(f"it's a tie")

        elif user_choice=="p" and pc_choice=="rock":
            await ctx.send(f"{ctx.author.mention} won!")

        elif user_choice=="s" and pc_choice=="rock":
            await ctx.send("looks likes i won!")
        elif user_choice=="r" and pc_choice=="scissors":       
            await ctx.send(f"{ctx.author.mention} won!")

        elif user_choice=="p" and pc_choice=="scissors":
            await ctx.send("looks i won!")
            
        elif user_choice=="s" and pc_choice=="scissors":
            await ctx.send("it's tie!")      

def setup(client):
    client.add_cog(rps(client))