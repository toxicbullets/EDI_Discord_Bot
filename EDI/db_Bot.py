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
    c.execute("SELECT * FROM rage")
    data = c.fetchall()
    return data;


def data_entry():
    c.execute("INSERT INTO stuff VALUES (145, '2017-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuff (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
                (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM stuff WHERE value = 8')
    for row in c.fetchall():
        print(row)

def del_and_update():
    c.execute('SELECT * FROM stuff')

    # c.execute('UPDATE stuff SET value = 99 WHERE value = 8')
    # conn.commit()
    # c.execute('SELECT * FROM stuff')
    # [print(row) for row in c.fetchall()]

    c.execute('DELETE FROM stuff WHERE value = 99')
    conn.commit()
    c.execute('SELECT * FROM stuff')
    [print(row) for row in c.fetchall()]

#read_from_db()
