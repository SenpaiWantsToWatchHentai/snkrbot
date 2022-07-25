import os 
import discord, requests, itertools

from dotenv import load_dotenv 
from nike_module import get_nike_shoes, get_links

# An object that represents a connection to Discord  (i.e. session)
client = discord.Client()  
# Nike SNKRS Lauch Calendar
NIKE_SNKRS_URL = 'https://heat-mvmnt.de/releases' 
# Create a Session
s = requests.Session() 
# Create a Response
r = s.get(NIKE_SNKRS_URL) 

# Functions 
@client.event 
async def on_ready(): 
    '''Event Handler: Handles the event when the client 
    has established a connection to Discord.'''
    print(f'{client.user} has connected to Discord!') 

@client.event
async def on_message(message): 
    '''Bot replies back with sneaker info when it sees a command.'''

    # Ignore messages from the bot itself.
    if message.author == client.user:
        return

    # !nike -> Give first five sneakers from Nike Launch Calendar
    if message.content.startswith('!nike'): 
        # Check if the site is up
        if r.ok:
            shoes = get_nike_shoes()  # List of shoes and releases
            links = get_links()  # List of Links to shoes
            bot_message = ''  # The message the bot will send in chat

            for shoe, link in zip(shoes, links): 
                bot_message += shoe + '\n' + link + '\n\n'

            bot_message += 'For more Nike releases: ' + NIKE_SNKRS_URL
            await message.channel.send(bot_message) 
        else: 
            await message.channel.send('Nike site is down.')

if __name__ == '__main__':
    # Loads env variables from .env to shell's env variables
    load_dotenv()  
    # Gets the token which 
    token = os.getenv('DISCORD_TOKEN') 
    # Runs Client/session using bot's token
    client.run(token)
