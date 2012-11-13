class Action :
	"""Eventually we'll have different damage types and such in here
	right now we just use this for init damage and such"""
	name = "Unnamed action"
	initReq = 0 #how long it takes to "cast"

	def __init__(self, name, initReq):
		self.initReq = initReq

	def doAct(self):
		print "Doing something"

class Attack(Action):

	name = "Unnamed Attack"
	initReq = 0
	damage = 0
	cancels = False
	target = ""

	def __init__(self,name,initReq,damage,cancels,target):
		self.name = name
		self.initReq = initReq
		self.damage = damage
		self.cancels = cancels
		self.target = target

	def doAct(self):
		self.target.hurt(self)