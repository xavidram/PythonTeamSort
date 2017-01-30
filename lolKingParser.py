"""
	Author: Xavid Ramirez
	Email: xavid.ramirez01@utrgv.edu
	Last Edit: January 30 2017
	License: MIT
"""
from html.parser import HTMLParser
from RiotAPI import *
from requests import *
from Summoner import *

# CONSTANTS
DEFAULT_REGION = 'na'
LOLK_BaseURL = "www.lolking.net/summoner/"
# EX: http://www.lolking.net/summoner/na/35979678/username#profile
# END CONSTANTS

class LOLKING:
	
	@staticmethod
	def getLKScore(summoner):
		if ' ' in summoner.username:
			summoner.username = summoner.username.replace(" ","%20")
		pageContent = get("http://"
			+ LOLK_BaseURL 
			+ DEFAULT_REGION 
			+ '/' + str(summoner.id)
			+ '/' + summoner.username)
		lines = pageContent.text.splitlines()
		
		i=0
		for line in lines:
			if 'class="summoner-stat"' in line and '<strong>' in lines[i+1]:
				return int(lines[i+1].replace("<strong>","").replace("</strong>","").strip())
			i += 1