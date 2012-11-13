from Messenger import *
from IOReader import *
import Action
import random
class Actor :
	"""Anything that can participate in combat"""
	init = 0
	chooseInit = 100
	actInit = 125 #temp value so we can do the first comparison
	dungeon = 0
	nextAct = Action.Action("blah",25)
	alive = True

	def __init__(self,path,dungeon):
		self.dungeon = dungeon
		#Read values from a file, then assign them to variables
		io = IOReader(path)
		k = io.parse()
		self.name = k['name']
		self.maxHP = int(k['maxHP'])
		self.curHP = int(k['curHP'])

		#set init to a random value to spice things up
		random.seed()
		self.init = random.randrange(0,self.actInit)

	def tick(self):
		self.alive = (self.curHP > 0)
		if (self.alive) :	
			if (self.init == self.chooseInit):
				#choose action
				self.nextAct = self.getAct()
				self.actInit = self.chooseInit + self.nextAct.initReq
			elif (self.init == self.actInit):
				self.nextAct.doAct()
				self.init = 0

		self.advance()

	def advance(self) :
		self.init += 1

	def getAct(self):
		#just attack the first monster in the dungeon
		return Action.Attack("No name",50,25,False,self.getTarget(self.dungeon))

	def getTarget(self,dungeon):
		#add code to make sure 
		return self.dungeon.monsters[0]

	def hurt(self,action):
		self.curHP -= action.damage

