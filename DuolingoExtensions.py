import duolingo
import time
import flask
from flask import request, jsonify

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
    
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>If you are seeing this...</h1>
<p>That means it works</p>'''

@app.route('/test/all', methods=['GET'])
def AllPointpage():
    scores = GetPoints()
    return jsonify(scores)

@app.route('/test/specific', methods=['GET'])
def SpecificPointPage():
    scores = GetPoints()
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No id specified"

    results = []

    for entry in scores:
        if entry["Name"] == name:
            results.append(entry)
    return jsonify(results)

if __name__ == '__main__':
    app.run()