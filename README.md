# NoNameNeeded-bot
The Brand new NNN bot, which has a lot of features, more than you think!


# Source Code
You can use the source code to help you make commands that you want, please do not steal all of it and not credit us, since thats mean :)

# Development Branch
This branch is for beta commands and for members to post their code for the bot!

# Invite
We really would like it if you invite our bot No Name Needed, that helps out tons and makes me more motivated to make NNN Bot!

INVITE URL: https://discord.com/api/oauth2/authorize?client_id=786164164690706462&permissions=2147483639&scope=bot



# Praw Sample Code
<h3> Praw is used to web scrape reddit and in this we will give you code to scrape some reddit memes</h3>
<h4>This is for discord.py but can be changed</h4>

```#DISCORD.PY COGGED

from cogs.imports import *
import praw

reddit = praw.Reddit(
        client_id = "",
        client_secret = "", 
        username = "",
        password = "", 
        user_agent = ""
)

class meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["memes"])
    async def meme(self,ctx):
        if random.randint(1,2) == 1:
            subreddit = "dankmemes"
        else:
            subreddit = "memes"  

        subreddit = reddit.subreddit(subreddit)

        typess = ["top", "new", "hot"]

        types = random.choice(typess)

        all_subs = []

        if types == "top":
            typeOFREDDIT = subreddit.top(limit= 50)
            print("top")

        elif types == "new":
            typeOFREDDIT = subreddit.new(limit= 50)
            print("new")

        elif types == "hot":
            typeOFREDDIT = subreddit.hot(limit= 50)    
            print("hot")

        else:
            return await ctx.send("something went wrong")    
            raise Exception("Smth SUS happened")

        for submission in typeOFREDDIT:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)  
        if random_sub.over_18:
            await ctx.send("No, try again") 
        else:  
            name = random_sub.title
            url = random_sub.url

            embed = discord.Embed(title= name)

            await ctx.send(embed=embed)
            await ctx.send(url)  


def setup(client):
    client.add_cog(meme(client))
```
