from bs4 import BeautifulSoup
import requests
from team_roster import *

def top_ten(category,Your_Team):
	# You have to chhose category - capital letters, and Team name in letter case
	# options are : ASSITS, BLOCKS, POINTS, STEALS, REBOUNDS ,
	# DEFENSIVE_REBOUNDS, OFFENSIVE_REBOUNDS , FREE_THROW_PERCENTAGE,
	# THREE_POINT_PERCENTAGE, FIELD_GOAL_PERCENTAGE
	
	team = roster(Your_Team)
	if category=="REBOUNDS":
		category = "TOTAL_REBOUNDS"
	source = requests.get('https://sports.yahoo.com/nba/stats/individual/?sortStatId='+category+'_PER_GAME&selectedTable=0/').text

	stats = BeautifulSoup(source,'lxml')
	players = stats.find_all('tr', attrs={'class':'Bgc(table-hover):h'})
	i = 1
	export_lst = []
	for player in players:
			player_name=player.th.div.a.text
			if (player_name not in team):
				export_lst.append(player_name)
			i += 1
			if i==21 or len(export_lst)==10:
				break
	print(export_lst)


