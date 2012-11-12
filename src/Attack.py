class Attack :
	"""Eventually we'll have different damage types and such in here
	right now we just use this for init damage and such"""

	initReq = 0 #how long it takes to "cast"
	cancels = False #Whether or not it cancels enemy attacks
	damage = 0 #how much damage it does (damage type later)

	def __init__(self, initReq, cancels,damage) :
		self.initReq = initReq
		self.cancels = cancels
		self.damage = damage
		