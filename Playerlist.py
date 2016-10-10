from Team import *
from Summoner import *


class Playerlist:

	def __init__(self, count=0, teamSize=5):
		self.count = count
		self.players = list()
		self.teamSize = teamSize


	def addPlayer(self, username):
		self.players.append(Summoner(username))
		self.count += 1

	def removePlayer(self, username):
		for player in self.players:
			if username in self.username:
				self.players.remove(player)
				self.count -= 1
				return

	def createTeams(self):
		sort(self.players)
		self.extras = list()
		teams = makeTeams()
		return teams

	def __str__(self):
		for player in self.players:
			print(player)

	def makeTeams(self):
		extrasCount = self.count % self.teamSize
		numTeams = self.count / self.teamSize

		for i in range(0,extrasCount):
			random.seed(datetime.now())
			rNum = random.uniform(0,time.time()) % self.count
			self.extras.append(self.players[rNum])
			self.players.pop(rNum)

		teams = list()
		fullTeams = list()

		for i in range(0,self.count):
			if self.players[i].inTeam == False:
				#move full teams to full team list.
				for j in range(0,self.teamSize):
					if teams[j].count == self.teamSize:
						fullTeams.append(teams[j])
						teams.remove(j)

				spacefound = False

				for k in range(0, self.teamSize):
					if self.teamSize - teams[k].count >= 2:
						spacefound = True

				if spacefound | self.players[i].duo == None:
					jMin = 0
					jOldMin = 0

					for l in range(1,len(teams)):
						x = teams[jMin].mmr
						y = teams[l].mmr

						if(x < y):
							jOldMin = jMin;
							jMin = l

					teams[jMin].add(self.players(i))

				else:
					temp = list()
					for team in teams:
						temp.add(team)

					teamMin = 0
					teamMin2 = 0

					for m in range(1, len(temp)):
						hasNonDuo = False
						for player in temp[m].players:
							if player.duo == None:
								hasNonDuo = True

						if hasNonDuo:
							xx = temp[teamMin].mmr
							yy = temp[m].mmr
							zz = temp[teamMin2].mmr

							if yy < xx:
								teamMin2 = teamMin
								teamMin = k

					lowestTeam = temp[teamMin]
					secondLowest = temp[teamMin2]

					target = self.players[i].mmr
					closest = lowestTeam.count - 1

					for n in range(0, lowestTeam.count - 1):
						if lowestTeam.players[n].duo == None:
							diff = abs(lowestTeam.players[m].mmr - target)
							closeDiff = abs(lowestTeam.players[closest].mmr - target)
							if diff < closeDiff:
								closest = n

					moving = lowestTeam.players[closest]
					lowestTeam.remove(moving)
					moving.inTeam = False
					secondLowest.add(moving)

		if len(teams) > 0:
			for team in teams:
				fullTeams.append(team)

		return fullTeams
