import picamera
from PIL import Image
from time import sleep
from os import listdir
from os.path import isfile, join
import slack
import memegenerator
def write(img, overlay):
    print (img + ":" + overlay)
    o = Image.open(overlay).convert('RGBA')
    i = Image.open(img).convert('RGBA')

    print(i.mode + ":" + o.mode)

    #merge
    new_img = Image.alpha_composite(i, o)
    new_img.save(img)


def take(top=None, bottom=None):
    img = 'diffuse.png'    
    meme = 'diffuse-meme.png'
    camera = picamera.PiCamera()
    camera.framerate = 24
    camera.resolution = (400, 400)
    camera.capture(img)
    memegenerator.make(top, bottom, img, meme)
    slack.send(meme)
    return img
