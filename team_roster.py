import requests
import json

def roster(teamname):
    url = "http://data.nba.net/json/cms/noseason/team/"+(teamname)+"/roster.json"

    response = requests.request("GET", url)

    data = json.loads(response.text)
    try:
        data2 = data["sports_content"]["roster"]['players']['player']
        if len(data2) != 0:
            for d in data2:
                first_name = d['first_name']
                last_name = d['last_name']
                print(first_name, last_name)
    except :
        print("No such a team")


roster("lakers")