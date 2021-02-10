import duolingo
import time

def GetPoints():
    lingo = duolingo.Duolingo("osk73080", "DefaultPassword")

    data = lingo.get_leaderboard("month", time.time())
    pointsArray = []

    for item in data:
        tempDict = {}
        tempDict["Name"] = item["username"]
        tempDict["Score"] = item["points"]
        pointsArray.append(tempDict)
    return pointsArray
    

print(GetPoints())
