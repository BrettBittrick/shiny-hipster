class IOReader :
	"""lets you perform actions with files"""

	f = "Error"
	def __init__(self,path) :
		self.f = open(path, 'r')

	def parse(self) :
		"""returns a dictionary full of keys and values to be sorted by the 
		caller"""
		keys = {}

		for line in self.f :
			k = self.grabKey(line)
			keys.update(k)
			
			return keys

	def grabKey(self,line):
		#Accumulates characters into a string until it comes across a deliniator
		keys = {}
		key = ""
		value = ""
		keyFound = False
		#this is bad and I should feel bad
		qCount = 0
		for c in line :
			if not (keyFound) :
				#kill pesky newlines
				if not (c == ":" or c == "\n"):
					key = key + c
				else :
					keys[key] = "novalyet"
					keyFound = True
			elif not (c == "\n"):
				if (c == " " or c == "\t"):
					#strip tabs and other shit from the output
					continue
				#try and just get between the quotes
				elif (c == "\""):
					qCount += 1
				elif (qCount != 2):
					value = value + c

		keys = {key:value}
		return keys
