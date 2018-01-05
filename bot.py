#EDI by Jordan

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("Ready when you are")

#Commands
#called using #ping
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!!")

#called using #info @"Username"
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The username is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

#called by using #kick @"Username"
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya Creep!".format(user.name))
    await bot.kick(user)

bot.run("Mzk4OTYwNTk5OTIyNTA3Nzc2.DTGJTg.JelJeOhrlz5MJ7fEgIC7XvFSg8o")

