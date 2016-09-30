from requests import *
import json


REGION = "na" #NA by default, can be changed
URL = "https://" + REGION + ".api.pvp.net"
APIKEY = "051db1a2-6b57-41c4-bc99-1e3a29056047"
RateLimit_perMin = "500" #500 Requests per 10 Minutes
RateLimit_perSec = "10" #10 requests per second

class Summoner:

	def __init__(self,username,region):
		summoner = RiotAPI.findByUsername(username,region)
		self.username = summoner[username]["name"]
		self.id = summoner[username]["id"]
		self.summonderLevel = summoner[username]["summonerLevel"]
		self.profileIconId = summoner[username]["profileIconId"]
		self.revsionDate = summoner[username]["revisionDate"]
		self.region = region

	def getMasteries(self):
		return RiotAPI.getMasteriesById(self.id,self.region)

	def getRunes(self):
		return RiotAPI.getRunesById(self.id, self.region)

class RunePage:

	def __init__(self,data):
		self.id = str(data["id"])
		self.name = data["name"]
		self.current = data["current"]
		if "slots" in data:
			self.slots = data["slots"]
		else:
			self.slots = []

class MasteryPage:

	def __init__(self,data):
		self.id = str(data["id"])
		self.name = data["name"]
		self.current = data["current"]
		if "masteries" in data:
			self.masteries = data["masteries"]
		else:
			self.masteries = []

	def getMasteryInfo(id):


class RiotAPI:

	def findByUsername(username,region):
		# /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)

	def getSummonerID(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["id"]

	def getSummonerLevel(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["summonerLevel"]

	def getProfileIconId(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["profileIconId"]

	def getRevisionDate(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["revisionDate"]

	def findBySummonerID(ID,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}
		r = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + ID + "?api_key=" + APIKEY)
		return r.text

	def getMasteriesByUsername(username,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		masteries = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + str(json.loads(r.text)[username]["id"]) + "/masteries" + "?api_key=" + APIKEY)
		return masteries.text

	def getMasteriesById(SummonerId,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries
		masteries = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + str(SummonerId) + "/masteries" + "?api_key=" + APIKEY)
		#return json.loads(masteries.text)[str(SummonerId)]["pages"][0]["masteries"]
		Pages = json.loads(masteries.text)[str(SummonerId)]["pages"]
		MasteryPages = dict()
		for page in Pages:
			MasteryPages[page["name"]] = MasteryPage(page)
		return MasteryPages
		

	def getRunesByUsername(username,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}/runes
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		runes = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + str(json.loads(r.text)[username]["id"]) + "/runes" + "?api_key=" + APIKEY)
		return masteries.text

	def getRunesById(SummonerId,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries
		runes = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + str(SummonerId) + "/runes" + "?api_key=" + APIKEY)
		Pages = json.loads(runes.text)[str(SummonerId)]["pages"]
		RunePages = dict()
		for page in Pages:
			RunePages[page["name"]] = RunePage(page)
		return RunePages
