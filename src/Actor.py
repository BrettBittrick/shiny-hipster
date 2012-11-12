from Messenger import *
from IOReader import *
import Attack
class Actor :
	"""Anything that can participate in combat"""

	name = "mumei"
	init = 0
	actInit = 100
	curHP = 100
	maxHP = 100
	atk = 10
	message = Messenger()
	dungeon = 0
	dead = False

	def __init__(self,path,dungeon):
		self.dungeon = dungeon
		#Read values from a file, then assign them to variables
		io = IOReader(path)
		k = io.parse()
		self.name = k['name']
		self.maxHP = int(k['maxHP'])
		self.curHP = int(k['curHP'])

	def advance(self) :
		self.init += 1

	def act(self) :
		if (self.curHP <= 0):
			self.dead = True
			return
		elif (self.init == self.actInit) :
			self.attack(self.getTarget(self.dungeon))
			self.init = 0
		self.advance()

	def attack(self,victim) :
		a = Attack.Attack(0,False,self.atk)
		victim.hurt(a)
		self.message.hurt(self,victim,self.atk)

	def hurt(self, attack):
		self.curHP -= attack.damage
		self.message.status(self)

	def getTarget(self, dungeon):
		#we'll just have him attack the first guy in the list
		if (len(dungeon.monsters) > 0) :
			return dungeon.monsters[0]
