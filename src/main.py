print "Welcome to RPG!"

class Messenger :
	message = "No Message"

	def __init__(self):
		print "Printing"

	def aoran(self,str):
		##determines whether or not a word should be preceeded by an a or an an
		if (str[0] == 'a' or str[0] == 'e' or str[0] == 'i' or str[0] == 'o' or str[0] == 'u') :
			return "an %s" % str 
		else :
			return "a %s" % str
	def appear(self,actor) :
		print "%s has appeared!" % self.aoran(actor.name)

class Actor :
	# anything that can participate in combat
	name = "mumei"
	init = 0
	actInit = 100
	curHP = 100
	maxHP = 100
	atk = 10

	def __init__(self,name):
		self.name = name
		init = 0
		actInit = 100
		message = Messenger()
		message.appear(self)

	def advance(self) :
		self.init += 1

	def act(self) :
		self.advance()
		if (self.init == self.actInit) :
			self.init = 0

exit = False
turn = 0

x = Actor("Actor x")
while (exit != True) : 
	x.act()

