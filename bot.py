import discord
from discord import app_commands
import random
from discord.ext import commands
import re
import os
from googletrans import Translator

MY_GUILD = discord.Object(id=INSERT GUILD ID)

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
translator = Translator()

furryImagesFolder = "INSERT PATH TO FURRY FOLDER"
furryFiles = os.listdir(furryImagesFolder)
nissanMurano = "INSERT PATH TO NISSAN MURANO FILES FOLDER"

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
async def gay_test(interaction: discord.Interaction):
    """Time to test your queerness!!"""
    i = random.randint(0, 100)
    if i <= 15:
        await interaction.response.send_message(f'youre straight :D')
    elif i <= 30:
        await interaction.response.send_message(f"bicurious... but still mostly straight :3")
    elif i <= 45:
        await interaction.response.send_message(f"mhh.. time to discover what omnisexual means!")
    elif i <=65:
        await interaction.response.send_message(f"ooo someone's bisexual/pansexual ;3")
    elif i <= 85:
        await interaction.response.send_message(f"closer to the same gender... but maybe if you get that one 10/10...")
    elif i <= 100:
        await interaction.response.send_message(f"that's it... you did it... you're homosexual :D")

@bot.tree.command()
async def japanese_check(interaction: discord.Interaction):
    """dont mind this, it's just a command to check the status of the translate API"""
    await interaction.response.send_message((await translator.translate("The quick brown fox jumps over the lazy dog.", dest="ja")).text)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    RNG=random.randint(0, len(responses)-1)

    miata_bot_present = re.search(r"\bmiat(a)?\s+bot\b", message.content, re.I)
    mx5_match = re.search(r"\bmx[^a-zA-Z]?5\b", message.content, re.I)
    miat_match = None if miata_bot_present else re.search(r"\bmiat(a)?\b", message.content, re.I)
    string_theory_match = re.search(r"(?=.*\bstring theory\b)", message.content, re.I)
    colon3_match = re.search(r":3|;3|:#", message.content, re.I)
    nissan_match= re.search(r"\bnissan\b", message.content, re.I)
    murano_match  = re.search(r"\bmurano\b", message.content, re.I)

    triggered_by_mention = bot.user in message.mentions
    triggered_by_keyword = miat_match or mx5_match

    if colon3_match and (triggered_by_mention or  triggered_by_keyword):
        random_furry_image = random.choice(furryFiles)
        random_furry_image_path = os.path.join(furryImagesFolder, random_furry_image)
        await message.reply("here's a goober for ya ;3c", file=discord.File(random_furry_image_path))
    
    elif  string_theory_match and (triggered_by_keyword or triggered_by_mention):
        await message.reply("i gotcha!", file=discord.File("INSERT PATH TO IMAGE", filename="stringtheory.png"))

    elif nissan_match and murano_match and (triggered_by_mention or triggered_by_keyword):
        randBool = bool(random.getrandbits(1))
        if randBool:    
            nissan_murano = discord.File(nissanMurano + "INSERT YOUR FIRST NISSAN MURANO IMAGE FILE NAME HERE")
        else: 
            nissan_murano = discord.File(nissanMurano + "INSERT YOUR SECOND NISSAN MURANO IMAGE FILE HERE")
        await message.reply("you have a weird obsession towards nissan to even know this one", file=nissan_murano)

    elif (triggered_by_mention or triggered_by_keyword) and not "http" in message.content:
        await message.add_reaction("INSERT YOUR EMOJI HERE")
        if random.randint(1, 50) == 50:
            await message.reply((await translator.translate(responses[RNG], dest="ja")).text, mention_author=triggered_by_mention)
        else:
            await message.reply(responses[RNG], mention_author=triggered_by_mention)
       

bot.run("INSERT YOUR BOT TOKEN HERE")

