import duolingo
import time
lingo = duolingo.Duolingo("osk73080", "DefaultPassword")

data = lingo.get_leaderboard("month", time.time())

for item in data:
    username = item["username"]
    score = item["points"]
    print("%20s: %5d" % (username, score))