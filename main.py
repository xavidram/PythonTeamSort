from Playerlist import *
import time

with open("players.txt", 'r') as f:
	players = f.readlines()

PlayerList = Playerlist()

#for player in players:
#	print(player)
#	PlayerList.addPlayer(player.strip('\n'))

j = 0
for i in range(0,len(players)):
	if(j < 10):
		j += 1
		#print(players[i])
		try:
			PlayerList.addPlayer(players[i].strip('\n'))
		except Exception as e:
			print(str(e))
	else:
		j = 0
		time.sleep(10)

#PlayerList.printList()
teams = PlayerList.createTeams()