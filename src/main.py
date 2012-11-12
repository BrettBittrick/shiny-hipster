from Messenger import *
from Actor import *
from Player import *
from Dungeon import *
print "Welcome to RPG!"

exit = False

dungeon = Dungeon(1)
p = Player("../dat/actor/defaultPlayer.act", dungeon)
dungeon.monsters.append(p)

while (exit != True) : 
	for m in dungeon.monsters:
		if (m.dead == False):
			m.act()
		else :
			dungeon.monsters.remove(m)
	if (p.dead == True):
		print "Player died, game over!"
		exit = True
