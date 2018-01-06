import db_Bot
#Rage command by Jordan


def Raged(ctx, user):
    name = user.name
    db_Bot.create_table(ctx)
    return db_Bot.incrementRage(name)

def leaderboards(ctx):
    db_Bot.create_table(ctx)
    return db_Bot.RageLeaderboards()

