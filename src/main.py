from Messenger import *
from Actor import *
from Player import *
from Dungeon import *
#kill this later
from Condition import *
print "Welcome to RPG \"Shiny-Hipster\""

exit = False

dungeon = Dungeon(10)
p = Player("../dat/actor/defaultPlayer.act", dungeon)
c = Condition()
p.addCondition(c)
dungeon.monsters.append(p)

while (exit != True) : 
	for m in dungeon.monsters:
		if (m.alive):
			m.tick()
		else :
			dungeon.monsters.remove(m)
	if (p.alive == False):
		print "Player died, game over!"
		exit = True
