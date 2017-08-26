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
