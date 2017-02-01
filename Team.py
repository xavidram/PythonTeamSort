from Summoner import *

class Team:
	""" Will host list of Summoners as a team for sorting"""
	def __init__(self, players=None,count=0):
		self.players = players if players != None else []
		self.count = count
		self.name = None
		#self.count = len(players)
		self.mmr = self.mmrcal(players) if players != None else 0

	def mmrcal(self,players):
		mmr = 0
		for player in players:
			mmr += int(player.mmr)
		return mmr
	
	def add(self, player):
		#Due to the overload of comparison operators for
		#sorting, __eq__ marks true due to mmr calculations
		#so implementing a bruteforce check
		exists = False
		for p in self.players:
			if player.username == p.username:
				exists = True

		if exists == False:
			if self.count < 5:
				self.count += 1
				self.mmr += int(player.mmr)
				player.inTeam = True
				self.players.append(player)

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

	def printTeam(self):
		print("Team Name: ",self.name)
		print("Team Members:")
		for player in self.players:
			print(player)
		print("Team MMR: ",self.mmr)
		print("Avg MMR:", int(self.mmr / 5))
		print("------")

			#Overloading comparison operators for sorting #
	def __lt__(self, Team2):
		return True if self.mmr <  Team2.mmr else False

	def __gt__(self, Team2):
		return True if self.mmr >  Team2.mmr else False

	def __le__(self, Team2):
		return True if self.mmr <= Team2.mmr else False

	def __ge__(self, Team2):
		return True if self.mmr >= Team2.mmr else False

	def __eq__(self, Team2):
		return True if self.mmr == Team2.mmr else False

	def __ne__(self, Team2):
		return True if self.mmr != Team2.mmr else False