from requests import *


## GLOBALS ##
REGION = "na" #NA by default, can be changed
OPGG_BaseURL = ".op.gg/"
OPGG_mmrURL = "summoner/ajax/mmr/summonerName="
## END GLOBALS ##



class OPGG:

	def getMMR(username):
		if ' ' in username:
			username = username.replace(" ","%20")
		pageContent = get("http://"+ REGION + OPGG_BaseURL + OPGG_mmrURL + username)
		lines = pageContent.text.splitlines()
		try:
			if "MMRBox Box" in lines[0]:
				return lines[4].strip().replace(",","")
			else:
				return "Unranked"
		except:
			print("Error with user: " + username)