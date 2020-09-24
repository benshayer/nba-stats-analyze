import json
import requests

teams_list=requests.get('https://www.balldontlie.io/api/v1/teams').json()['data']
teams_dict={}
for team in teams_list:
	teams_dict[team['full_name']] = team['name']


def find_team_season_avg(team):
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

clippers_stats=find_team_season_avg('New York Knicks')
print(clippers_stats)