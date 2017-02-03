"""
	Author: Xavid Ramirez
	Email: xavid.ramirez01@utrgv.edu
	Last Edit: January 30 2017
	License: MIT
"""
from requests import *
import json

## GLOBALS ##
REGION = "na" #NA by default, can be changed
URL = "https://" + REGION + ".api.pvp.net"
APIKEY = "RGAPI-0364e714-7e66-4567-aa8b-5ce65ae1620f"
RateLimit_perMin = "500" #500 Requests per 10 Minutes
RateLimit_perSec = "10" #10 requests per second

class RiotAPI:
	""" Class that will handle the API calls to riots api"""
	@staticmethod
	def findByUsername(username,region="na"):
		# /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)

	@staticmethod
	def getSummonerID(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["id"]

	@staticmethod
	def getSummonerLevel(username,region):
		r = get(URL+"/api/lol/" + region + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
		return json.loads(r.text)[username]["summonerLevel"]

	@staticmethod
	def findBySummonerID(ID,region):
		#/api/lol/{region}/v1.4/summoner/{summonerIds}
		r = get(URL + "/api/lol/" + region + "/v1.4/summoner/" + ID + "?api_key=" + APIKEY)
		return r.text
