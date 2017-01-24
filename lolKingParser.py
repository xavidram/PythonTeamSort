from html.parser import HTMLParser
from RiotAPI import *
from requests import *
from Summoner import *

# CONSTANTS
DEFAULT_REGION = 'na'
LOLK_BaseURL = "www.lolking.net/summoner/"
# EX: http://www.lolking.net/summoner/na/35979678/xavidram#profile
# END CONSTANTS

class parser(HTMLParser):
	def __init__(self):
		self.reset()
		self.NEWTAGS = []
		self.NEWATTRS = []
		self.HTMLDATA = []

	def handle_starttag(self,tag,attrs):
		self.NEWTAGS.append(tag)
		self.NEWATTRS.append(attrs)

	def handle_data(self,data):
		self.HTMLDATA.append(data)

	def clean(self):
		self.NEWTAGS = []
		self.NEWATTRS = []
		self.HTMLDATA = []

class LOLKING:

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

player = Summoner('xavidram')

print(LOLKING.getLKScore(player))