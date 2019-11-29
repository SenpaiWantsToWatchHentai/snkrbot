import os 
import discord 

from dotenv import load_dotenv 

# An object that represents a connection to Discord  (i.e. session)
client = discord.Client()  

# Functions 
@client.event 
async def on_ready(): 
    '''Event Handler: Handles the event when the client 
    has established a connection to Discord.'''
    print(f'{client.user} has connected to Discord!') 

@client.event
async def on_message(message): 
    '''Bot replies back with hello when it sees hello.'''

    # Ignore messages from the bot itself.
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
# Loads env variables from .env to shell's env variables
load_dotenv()  
# Gets the token which 
token = os.getenv('DISCORD_TOKEN') 

# Runs Client/session using bot's token
client.run(token)