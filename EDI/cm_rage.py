#Rage command by Jordan
values = []
Members = []
#open existing file or create new one if not existing
file = open("Rages.txt", "w+")

readValues()
if (len(value) == 0)
    writeValues()
else
    for word in values
        Members.append(parseString(word))


def readValues()
    #reads file for current values
    for line in file
        values.append(line)

def writeValues()
    #writes back increment value for person who raged


def parseString(value)
    current = value.split(" ")
    mem = new Member()
    mem.name = current[0]
    mem.rageMeter = current[1]


class Member:
    def __init__(self):
        self.name = ""
        self.rageMeter = 0

