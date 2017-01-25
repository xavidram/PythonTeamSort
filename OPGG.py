from requests import *
from lxml import html


## GLOBALS ##
REGION = "na" #NA by default, can be changed
OPGG_BaseURL = ".op.gg/"
OPGG_mmrURL = "summoner/ajax/mmr/summonerName="
OPGG_PROFILE = "summoner/userName="
## END GLOBALS ##

#http://na.op.gg/summoner/userName=xavidram

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

		pageContent = get("http://" + REGION + OPGG_BaseURL + OPGG_PROFILE + username)
		
		#lines = pageContent.text.splitlines()
		try:
			tree = html.fromstring(pageContent.content)
			itemTip = tree.xpath('//li[@class="Item tip"]/text()')
			print(itemTip)
		except Exception as e:
			print(str(e))


OPGG.getMMR_Past("xavidram")