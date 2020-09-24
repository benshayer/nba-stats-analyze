import json
import requests

#team_choice = input('Enter your team:')
teams_rosters={}
problem=[]
total_pages=requests.get('https://www.balldontlie.io/api/v1/players').json()['meta']['total_pages']
for i in range(1,total_pages+1):	
	try:
			players_json = requests.get('https://www.balldontlie.io/api/v1/players',params={'page': i}).json()
			print(i)
	except:
		pass
	for player in players_json['data']:
		player_id=player['id']
		team_name=player['team']['full_name']
		if team_name in teams_rosters:
			teams_rosters[team_name].append(player_id)
		else:
			teams_rosters[team_name]=[player_id]
print(teams_rosters)