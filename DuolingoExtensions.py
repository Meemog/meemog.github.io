import duolingo
import time
import json

def GetPoints():
    lingo = duolingo.Duolingo("osk73080", "DefaultPassword")

    data = lingo.get_leaderboard("month", time.time())
    scoresDictionary = {}
    for item in data:
        username = item["username"]
        score = item["points"]
        scoresDictionary[username] = score
    return scoresDictionary
    
def DumpData(scores):
    with open('scores.json', 'w') as fp:
       json.dump(scores, fp)


DumpData(GetPoints())