import db_Bot
#Rage command by Jordan


def duckShoot(ctx):
    name = ctx.message.author.name
    db_Bot.create_duck_table(ctx)
    return db_Bot.incrementBang(name)

def duckFriend(ctx):
    name = ctx.message.author.name
    db_Bot.create_duck_table(ctx)
    return db_Bot.incrementBef(name)

def leaderboards(ctx):
    db_Bot.create_duck_table(ctx)
    return db_Bot.DuckLeaderboards()

