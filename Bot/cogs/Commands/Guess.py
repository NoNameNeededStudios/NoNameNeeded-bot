from cogs.imports import *


class Guess(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["guess"])
    async def Guess(self,message, *, PlayerGuess:int, name="playerguess"):
        CPUGUESS = random.randint(1,10)
    

        #!Unless its Less than 1 and more than 10
        if PlayerGuess > 10:
            await message.send("Sorry its only between 1-10!")
        if PlayerGuess < 1:
            await message.send("Sorry its only between 1-10!")    
        


        if PlayerGuess < 11 and PlayerGuess > 0:

            sleep(0.4)
            await message.send(f"Your Guess: **{PlayerGuess}**")
            sleep(0.6)    
            await message.send(f"My Number was : **{CPUGUESS}**")
            sleep(0.5)
            #*if CPU Won
            if PlayerGuess != CPUGUESS:
                await message.send("That Means **i won**.**GG**")
                #*if Player Won
            if PlayerGuess == CPUGUESS:
                await message.send("That Means **you won**.**GG**")


def setup(client):
    client.add_cog(Guess(client)) 