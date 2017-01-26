from requests import *
from bs4 import BeautifulSoup


## GLOBALS ##
REGION = "na" #NA by default, can be changed
OPGG_BaseURL = ".op.gg/"
OPGG_mmrURL = "summoner/ajax/mmr/summonerName="
OPGG_PROFILE = "summoner/userName="
## END GLOBALS ##

#http://na.op.gg/summoner/userName=xavidram

class MMR:

	def __init__(self, season=None,mmr=0,rank="Unranked"):
		self.season = season
		self.mmr = mmr
		self.rank = rank

	def __str__(self):
		return self.season + " " + str(self.rank) + " MMR: " + str(self.mmr)

	def printObject(self):
		print(self.season , str(self.rank) , " MMR: " , str(self.mmr))

class OPGG:

	def getMMR(username):
		if ' ' in username:
			username = username.replace(" ","%20")
		pageContent = get("http://"+ REGION + OPGG_BaseURL + OPGG_mmrURL + username)
		lines = pageContent.text.splitlines()
		try:
			if "MMRBox Box" in lines[0]:
				return int(lines[5].strip().replace(",",""))
			else:
				return 940
		except:
			print("Error with user: " + username)

	def getMMR_Past(username):
		if '' in username:
			username = username.replace(" ","%20")

		pageContent = get("http://" + REGION + OPGG_BaseURL + OPGG_PROFILE + username).text
		
		#lines = pageContent.text.splitlines()
		try:
			parsed_html = BeautifulSoup(pageContent,"html.parser")
			pastSeasons = parsed_html.body.find_all('li',attrs={'class':'Item tip'})
			pastMMR = list()
			for s in pastSeasons:
				rank = s.get("title").split(" ")
				pastMMR.append(MMR(s.b.contents,calculateMMR(rank),''.join([rank[0],rank[1]])))
		
			for x in pastMMR:
				x.printObject()
				
		except Exception as e:
			print(str(e))

def calculateMMR(rank):
	values = {
		"Bronze"	:	{
			"5"	:	{"Low":	800,"High": 869},
			"4"	:	{"Low":	870,"High": 939},
			"3"	:	{"Low":	940,"High": 1009},
			"2"	:	{"Low":	1010,"High": 1079},
			"1"	:	{"Low":	1080,"High": 1149}
		},
		"Silver"	:	{
			"5"	:	{"Low":	1150,"High": 1219},
			"4"	:	{"Low":	1220,"High": 1289},
			"3"	:	{"Low":	1290,"High": 1359},
			"2"	:	{"Low":	1360,"High": 1429},
			"1"	:	{"Low":	1430,"High": 1499}
		},
		"Gold"		:	{
			"5"	:	{"Low":	1500,"High": 1569},
			"4"	:	{"Low":	1570,"High": 1639},
			"3"	:	{"Low":	1640,"High": 1709},
			"2"	:	{"Low":	1710,"High": 1779},
			"1"	:	{"Low":	1780,"High": 1849}
		},
		"Platinum"	:	{
			"5"	:	{"Low":	1850,"High": 1919},
			"4"	:	{"Low":	1920,"High": 1989},
			"3"	:	{"Low":	1990,"High": 2059},
			"2"	:	{"Low":	2060,"High": 2129},
			"1"	:	{"Low":	2130,"High": 2199}
		},
		"Diamond"	:	{
			"5"	:	{"Low":	2200,"High": 2269},
			"4"	:	{"Low":	2270,"High": 2339},
			"3"	:	{"Low":	2340,"High": 2409},
			"2"	:	{"Low":	2410,"High": 2479},
			"1"	:	{"Low":	2480,"High": 2549}
		},
		"Masters" : {"Low":	2550,"High": 2899},
		"Challenger" : {"Low":	2900,"High": 5000}
	}

	if rank[0] in ["Masters","Challenger"]:
		if(len(rank) == 2):
			return int(values.get(rank[0]).get("Low")) + int(rank[1].strip("LP"))
		else:
			return int(values.get(rank[0]).get("Low"))
	else:
		if(len(rank) > 2):
			return int(values.get(rank[0]).get(rank[1]).get("Low")) + int(rank[2].strip("LP"))
		else:
			return int(values.get(rank[0]).get(rank[1]).get("Low"))


OPGG.getMMR_Past("sts")
