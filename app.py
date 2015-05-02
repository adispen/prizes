from flask import Flask, render_template
import requests
import urllib, json
import locale

locale.setlocale(locale.LC_ALL, '')
url = "https://api.steampowered.com/IEconDOTA2_570/GetTournamentPrizePool/v1/?key=66E1E5D64EE0F14B06F3CBE57F75ABDA&leagueid=2733"
app = Flask(__name__)

def getJson():
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	prize = locale.currency(data['result']['prize_pool'], grouping=True)
	return prize

@app.route('/')
def show_prize(prize=None):
	return render_template('index.html', prize=getJson())

@app.route('/update', methods=['GET'])
def update():
	return json.dumps({'prize': getJson()})

if __name__ == '__main__':
	app.run(debug=True)

