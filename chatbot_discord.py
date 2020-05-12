import discord
import asyncio
from discord.ext import commands
import main2_chatbot

#TOKEN DU BOT DISCORD
TOKEN = 'entrer_your_token_here'

#PREFIX POUR DONNER UNE REQUETE AU BOT | ICI IL N Y EN A PAS VOLONTAIREMENT
bot = commands.Bot(command_prefix="")

#MISE EN LIGNE DU BOT | RENVOIE DANS LA CONSOLE LORSQUE CELUI EST EN LIGNE
@bot.event
async def on_ready():
    print("Bot en ligne")


#RENVOIE D UN MESSAGE DANS LE CHANNEL DISCORD CORRESPONDANT | L INPUT COMPREND LE MESSAGE ET LE CHANNEL
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return ""
    else:
        await message.channel.send(main2_chatbot.chat(str(message.content.lower())))

#RUN DU BOT
try:
    bot.run(TOKEN)
except keybordInterrupt:
    print("")
