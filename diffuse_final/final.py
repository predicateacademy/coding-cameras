from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *
import random
import capture, helper

mc = Minecraft.create()
x, y, z = mc.player.getPos()
x = int(x)
y = int(y)
z = int(z)

#clear the field
mc.setBlocks(x-50, y, z-50, x+50, y+50, z+50, block.AIR.id)
mc.setBlocks(x-50, y-1, z-50, x+50, y-1, z+50, block.GRASS.id)

#add some bomb locations
bombs = []
for i in range(4):
	bombs.append((x+10+i, y, z))

#place the bombs
for bomb in bombs:
	mc.setBlock(bomb[0], bomb[1], bomb[2], block.TNT.id, 1)

#pick a random loser location
loser = random.choice(bombs)

while True:

	if len(bombs)==1:
		mc.postToChat("Winner")
		capture.take("winner winner", "chicken dinner")
		break

	#wait for a sword hit on a block we care about
	hit = helper.poll()

	if hit == loser:
		mc.postToChat("Oh No!!")
		helper.explode(hit)
		capture.take("you had", "one job to do")
		break
	else:
		mc.postToChat("Phew!")
		bombs.remove((x,y,z))
		mc.setBlock(hit[0], hit[1], hit[2], block.AIR.id)


