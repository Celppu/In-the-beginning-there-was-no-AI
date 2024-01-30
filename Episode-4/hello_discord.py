# For AI-course 
# Date of creation: 2024-01-30

# Import discord.py to access Discord's API
import discord

# Create an instance of a client (bot)intents = discord.Intents.default()
intents = discord.Intents.default() 
# NOTE: Old tutorials do not have the intents parameter
#      If you get an error, try the following instead:
bot = discord.Client(intents=intents)

# Event listener for when the bot is ready (online)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Event listener for when a new message is sent to a channel
@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # Check if the message contains 'hello' (case-insensitive)
    if 'hello' in message.content.lower():
        # Send a friendly response to the channel
        await message.channel.send('Hello there! Hope you are having a great day 😊')

# Run the bot with your bot token
bot.run('YOUR_BOT_TOKEN')
