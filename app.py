from flask import Flask, render_template
import requests
import urllib, json
import locale
import os

# Grabbing the API key from your environment variables (must set this yourself)
STEAM_API_KEY = os.environ.get('STEAM_API_KEY')

# Setting locale to be whatever the user has on their machine
locale.setlocale(locale.LC_ALL, '')

# Grabbing TI5 JSON response
url = "https://api.steampowered.com/IEconDOTA2_570/GetTournamentPrizePool/v1/"+\
		"?key="+STEAM_API_KEY+"&leagueid=2733"
app = Flask(__name__)

def getJson():
	"""	Grabs the JSON reposnse and parses the prize pool into proper currency 
	based on locale 
	"""
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	prize = locale.currency(data['result']['prize_pool'], grouping=True)
	return prize

@app.route('/')
def show_prize(prize=None):
	return render_template('index.html', prize=getJson())

@app.route('/update', methods=['GET'])
def update():
	""" This route exists for the JS on the frontend to grab and update the 
	prize pool in real time (every 3 seconds)
	"""
	return json.dumps({'prize': getJson()})

if __name__ == '__main__':
	app.run(debug=True)

