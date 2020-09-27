import json
import requests

def player_stats(full_name,season=2019):
	first_name=full_name.split(' ')[0]
	last_name=full_name.split(' ')[1]
	player_json = requests.get(f'https://www.balldontlie.io/api/v1/players?search={first_name}%20{last_name}').json()
	if player_json['meta']['total_count'] == 1:
		player_id=player_json['data'][0]['id']
		player_team=player_json['data'][0]['team']['abbreviation']
		player_profile_json=requests.get(f'https://www.balldontlie.io/api/v1/players/{player_id}').json()
		player_position=player_profile_json['position']
		player_stats_json=requests.get(f'https://www.balldontlie.io/api/v1/season_averages?season={season}&player_ids[]={player_id}').json()
		try:
			player_stats_dict=player_stats_json['data'][0]
			player_profile_dict={'first_name':first_name, 'last_name':last_name,'Position':player_position,'Team':player_team}
			player_list=[player_profile_dict,player_stats_dict]
			return player_list
		except:
			return(f'{first_name} {last_name} didn not play in the NBA this season')

	elif player_json['meta']['total_count'] == 0:
		return(f'There is no player in the NBA named {full_name}')

def find_team_season_avg(team): #we have to pass team_dict
	teams_list=requests.get('https://www.balldontlie.io/api/v1/teams').json()['data']
	teams_dict={}
	for team in teams_list: #We can consider to change the for loop
			teams_dict[team['full_name']] = team['name']
	team_name= str.lower(teams_dict[team])
	teams_stats_json=requests.get(f'http://data.nba.net/json/cms/2019/statistics/{team_name}/regseason_stats_and_rankings.json').json()
	team_season_avg = teams_stats_json['sports_content']['team']['averages']
	rank_categories= teams_stats_json['sports_content']['team']['rankings']
	strong_categories=[]
	weak_categories=[]
	for category in rank_categories:
		if int(rank_categories[category][:-2]) < 4:
			strong_categories.append(category)
		elif int(rank_categories[category][:-2])>20:
			weak_categories.append(category)
	team_season_stats={'name':team, 'averages':team_season_avg, 'Strong Side':strong_categories, 'Weak Side': weak_categories}
	return team_season_stats

def roster(team):
	teams_list=requests.get('https://www.balldontlie.io/api/v1/teams').json()['data']
	teams_dict={}
	for team_i in teams_list: #We can consider to change the for loop
		teams_dict[team_i['full_name']] = team_i['name']
	team_name= str.lower(teams_dict[team])
	url = "http://data.nba.net/json/cms/noseason/team/"+(team_name)+"/roster.json"
	response = requests.request("GET", url)
	roster_list=[]
	data = json.loads(response.text)
	try:
	    players = data["sports_content"]["roster"]['players']['player']
	    if len(players) != 0:
	        for player in players:
	            first_name = player['first_name']
	            last_name = player['last_name']
	            full_name=first_name+' '+last_name
	            roster_list.append(full_name)
	        return(roster_list)
	except :
	    return ("No such a team")



#roster_list=roster("LA Clippers")
#player_stat=player_stats(roster_list[2],2019)
#print(player_stat)
