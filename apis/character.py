

class Character(object):
	def __init__(self, name, realm, battlegroup, char_class, race, gender, level, achievementPoints, achievements=None, appearence=None, guild=None, hunter_pets=None, items=None, mounts=None, pets = None, pet_slots=None, professions=None, progression=None, pvp=None, quests=None, reputation=None, stats=None, talents=None, titles=None):
		self.name = name
		self.realm = realm
		self.battlegroup = battlegroup
		self.char_class = char_class
		self.race = race
		self.gender = gender
		self.level = level
		self.achievementPoints = achievementPoints
		self.achievements = achievements
		self.appearence = appearence
		self.guild = guild
		self.hunter_pets = hunter_pets
		self.items = items
		self.mounts = mounts
		self.pets = pets
		self.pet_slots = pet_slots
		self.professions = professions
		self.progression = progression
		self.pvp = pvp
		self.quests = quests
		self.reputation = reputation
		self.stats = stats
		self.talents = talents
		self.titles = titles
