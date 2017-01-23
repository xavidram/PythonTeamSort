from RiotAPI import *
from OPGG import *

class Summoner:

	def __init__(self,username):
		username = username.lower().replace(" ", "")
		SummonerStats = RiotAPI.findByUsername(username)
		#print(SummonerStats)
		self.username = username
		self.id = SummonerStats[username]['id']
		self.summonerLevel = SummonerStats[username]["summonerLevel"]
		self.name = SummonerStats[username]["name"]
		self.mmr = OPGG.getMMR(self.name)
		self.inTeam = False

	def __str__(self):
		return self.username + " " +  str(self.id) + " " + str(self.summonerLevel) + " " + str(self.mmr)

	#Overloading comparison operators for sorting #
	def __lt__(self, summoner2):
		return True if self.mmr <  summoner2.mmr else False

	def __gt__(self, summoner2):
		return True if self.mmr >  summoner2.mmr else False

	def __le__(self, summoner2):
		return True if self.mmr <= summoner2.mmr else False

	def __ge__(self, summoner2):
		return True if self.mmr >= summoner2.mmr else False

	def __eq__(self, summoner2):
		return True if self.mmr == summoner2.mmr else False

	def __ne__(self, summoner2):
		return True if self.mmr != summoner2.mmr else False