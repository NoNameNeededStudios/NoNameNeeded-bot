from cogs.imports import *

class command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball", "eightbal"])
    async def eightball(self,ctx,*,question):
        if question == "hi":
            responses =  f"hello there {ctx.author.name} <:minecraftheart:795035007533842442> !" or f"hi there <:minecraftheart:795035007533842442>"
            response = random.choice(responses)

        elif "gay" in question:
            responses = f"well...i mean, are you gay?" or "maybe..", "yes", "nahahahah"
            response = random.choice(responses)

        elif "really" in question:
            responses = f"Eehhh, yea..sorry or..not" or "lol yep"
            response = random.choice(responses)

        elif "boobs" in question:
            responses = f"<:minecraftheart:795035007533842442> well...i dont succ on them tittes <:minecraftheart:795035007533842442>", "yes this dose get repeated, too lazy"
            response = random.choice(responses)

        elif "bye" in question:
            responses = [f"well...penis, lol" or "welp bye"]
            response = random.choice(responses)
        else:
            LOR=  ["eello...penis, lol", "nope", "is uno mars is gay?", "harder daddy", "no im not gay", "yes i am answerinig with things not related to what you are saying", "and here is me, ignoring you", "come milk my tites", "nope, i would lick banana", "oooooo nice", "ew", "yes 100%", "tf no"]  

            response = random.choice(LOR)

        embed = discord.Embed(title="Eight Ball", description=response, colour=discord.Colour.random())      
        await ctx.send(embed=embed)         


def setup(client):
    client.add_cog(command(client))