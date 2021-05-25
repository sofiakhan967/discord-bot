import discord
from discord import message
import random
from discord.ext import commands

token=('ENTER YOUR TOKEN HERE')

words=['hi','hello','whatsup','good to see you']
reply=['hi', 'hello' , 'good to see you too', 'hey buddy', 'much better','its been a long day ']
intents=discord.Intents.default()
intents.members=True
#intents=intents
client=commands.Bot(command_prefix="." ,intents=intents)
@client.event
async def on_ready():
    print(f"{client.user} has been connected succesfully")

@client.command()
async def hello(ctx):
    await ctx.send('hi')

    #WELCOMING NEW MEMBERS ON SERVER 
@client.event
async def on_member_join(member):
    guild=client.get_guild(841419937256046613) #server id
    channel=guild.get_channel(841419937708245024) #channel id
    await channel.send(f'{member.mention} welcome to server ! :partying_face:') #welcome member on server
    await member.send(f'welcome to {guild.name} server , {member.mention} , :partying_face:') #welcome msg DM

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any (word in message.content for word in words):
        await message.channel.send(random.choice(reply))
client.run(token)    
