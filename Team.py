from Summoner import *

class Team:

	def __init__(self, players=None,count=0):
		self.players = players if players != None else []
		self.count = len(players) if count > 0 else 0
		#self.count = len(players)
		self.mmr = self.mmrcal(players) if players != None else 0

	def mmrcal(self,players):
		mmr = 0
		for player in players:
			mmr += int(player.mmr)
		return mmr


	def add(self, player):
		if player not in self.players:
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
		print("Team Members:")
		for player in self.players:
			print(player)
		print("Team MMR: ",self.mmr)
		print("------")