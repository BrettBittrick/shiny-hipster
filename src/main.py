print "Welcome to RPG!"

class Messenger :
	message = "No Message"

	def __init__(self):
		print "Printing"

	def aoran(self,str):
		##determines whether or not a word should be preceeded by an a or an an
		##not working for some reason, probably in the comparison
		if (str[0] == "a" or str[0] == "e" or str[0] == "i" or str[0] == "o" or str[0] == "u") :
			return "an %s" % str 
		else :
			return "a %s" % str

	def appear(self,actor) :
		print "%s has appeared!" % self.aoran(actor.name)

	def hurt(self, attacker, victim, dmg) :
		print "%s hits %s and does %i damage!" % (attacker.name, victim.name, dmg)

	def status(self, actor):
		print "%s has %i of %i HP remaining!" % (actor.name, actor.curHP, actor.maxHP )

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
y = Actor("Monster y")
while (exit != True) : 
	x.act()

