from cogs.imports import *
import praw


reddit = praw.Reddit(client_id = "7490cg5jBMcKVQ",
        client_secret = "S3eOr7DFAjsTUQGklyY6oncIXmaS3g", username = "VoidyDEV",
        password = "3Ybwp+4mFkCLBJ(", user_agent = "pythonpraw")

class SubRedditScrapper(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=["r/", "reddit/"])
    async def r(self,ctx, subreddit=None,types=None):
        subreddit = reddit.subreddit(subreddit)

        if subreddit == None:
            await ctx.send("Please tell me a subreddit, and where in that sub reddit, e.g: `n!r memes top`")
        elif types== None:
            await ctx.send(f"Please tell me where you want to find a post in {subreddit} , e.g: `n!r memes top`")
        else:

                    typess = ['top', 'new', 'hot']
                   
                    bad_subs = ["porn", "sex", "dick", "cock", "fuck", "pussy", "boobs", "dicks", "cocks", "boob", "vegina", "Sex", "Porn", "Dick", "Cock", "Dicks", "Boobs", "Boob", "Pussy", "Vegina", "Cocks"]

                    if types not in typess:
                        await ctx.send("Please use `top`, `new` or `hot`")
                    elif subreddit in bad_subs:
                        await ctx.send("naughty naughty, and no")    
                    else:    
                        all_subs = []
                        typeOFREDDIT = subreddit.top(limit= 50)

                        for submission in typeOFREDDIT:
                            all_subs.append(submission)

                        random_sub = random.choice(all_subs)  

                        name = random_sub.title
                        url = random_sub.url

                        embed = discord.Embed(title= name)
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)  

    @commands.command(aliases=["r/search", "reddit/search"])
    async def VMKSwmwfjuwi(self,ctx,subreddit=None,*,what_to_search_for=None):
        subreddit = reddit.subreddit(subreddit)

        if subreddit == None:
            await ctx.send("Please tell me a subreddit, and where in that sub reddit, e.g: `n!r/search minecraft desert`")
        elif what_to_search_for== None:
            await ctx.send(f"Please tell me what to find in {subreddit}")
        else:
                    bad_subs = ["porn", "sex", "dick", "cock", "fuck", "pussy", "boobs", "dicks", "cocks", "boob", "vegina", "Sex", "Porn", "Dick", "Cock", "Dicks", "Boobs", "Boob", "Pussy", "Vegina", "Cocks"]

                   
                    if subreddit in bad_subs:
                        await ctx.send("naughty naughty, and no")  
                    elif what_to_search_for in bad_subs:
                        await ctx.send("naughty naughty, and no")   
                    else:
                        all_subs = []
                        for submission in reddit.subreddit("all").search(f"{subreddit} {what_to_search_for}"):
                            all_subs.append(submission)

                        random_sub = random.choice(all_subs)  

                        name = random_sub.title
                        url = random_sub.url

                        embed = discord.Embed(title= name)
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)  

         






def setup(client):
    client.add_cog(SubRedditScrapper(client))
