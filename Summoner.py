from RiotAPI import *

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
