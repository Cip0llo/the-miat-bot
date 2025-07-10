import discord
import random
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

responses = [
    "Trump imposed tariffs on steel so that Mazda couldn't make the Miata in the United States in order to protect Mustang sales. #MiataFacts ",
    "If Mazda put the Skyactiv 2.5T engine in the Miata, BMW would be forced out of business overnight. #MiataFacts ",
    "The Mazda Miata was designed with stance in mind. That's why slammed Miatas corner faster. #MiataFacts ",
    "Did you know that Hillary Clinton forced Mazda to sell automatic versions of the Miata? #MiataFacts ",
    "Make sure you put a 'Shocker' sticker on your Miata, so people don't think you're gay! #MiataFacts ",
    "A lot of drivers make jokes about them, but true drivers know to respect the Miata. #MiataFacts ",
    "Did you know that the Miata is more environmentally friendly than a Prius? #MiataFacts ",
    "The Mazda MX-5 is literally the best drivers' car in history, hands down. #MiataFacts ",
    "Acceleration is only needed if you have to slow down for corners. #MiataFacts ",
    "Did you know that the Miata is the only car that works on girls? #Niceguy #MiataFacts ",
    "The 2017 Miata is slower to 60 than a 2017 V6 Camry. Right. #FakeNews #MiataFacts ",
    "A Miata with good tires will win literally any track day ever. #MiataFacts ",
    "The 2019 Mazda 3 is literally just a more practical MX-5. #MiataFacts ",
    "Better to be slow car fast than fast car slow! #MiataFacts ",
    "A roll cage legally makes a Miata a race car. #MiataFacts ",
]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    miata_bot_present = re.search(r"\bmiat(a)?\s+bot\b", message.content)

    mx5_match = re.search(r"\bmx[^a-zA-Z]?5\b", message.content)

    miat_match = None if miata_bot_present else re.search(r"\bmiat(a)?\b", message.content)

    triggered_by_mention = bot.user in message.mentions
    triggered_by_keyword = miat_match or mx5_match

    if triggered_by_mention or triggered_by_keyword:
        await message.reply(responses[ random.randint(0, len(responses)-1)], mention_author=triggered_by_mention)
        await message.add_reaction("<:mazdamiata:1392566131558056038>")

    await bot.process_commands(message)