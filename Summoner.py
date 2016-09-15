class Summoner:

	def __init__(self,name,username,mmr,duo=None,inTeam=False):
		self.name = name
		self.username = username
		self.mmr = mmr
		self.duo = duo
		self.inTeam = inTeam

	def addDuo(self, duoPartner):
		self.inTeam = True
		self.duo = duoPartner

	def changeDuo(self, duoPartner):
		self.duo = duoPartner

	def removeDuo(self):
		self.duo = None

	def __str__(self):
		return self.name + " " + self.username + " " + str(self.mmr) + " " + str(self.inTeam)