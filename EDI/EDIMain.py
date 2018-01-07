#EDI by Jordan
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import cm_rage

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("Ready when you are")

#Commands

#Info Commands

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
 

@bot.command(pass_context = True)
async def Poking(ctx):
    #embed = discord.Embed(title="I Was Just Poking", description = "https://www.youtube.com/watch?v=eBSzO29pUK0", color = 0x00ff00)
    await bot.say("**I Was Just Poking** \n https://www.youtube.com/watch?v=eBSzO29pUK0")
    


#called by using #kick @"Username"
#kicks user in the caller has a Admin role
@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya Creep!".format(user.name))
    await bot.kick(user)




bot.run("Mzk4OTYwNTk5OTIyNTA3Nzc2.DTGJTg.JelJeOhrlz5MJ7fEgIC7XvFSg8o")

