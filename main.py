from Playerlist import *
import time

with open("players.txt", 'r') as f:
	players = f.readlines()

PlayerList = Playerlist()

#for player in players:
#	print(player)
#	PlayerList.addPlayer(player.strip('\n'))
j = 0
for player in players:
	#make sure we dont exceed request limit from temp api
	if(j<5):
		j += 1
	else:
		j = 0
		time.sleep(15)

	# try and catch any errors requesting info from RIOT API
	try:
		PlayerList.addPlayer(player.strip('\n'))
	except Exception as e:
		print(str(e))


#PlayerList.printList()
teams = PlayerList.createTeams()

print("Teams\n")
PlayerList.printTeams()
PlayerList.toCsv()