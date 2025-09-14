import discord
from discord import app_commands
import random
from discord.ext import commands
import re
import os
from googletrans import Translator

MY_GUILD = discord.Object(id=INSERT GUILD ID HERE)

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.default()
intents.message_content = True  
bot = MyClient(intents=intents)

nissanMurano = "INSERT NISSAN MURANO FILE PATH HERE"

responses = [
    "Trump imposed tariffs on steel so that Mazda couldn't make the Miata in the United States in order to protect Mustang sales. #MiataFacts ",
    "If Mazda put the Skyactiv 2.5T engine in the Miata, BMW would be forced out of business overnight. #MiataFacts ",
    "The Mazda Miata was designed with stance in mind. That's why slammed Miatas corner faster. #MiataFacts ",
    "Did you know that Hillary Clinton forced Mazda to sell automatic versions of the Miata? #MiataFacts ",
    "Make sure you put a 'Shocker' sticker on your Miata, so people don't think you're gay! #MiataFacts ",
    "A lot of drivers make jokes about them, but true drivers know to respect the Miata. #MiataFacts ",
    "Miata is the best car with wheels and pop up headlights... Or not but still the best. #MiataFacts",    
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

@bot.tree.command()
async def japanese_check(interaction: discord.Interaction):
    """dont mind this, it's just a command to check the status of the translate API"""
    await interaction.response.send_message((await Translator().translate("The quick brown fox jumps over the lazy dog.", dest="ja")).text)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    miata_bot_present = re.search(r"\bmiat(a)?\s+bot\b", message.content, re.I)
    mx5_match = re.search(r"\bmx[^a-zA-Z]?5\b", message.content, re.I)
    miat_match = None if miata_bot_present else re.search(r"\bmiat(a)?\b", message.content, re.I)
    string_theory_match = re.search(r"(?=.*\bstring theory\b)", message.content, re.I)
    nissan_match= re.search(r"\bnissan\b", message.content, re.I)
    murano_match  = re.search(r"\bmurano\b", message.content, re.I)
    
    triggered_by_mention = bot.user in message.mentions
    triggered_by_keyword = miat_match or mx5_match
    default_triggers = triggered_by_mention or triggered_by_keyword
    
    async def FinalOutput(CurrentActiveReply, **file):
        if CurrentActiveReply:
            RandomWordExchange = CurrentActiveReply.split()
            for x in RandomWordExchange:
                if random.randint(1, 100) == 100:
                    RandomWordExchange[RandomWordExchange.index(x)] = "AAAA" 
            CurrentActiveReply = " ".join(RandomWordExchange)
            if random.randint(1, 20) != 20:
                await message.reply(CurrentActiveReply, **file)
            else:
                await message.reply((await Translator().translate(CurrentActiveReply, dest="ja")).text, **file)

    RNG=random.randint(0, len(responses)-1)

    if string_theory_match and default_triggers:
        await FinalOutput("i gotcha!", file=discord.File("INSERT STRING THEORY IMAGE HERE"))

    elif nissan_match and murano_match:
        randBool = bool(random.getrandbits(1))
        if randBool:    
            nissan_murano = discord.File(nissanMurano +"INSERT FIRST NISSAN MURANO IMAGE FILENAME HERE")
        else: 
            nissan_murano = discord.File(nissanMurano + "INSERT SECOND NISSAN MURANO IMAGE FILENAME HERE")
        await FinalOutput("you have a weird obsession towards nissan to even know this one", file=nissan_murano)

    elif default_triggers and not "http" in message.content:
        await message.add_reaction("INSERT REACTION EMOJI HERE")
        await FinalOutput(str(responses[RNG]))

bot.run("INSERT BOT TOKEN HERE")