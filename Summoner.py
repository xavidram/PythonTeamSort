from RiotAPI import *


class Summoner:

	def __init__(self,username):
		SummonerStats = RiotAPI.findByUsername(username)
		self.username = username
		self.id = SummonerStats[username]['id']
		self.summonerLevel = SummonerStats[username]["summonerLevel"]

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
		return self.username + " " +  str(self.id) + " " + str(self.summonerLevel)

User = Summoner("xavidram")
print(User)