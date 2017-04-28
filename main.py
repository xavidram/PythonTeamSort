from models.Playerlist import *
import time

def main():
	with open("players.txt", 'r') as f:
		players = f.readlines()

	PlayerList = Playerlist()

	#users that were not found in riot database
	errorUsers = list()

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
			errorUsers.append(e)
			print(str(e))
	
	if len(errorUsers) > 0:
		print("Players not found in Riot Database for North America:")
		with open("ErrorUsers.txt",'w') as errUsr:
			for p in errorUsers:
				print(p)
				errUsr.write(str(p) + '\n')

	#Create the Teams
	PlayerList.createTeams()

	print("Teams:")
	print("-----------------------")

	#print out all the teams
	PlayerList.printTeams()
	#convert output to csv
	PlayerList.toCsv()

if __name__ == '__main__':
	main()