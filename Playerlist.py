from Team import *
from Summoner import *
import random
from datetime import datetime
import time
from random import shuffle
import numpy

def getkey(object):
	return object.mmr

class Playerlist:

	def __init__(self, count=0, teamSize=5):
		self.count = count
		self.players = list()
		self.teamSize = teamSize
		self.numTeams = 0
		self.Teams = None


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
		sorted(self.players)
		self.extras = list()
		return self.makeTeams()
		
	def printTeams(self):
		for i in range(0,self.numTeams):
			self.Teams[i].printTeam()

	def printList(self):
		for player in self.players:
			print(player)

	def getAverageTeamMMR(self):
		avg = 0
		for T in self.Teams:
			avg += T.mmr
		return int(avg / self.numTeams)

	def makeTeams(self):
		print('\n')
		
		extrasCount = self.count % self.teamSize
		numTeams = int(self.count / self.teamSize)

		self.extras = list()

		for i in range(0,extrasCount):
			random.seed(datetime.now())
			rNum = int(random.uniform(0,time.time()) % self.count)
			self.extras.append(self.players[rNum])
			self.players.pop(rNum)

		players = sorted(self.players,reverse=True)

		#set the team captains
		self.Teams = list()
		for i in range(0,numTeams):
			self.Teams.append(Team([players[0]],1))
			players.pop(0)

		#add highest player left in list to team with lowest total mmr
		#shuffle(players)

		#start rebalancing
		self.numTeams = numTeams