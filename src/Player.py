from Actor import *
from Messenger import *
class Player(Actor) :
	mess = Messenger()
	def act(self) :
		if (self.curHP <= 0) :
			self.dead = True
		self.advance()
		if (self.init == self.actInit):
			index = 0
			self.init = 0
			for m in self.dungeon.monsters :
				print "(%i) %s %s" % (index, m.name, self.mess.status(m))
				index += 1

			self.attack(self.dungeon.monsters[self.getTarget()])

	def getTarget(self):
		target = self.mess.prompt("What do you wish to attack?",
			"%s >" % self.name)
		while not (int(target) < len(self.dungeon.monsters)):
			self.getTarget()
			target = self.mess.prompt("What do you wish to attack?",
			"%s >" % self.name)
		return int(target)
