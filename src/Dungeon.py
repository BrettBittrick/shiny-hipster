from Actor import *
class Dungeon :
	monsters = []
	size = 10

	def __init__(self,size):
		for x in xrange(0,size) :
			self.monsters.append(Actor("../dat/actor/defaultMonster.act" ,self))

	def append(self,actor) :
		self.monsters.append(actor)