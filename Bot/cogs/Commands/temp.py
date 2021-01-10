from cogs.imports import *

class Temp(commands.Cog):

    def __init__(self, client):
        self.client = client


    
    @commands.command(aliases=["Temperature", "temperature"])
    async def temp(self,ctx, *,city_):
        """To find out the temperature of a city"""

        city = city_
        url = 'http://api.openweathermap.org/data/2.5/weather?q={str(city)}&appid=ac7c75b9937a495021393024d0a90c44&units=metric'

        try:
            async with aiohttp.ClientSession()as cs:
                res = await cs.get(f'http://api.openweathermap.org/data/2.5/weather?q={str(city)}&appid=ac7c75b9937a495021393024d0a90c44&units=metric')
                data = await res.json()
                temp = data['main']['temp']
                wind_speed = data['wind']['speed']
                latitude = data['coord']['lat']
                longitude = data['coord']['lon']
                descriptions = data['weather'][0]['description']
                embed = discord.Embed(
                title=f"Temperature of {city}", description=f"Temperature = {temp}°C", color=discord.Color.blurple())
                embed.add_field(name='Wind Speed',value=f' {wind_speed} m/s')
                            
                            
                            
                embed.add_field(name='Latitude', value=f' {latitude}')
                embed.add_field(name='Longitude', value=f' {longitude}')

                embed.add_field(name='Description',value=f' {descriptions}')

                await ctx.send(embed=embed)

        except Exception:
            embed = discord.Embed(
                title=f"Error", description=f"Command Failed, Reason: Invaild City name | Or API Does not understand", color=discord.Color.blurple())

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Temp(client))