class Team:

	def __init__(self, players):
		self.players = players
		self.count = len(players)
		self.mmr = mmrcal(players)

	def mmrcal(players):
		for player in players:
			total += player.mmr
		return total

	def add(self, player):
		if player not in self.players:
			self.count += 1
			self.mmr += player.mmr
			player.inTeam = True
			self.players.append(player)
			if player.duo != None:
				self.mmr += 25
				add(player.duo)

	def remove(self, player):
		if player in self.players:
			self.players.remove(player)
			self.count -= 1
			self.mmr = mmrcal(self.players)

	def avgMMR(self):
		return self.mmr / self.count
