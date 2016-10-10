from Summoner import *

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