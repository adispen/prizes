from flask import Flask
import requests
import urllib, json
import locale

locale.setlocale(locale.LC_ALL, '')
url = "https://api.steampowered.com/IEconDOTA2_570/GetTournamentPrizePool/v1/?key=66E1E5D64EE0F14B06F3CBE57F75ABDA&leagueid=2733"
response = urllib.urlopen(url)
data = json.loads(response.read())
prize = data['result']['prize_pool']

print locale.currency(prize, grouping=True)
