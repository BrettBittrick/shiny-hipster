print "Welcome to RPG!"
class Actor :
	# anything that can participate in combat
	init = 0
	actInit = 100
	def __init__(self):
		print "Actor created!"
		init = 0
		actInit = 100

	def advance(self) :
		print "Advancing"
		self.init += 1

	def act(self) :
		print "acting"
		self.advance()
		if (self.init == self.actInit) :
			print "Acting"
			self.init = 0
		else :
			print "Only %i of %i init, not acting" % (self.init, self.actInit)	

exit = False
turn = 0


x = Actor()
while (exit != True) : 
	print "Game Loop"
	x.act()
	print "after x.act"

