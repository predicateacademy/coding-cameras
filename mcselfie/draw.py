from mcpi.minecraft import Minecraft
from skimage import io, color
import cmap

### load picture and map
selfie_rgb = io.imread("capture.jpg")
map_rgb = io.imread("cmap.png")

### Convert to Lab
selfie_lab = color.rgb2lab(selfie_rgb)
map_lab = color.rgb2lab(map_rgb)

### Talk to Minecraft
mc = Minecraft.create()

### Draw picture
cmap.draw(mc, selfie_lab, map_lab)
