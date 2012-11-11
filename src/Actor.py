from Messenger import *
class Actor :
	# anything that can participate in combat
	name = "mumei"
	init = 0
	actInit = 100
	curHP = 100
	maxHP = 100
	atk = 10
	message = Messenger()
	dungeon = 0
	dead = False

	def __init__(self,name,dungeon):
		self.name = name
		message = Messenger()
		message.appear(self)
		self.dungeon = dungeon

	def advance(self) :
		self.init += 1

	def act(self) :
		if (self.curHP <= 0):
			print "%s died" % self.name
			self.dead = True
			return
		elif (self.init == self.actInit) :
			self.attack(self.findTarget(self.dungeon))
			self.init = 0
		self.advance()

	def attack(self,victim) :
		victim.hurt(self.atk)
		self.message.hurt(self,victim,self.atk)

	def hurt(self, dmg):
		#this will be made better later
		self.curHP -= dmg
		self.message.status(self)

	def findTarget(self, dungeon):
		#we'll just have him attack the first guy in the list
		if (len(dungeon.monsters) > 0) :
			return dungeon.monsters[0]
