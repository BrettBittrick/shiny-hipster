class Messenger :
	message = "No Message"

	def __init__(self):
		#print "Printing"
		self.message = "Initialized"

	def aoran(self,str):
		##determines whether or not a word should be preceeded by an a or an an
		##not working for some reason, probably in the comparison
		if (str[0] == "a" or str[0] == "e" or str[0] == "i" or str[0] == "o" or str[0] == "u") :
			return "an %s" % str 
		else :
			return "a %s" % str

	def appear(self,actor) :
		print "%s has appeared!" % self.aoran(actor.name)

	## These two functions will need to be altered (damage done is calculated by the victim, so
	## there's no way to know how much damage an attack does at this point)
	def hurt(self, attacker, victim, dmg) :
		print "%s hits %s and does %i damage!" % (attacker.name, victim.name, dmg)

	def status(self, actor):
		print "%s has %i of %i HP remaining!" % (actor.name, actor.curHP, actor.maxHP )

	def prompt(self, message, prompt):
		print message
		return raw_input(prompt) 