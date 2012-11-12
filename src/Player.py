from Actor import *
from Messenger import *
class Player(Actor) :
	mess = Messenger()
	def act(self) :
		self.advance()
		if (self.init == self.actInit):
			index = 1
			for m in self.dungeon.monsters :
				print "(%i) %s %s" % (index, m.name, self.mess.status(m))
				index += 1
			self.mess.prompt("Who do you wish to attack?", "%s>" % self.name)	