from requests import *
from lxml import etree
import json

region = "na"
baseURL = ".op.gg/"
mmr = "summoner/ajax/mmr/summonerName="

class OPGG:

	def getMMR(username):
		if ' ' in username:
			username = username.replace(" ","%20")
		page = get("http://"+ region + baseURL + mmr + username)
		tree = etree.fromstring(page.content)
		return tree


print(OPGG.getMMR("xavidram"))