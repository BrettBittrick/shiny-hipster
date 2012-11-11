from Actor import *
class Player(Actor) :
	def act(self) :
		self.advance()
		if (self.init == self.actInit):
			print "Player's turn" 