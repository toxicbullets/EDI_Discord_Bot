#EDI by Jordan
import discord
import threading
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time
import cm_rage
import cm_duck
import cm_league

duck = False
bot = commands.Bot(command_prefix='#')
channel = None


@bot.event
async def on_ready():
    print("Ready when you are")

#Commands

#Info Commands
#************************************************************************************************************************************************

#called using #info @"Username"
#Returns the information about the entered User
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title = "{}'s info".format(user.name), description= "Here's what I could find.", color = 0x00ff00)
    embed.add_field(name= "Name", value= user.name, inline = True)
    embed.add_field(name= "ID", value= user.id, inline = True)
    embed.add_field(name= "Status", value= user.status, inline = True)
    embed.add_field(name= "Highest Role", value= user.top_role, inline = True)
    embed.add_field(name= "Joined", value= user.joined_at, inline = True)
    embed.set_thumbnail(url= user.avatar_url)
    await bot.say(embed = embed)

#called using #serverinfo
#Returns the server information
@bot.command(pass_context = True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description = "Here's what I could find", color = 0x00ff00)
    embed.add_field(name= "Name", value= ctx.message.server.name, inline = True)
    embed.add_field(name= "ID", value= ctx.message.server.id, inline = True)
    embed.add_field(name= "Roles", value=len(ctx.message.server.roles), inline = True)
    embed.add_field(name= "Members", value= len(ctx.message.server.members), inline = True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed = embed)


#Action Commands
#************************************************************************************************************************************************

#called using #Rage @Username
#Increments rage score and returns the users current score
@bot.command(pass_context= True)
async def Rage(ctx, user: discord.Member):
    num = cm_rage.Raged(ctx, user)
    await bot.say("{} has Rage Quit {} times".format(user.name, num[1]))

#called using #RageScore
#Returns the leaderboards for the rage scores in the database
@bot.command(pass_context = True)
async def RageScore(ctx):
    embed = discord.Embed(title="{}'s Rage Leaderboards".format(ctx.message.server.name), description = "Here are the scores:", color = 0x00ff00)
    results = cm_rage.leaderboards(ctx)
    formatted = ""
    for values in results:
        formatted += '{:12}   {:>4} Rages\n'.format(str(values[0]), str(values[1]))
        print(formatted)
    embed.add_field(name= "Leaderboard", value = formatted, inline = True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed = embed)
 
#Call with #Poking
# Returns an inside joke with its corresponding video
@bot.command(pass_context = True)
async def Poking(ctx):
    #embed = discord.Embed(title="I Was Just Poking", description = "https://www.youtube.com/watch?v=eBSzO29pUK0", color = 0x00ff00)
    await bot.send_message(ctx.message.channel, '**I Was Just Poking** ', tts = True)
    await bot.say("https://www.youtube.com/watch?v=eBSzO29pUK0")



#called by using #kick @"Username"
#kicks user in the caller has a Admin role
@bot.command(pass_context=True)
@commands.has_role("root")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya Creep!".format(user.name))
    await bot.kick(user)

#called with #Bang  Shoots duck is there is one
@bot.command(pass_context=True)
async def Bang(ctx):
    global duck
    if duck:
        value = cm_duck.duckShoot(ctx)
        await bot.say("{} has shot {} ducks".format(value[0], value[1])) 
        duck = False
    else:
        await bot.say("Why are you shooting? There are no ducks here you creep")

#called with #Bef   Befriends duck is there is one
@bot.command(pass_context=True)
async def Bef(ctx):
    global duck
    if duck:
        value = cm_duck.duckFriend(ctx);
        await bot.say("{} has befriended {} ducks".format(value[0], value[2]))   
        duck = False
    else:
        await bot.say("You can befriend a duck that doesn't exist. Are you crazy?")

#called using #DuckScore
#Returns the leaderboards for the duck scores in the database
@bot.command(pass_context = True)
async def DuckScore(ctx):
    embed = discord.Embed(title="{}'s Duck Leaderboards".format(ctx.message.server.name), description = "Here are the scores:", color = 0x00ff00)
    results = cm_duck.leaderboards(ctx)
    formatted = ""
    for values in results:
        formatted += '{:10} {:>4} ducks shot {:>4} ducks befriended\n'.format(str(values[0]), str(values[1]), str(values[2]))
    embed.add_field(name= "Leaderboard", value = formatted, inline = True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed = embed)

#loops the duck spawning system
async def background_loop():
    await bot.wait_until_ready()
    channel = bot.get_channel("266335971606265857")
    print(channel)
    while not bot.is_closed:
        value = random.randint(0,10)
        print("Quack " + str(value))
        if value == 1:
            global duck
            duck = True 
            await bot.send_message(channel, "....Quack 🦆")
        await asyncio.sleep(120)

bot.loop.create_task(background_loop())


#Web Accessing Commands
#************************************************************************************************************************************************
#called using #DuckScore
#Returns the leaderboards for the duck scores in the database
@bot.command()
async def LeagueStats(userID : str):
    results = cm_league.getLeagueStats(userID)
    if results == None:
        print("Error with stats")
        await bot.say("Invalid Summoner Name")
        return None
    embed = discord.Embed(title="{}'s League Stats".format(userID), description = "Here are the numbers:", color = 0x00ff00)
    embed.add_field(name= "Account Level", value = str(results[0]), inline = True)
    embed.add_field(name= "Summoner ID", value = str(results[1]), inline = True)
    embed.set_thumbnail(url= "https://avatar.leagueoflegends.com/na/" + userID + ".png")
    if len(results) != 2:
        embed.add_field(name= "Rank", value = str(results[2]), inline = True)
        embed.add_field(name= "Division", value = str(results[3]), inline = True)
        embed.add_field(name= "League Points", value = str(results[4]), inline = True)
        embed.add_field(name= "Win Rate", value = "{0:.2f}".format(results[5]), inline = True)
    await bot.say(embed = embed)





bot.run("Mzk4OTYwNTk5OTIyNTA3Nzc2.DTGJTg.JelJeOhrlz5MJ7fEgIC7XvFSg8o")


