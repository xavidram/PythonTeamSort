from requests import *
import json


## GLOBALS ##
REGION = "na" #NA by default, can be changed
URL = "https://" + REGION + ".api.pvp.net"
APIKEY = "API HERE"
RateLimit_perMin = "500" #500 Requests per 10 Minutes
RateLimit_perSec = "10" #10 requests per second

class RiotAPI:

	def findByUsername(username,region="na"):
		# /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)

	def getSummonerID(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["id"]

	def getSummonerLevel(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["summonerLevel"]

	def findBySummonerID(ID,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}
		r = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + ID + "?api_key=" + APIKEY)
		return r.text
