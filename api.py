import requests
import jsonpickle
from constants import * 
from apis.character import Character
from apis.race import Race

class API(object):

	def __init__(self, realm=None, locale=None):
		self.realm = realm
		self.locale = locale	

	def retrieve_race(self,race_id):
		r = requests.get(BATTLE_NET_URL + "/data/character/races")
		decoded = jsonpickle.decode(r.text)
		for race in decoded['races']:
			if race['id'] == race_id:
				r = Race(race_id = race['id'], mask = race['mask'], side = race['side'], name = race['name'])
				return r
		
	def retrieve_char(self, name):
		r = requests.get(BATTLE_NET_URL + "/character/" + self.realm + "/" + name)
		decoded = jsonpickle.decode(r.text)
		race = self.retrieve_race(decoded['race'])
		character = Character(name = decoded['name'], realm = decoded['realm'], battlegroup = decoded['battlegroup'], char_class = decoded['class'], race = race, gender = decoded['gender'], level = decoded['level'], achievementPoints = decoded['achievementPoints'])
		return character
	

api = API("Goldrinn")
charac = api.retrieve_char("Pdiniz")
print charac.items


	
