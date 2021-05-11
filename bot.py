import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3

dataBase = sqlite3.connect("token.db")
cursor = dataBase.cursor()

query = "Select * from token"
cursor.execute(query)
datas = cursor.fetchone()
data = str(datas[0])

token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!elon ")

@bot.command()
async def say(ctx,*,arg="Bir metin giriniz"):
    if arg != "Bir metin giriniz":
        await ctx.send(arg)
        await ctx.message.delete()
    else:
        await ctx.reply(content=arg)

bot.run(data)
