#ALL THE COMMANDS FOR THE BOT ARE IN FUNCTIONS/MAIN!!!!
#SEE EACH FILE THERE FOR COMMENTS ON HOW EACH COMMAND WORKS
#partner = person user married

#SEE database explain.txt for info on how stuff is stored in the database
import discord
import os #to get the token
import sys #to check arguments

try: #see if there is a noWebServer flag
    if sys.argv[1] == '-noWebServer':
        print('Keepalive disabled!')
except IndexError:
    from threading import Thread #to keep the repl from dying
    def keepalive(): #             ^^
        os.system('node keepalive.js')
    keepAliveThread = Thread(target=keepalive)
    keepAliveThread.start() #start the thread
    print('Keepalive started! Make sure to ping it! See README.md for info')
#now acutally get into running the bot
from discord.ext import commands

import settings

#load cogs, load intents etc.
intents = discord.Intents.all()

#see each command file with comments in Functions/folder/comamnd.py
#Admins folder is ignored as it isn't used
#Main folder if for the marriage stuff
cogs: list = ["Functions.Main.m", "Functions.Main.d","Functions.Main.t","Functions.Main.ad","Functions.Main.e","Functions.Main.do", "Functions.Main.help", "Functions.Main.mp", "Functions.Main.c"]

#client init...
client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            #I mean load cogs NOW
            print(f"Loading cog {cog}")
            client.load_extension(cog)
            print(f"Loaded cog {cog}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))
try: #attempt to get token and run bot
    token = os.environ['BOT_TOKEN']
    client.run(token)
except: #key not found
    raise KeyError('Could not find bot token. Did you forget to add the enviroment secret BOT_TOKEN?')