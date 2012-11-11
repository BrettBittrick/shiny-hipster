from Messenger import *
print "Welcome to RPG!"

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
		init = 0
		actInit = 100
		message = Messenger()
		message.appear(self)
		self.dungeon = dungeon
		dead = False

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

class Player(Actor) :
	def act(self) :
		self.advance()
		if (self.init == self.actInit):
			print "Player's turn" 
	
class Dungeon :
	monsters = []
	size = 10

	def __init__(self,size):
		for x in xrange(0,size) :
			self.monsters.append(Actor("%i" % x ,self))

	def append(self,actor) :
		self.monsters.append(actor)

exit = False

dungeon = Dungeon(5)
p = Player("Player", dungeon)
dungeon.monsters.append(p)

while (exit != True) : 
	for m in dungeon.monsters:
		if (m.dead == False):
			m.act()
		else :
			dungeon.monsters.remove(m)
	if (p.dead == True):
		print "Player died, game over!"
		exit = True
