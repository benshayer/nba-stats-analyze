import json
import requests
full_name='Jayson Tatum'
team='DAL'
def player_stats(full_name,season):
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


#tatum_list=player_stats(full_name,2017)
#print(tatum_list)