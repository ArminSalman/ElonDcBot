import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("token.env")

token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!elon ")

@bot.command()
async def say(ctx,*,arg="Bir metin giriniz"):
    if arg != "Bir metin giriniz":
        await ctx.send(arg)
        await ctx.message.delete()
    else:
        await ctx.reply(content=arg)

bot.run(token)
