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
		if (m.alive):
			m.tick()
		else :
			dungeon.monsters.remove(m)
	if (p.alive == False):
		print "Player died, game over!"
		exit = True
