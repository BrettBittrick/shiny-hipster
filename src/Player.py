from Actor import *
from Messenger import *
class Player(Actor) :
	mess = Messenger()

	def getTarget(self,dungeon):

		index = 0

		for m in dungeon.monsters :
			print "(%i) %s %s" % (index, m.name, self.mess.status(m))
			index += 1

		target = self.mess.prompt("What do you wish to attack?",
			"%s >" % self.name)
		while not (int(target) < len(self.dungeon.monsters)):
			self.getTarget()
			target = self.mess.prompt("What do you wish to attack?",
			"%s >" % self.name)
		return dungeon.monsters[int(target)]