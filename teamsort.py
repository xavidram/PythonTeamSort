import random
import time
from Team import *
from Summoner import *
from playerList import *

with open("players.txt") as p:
	lines = p.readlines()
	players = list()
	for line in lines:
		details = [x.strip for x in line.strip(,)]
		np = Summoner("None",details[0])
		players.add()