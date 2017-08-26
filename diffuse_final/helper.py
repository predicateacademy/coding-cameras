def poll(bombs):
    while True:
        for evt in mc.events.pollBlockHits():
        	pos = evt.pos
        	x = int(pos.x)
        	y = int(pos.y)
        	z = int(pos.z)
        	if (x,y,z) in bombs:        		
        		return (x,y,z)
        sleep(0.1)

def explode(pos):
	fuse = 3
	blast = 10
	blockType = mc.getBlock(pos[0], pos[1], pos[2])
	for fuse in range(fuse):
		mc.setBlock(pos[0], pos[1], pos[2], block.AIR)
		sleep(0.5)
		mc.setBlock(pos[0], pos[1], pos[2], blockType)
		sleep(0.5)
        # create sphere of air
        for x in range(blast*-1,blast):
            for y in range(blast*-1, blast):
                for z in range(blast*-1,blast):
                    if x**2 + y**2 + z**2 < blast**2:
                        mc.setBlock(pos[0] + x, pos[1] + y, pos[2] + z, block.LAVA_FLOWING)	
