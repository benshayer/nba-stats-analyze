from bs4 import BeautifulSoup
import requests

source = requests.get('https://sports.yahoo.com/nba/stats/individual/?sortStatId=TOTAL_REBOUNDS_PER_GAME&selectedTable=0/').text

stats = BeautifulSoup(source,'lxml')

players = stats.find_all('tr', attrs={'class':'Bgc(table-hover):h'})
for player in players:
		player_name=player.th.div.a.text
		print(player_name)