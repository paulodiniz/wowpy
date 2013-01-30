import requests
import jsonpickle
from constants import * 
from apis.character import Character

class API(object):

	def __init__(self, realm=None, locale=None):
		self.realm = realm
		self.locale = locale	

	def retrieve_char(self, name):
		r = requests.get(BATTLE_NET_URL + "/character/" + self.realm + "/" + name)
		decoded = jsonpickle.decode(r.text)
		character = Character(name = decoded['name'], realm = decoded['realm'], battlegroup = decoded['battlegroup'], char_class = decoded['class'], race = decoded['race'], gender = decoded['gender'], level = decoded['level'], achievementPoints = decoded['achievementPoints'])
		return character

api = API("Goldrinn")
charac = api.retrieve_char("Pdiniz")
print charac.name, charac.race


	
