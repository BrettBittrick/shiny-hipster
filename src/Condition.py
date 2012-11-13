class Condition:
	"""persistant conditions that are applied to actors poison etc"""
	name = "unNamed condition"
	duration = 5

	def __init__(self):
		print "new condition"

	def condTick(self):
		print "%s condition ticked! %d" % (self.name, self.duration)
		self.duration -= 1
				