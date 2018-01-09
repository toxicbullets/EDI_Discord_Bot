import requests

payload = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": "INSERTAPIKEYHERE",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 OPR/49.0.2725.64"
}
def getLeagueStats(username):
    accInfo = getSumAccInfo(username)
    if accInfo == None:
        print("Couldn't find account info")
        return None
    level = accInfo['summonerLevel']
    sumID = accInfo['id']
    print(sumID)
    rankedData = requestRankedData(sumID)
    if not rankedData:
        return [level, sumID]
    rankedInfo = rankedData[0]
    tier = rankedInfo['tier']
    rank = rankedInfo['rank']
    lp = rankedInfo['leaguePoints']
    winRate = float(rankedInfo['wins']) / float(rankedInfo['losses'])
    results = [level, sumID, tier, rank, lp, winRate]
    return results


def requestRankedData(ID):
    URL = "https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/" + str(ID)
    response = requests.get(URL, headers =payload)
    print(response.status_code)
    if response.status_code != 200:
        return None
    return response.json()

def getSumAccInfo(summonerName):
    URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName
    response = requests.get(URL, headers = payload)
    if response.status_code != 200:
        return None
    return response.json()

