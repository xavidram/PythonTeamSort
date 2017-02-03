"""
	Author: Xavid Ramirez
	Email: xavid.ramirez01@utrgv.edu
	Last Edit: January 30 2017
	License: MIT
"""
from datetime import datetime
from random import shuffle
from models.Team import *
from models.Summoner import *
import random, time, numpy, csv

def getkey(object):
	""" Returns object key mmr value """
	return object.mmr

class Playerlist:
	"""List of players class for sorting and creating teams"""
	def __init__(self, count=0, teamSize=5):
		self.count = count
		self.players = list()
		self.teamSize = teamSize
		self.numTeams = 0
		self.Teams = None


	def addPlayer(self, username):
		"""Add player to list, increment player count"""
		self.players.append(Summoner(username))
		self.count += 1

	def removePlayer(self, username):
		""" Remove player for list, decrement player count """
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

	def toCsv(self):
		with open('Tournament.csv','w') as outfile:
			writer = csv.writer(outfile,delimiter=",")
			for T in self.Teams:
				data = T.toCSVData()
				writer.writerows(data)
				writer.writerow([])

	def getAverageTeamMMR(self):
		""" Return the average mmr for team """
		avg = 0
		for T in self.Teams:
			avg += T.mmr
		return int(avg / self.numTeams)

	def makeTeams(self):
		print('\n')
		
		extrasCount = self.count % self.teamSize
		numTeams = int(self.count / self.teamSize)

		self.extras = list()

		""" Randomly select the extras """
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
		for p in players:
			self.Teams = sorted(self.Teams,reverse=False)
			self.Teams[0].add(p)
		#shuffle(players)
		#number the teams
		n = 1
		for T in  self.Teams:
			T.name = ''.join(["Team ",str(n)])
			n += 1 
		#start rebalancing
		self.numTeams = numTeams