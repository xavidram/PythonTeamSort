from requests import *


## GLOBALS ##
REGION = "na" #NA by default, can be changed
OPGG_BaseURL = ".op.gg/"
OPGG_mmrURL = "summoner/ajax/mmr/summonerName="
OPGG_PROFILE = "summoner/userName="
## END GLOBALS ##



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

		pageContent = get("https://" + REGION + OPGG_PROFILE + username)
		lines = pageContent.text.splitlines()
		try:
			tags = []
			i=0
			for line in lines:
				if 'Item tip' in line:
					tag.append(line)

			for t in tag:
				print(t)

		except Exception as e:
			print(str(e))


print(OPGG.getMMR_Past("xavidram"))