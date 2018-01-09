import sqlite3
import time
import datetime
import random
import discord

conn = sqlite3.connect('Normandy.db')
c = conn.cursor()

def create_table(ctx):
    c.execute('CREATE TABLE IF NOT EXISTS rage(person TEXT, num INTEGER)')
    c.execute('SELECT * FROM rage')
    print("Start Adding")
    if not c.fetchall():
        print("Fetch empty")
        print(len(ctx.message.server.members))
        for members in ctx.message.server.members:
            print(members.name)
            c.execute("INSERT INTO rage(person, num) VALUES (?, ?)",(members.name, 0))
            conn.commit()
            


def incrementRage(name):
    c.execute("SELECT * FROM rage WHERE person LIKE '{}'".format(name))
    data = c.fetchone()
    print(data)
    if not data:
        c.execute("INSERT INTO rage VALUES (?, ?)", (name, 1))
        conn.commit()
        data = [name, 1]
        return data;
    else:
        altered = [name, data[1] + 1]
        print(altered)
        c.execute("UPDATE rage SET num = (?) WHERE person like '{}'" .format(altered[0]),(altered[1],))
        conn.commit()
        return altered

def RageLeaderboards():
    c.execute("SELECT * FROM rage ORDER BY num DESC")
    data = []
    for values in c.fetchall():
        data.append(values)
    return data


def create_duck_table(ctx):
    c.execute('CREATE TABLE IF NOT EXISTS duck(person TEXT, bang INTEGER, bef INTEGER)')
    c.execute('SELECT * FROM duck')
    if not c.fetchall():
        print("Fetch empty")
        print(len(ctx.message.server.members))
        for members in ctx.message.server.members:
            c.execute("INSERT INTO duck(person, bang, bef) VALUES (?, ?, ?)",(members.name, 0, 0))
            conn.commit()

def incrementBef(name):
    c.execute("SELECT * FROM duck WHERE person LIKE '{}'".format(name))
    data = c.fetchone()
    if not data:
        c.execute("INSERT INTO duck VALUES (?, ?, ?)", (name, 0, 1))
        conn.commit()
        data = [name, 0, 1]
        return data;
    else:
        altered = [name,data[1], data[2] + 1]
        print(altered)
        c.execute("UPDATE duck SET bef = (?) WHERE person like '{}'" .format(altered[0]),(altered[2],))
        conn.commit()
        return altered

def incrementBang(name):
    c.execute("SELECT * FROM duck WHERE person LIKE '{}'".format(name))
    data = c.fetchone()
    print(data)
    if not data:
        c.execute("INSERT INTO duck VALUES (?, ?, ?)", (name, 1, 0))
        conn.commit()
        data = [name, 1, 0]
        return data;
    else:
        altered = [name, data[1] + 1, data[2]]
        print(altered)
        c.execute("UPDATE duck SET bang = (?) WHERE person like '{}'" .format(altered[0]),(altered[1],))
        conn.commit()
        return altered


def DuckLeaderboards():
    c.execute("SELECT * FROM duck ORDER BY bang DESC")
    dataBef = []
    dataBang = []
    for values in c.fetchall():
        dataBang.append(values)
    c.execute("SELECT * FROM duck ORDER BY bef DESC")
    for values in c.fetchall():
        dataBef.append(values)
    data = [dataBang,dataBef]
    return data