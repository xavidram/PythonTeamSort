from requests import *
import json


## GLOBALS ##
REGION = "na" #NA by default, can be changed
URL = "https://" + REGION + ".api.pvp.net"
APIKEY = "User API KEY HERE"
RateLimit_perMin = "500" #500 Requests per 10 Minutes
RateLimit_perSec = "10" #10 requests per second
OPGG_BaseURL = ".op.gg/"
OPGG_mmrURL = "summoner/ajax/mmr/summonerName="
## END GLOBALS ##

class Summoner:

	def __init__(self,username):
		username = username.lower().replace(" ", "")
		SummonerStats = RiotAPI.findByUsername(username)
		print(SummonerStats)
		self.username = username
		self.id = SummonerStats[username]['id']
		self.summonerLevel = SummonerStats[username]["summonerLevel"]
		self.name = SummonerStats[username]["name"]
		self.mmr = OPGG.getMMR(self.name)

	def addDuo(self, duoPartner):
		if(self.duo == None):
			self.inTeam = True
			self.duo = duoPartner
		else:
			print("Already Contains Duo: " + self.duo)

	def changeDuo(self, duoPartner):
		self.duo = duoPartner

	def removeDuo(self):
		self.duo = None

	def __str__(self):
		return self.username + " " +  str(self.id) + " " + str(self.summonerLevel) + " " + self.mmr

class Team:

	def __init__(self, players):
		self.players = players
		self.count = len(players)
		self.mmrcal(players)

	def mmrcal(self,players):
		self.mmr = 0
		for player in players:
			self.mmr += player.mmr

	def add(self, player):
		if player not in self.players:
			if self.count < 5:
				self.count += 1
				self.mmr += player.mmr
				player.inTeam = True
				self.players.append(player)
				if player.duo != None:
					self.mmr += 25
					add(player.duo)

	def remove(self, player):
		if player in self.players:
			if self.count > 0:
				self.players.remove(player)
				self.count -= 1
				self.mmr = mmrcal(self.players)
			else:
				print()

	def avgMMR(self):
		return self.mmr / self.count

class RiotAPI:

	def findByUsername(username,region="na"):
		# /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)

	def getSummonerID(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["id"]

	def getSummonerLevel(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["summonerLevel"]

	def findBySummonerID(ID,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}
		r = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + ID + "?api_key=" + APIKEY)
		return r.text

class OPGG:

	def getMMR(username):
		if ' ' in username:
			username = username.replace(" ","%20")
		pageContent = get("http://"+ REGION + OPGG_BaseURL + OPGG_mmrURL + username)
		lines = pageContent.text.splitlines()
		try:
			if "MMRBox Box" in lines[0]:
				return lines[4].strip().replace(",","")
			else:
				return "Unranked"
		except:
			print("Error with user: " + username)

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
		teams = makeTeams(extras, self.teamSize)
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


with open("players.txt", 'r') as f:
	players = f.readlines()

PlayerList = Playerlist()

for player in players:
	print(player)
	PlayerList.addPlayer(player.strip('\n'))

print(PlayerList)