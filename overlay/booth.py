import picamera
from PIL import Image
from time import sleep
from os import listdir
from os.path import isfile, join
import console
import slack

def write(img, overlay):
    print (img + ":" + overlay)
    o = Image.open(overlay).convert('RGBA')
    i = Image.open(img).convert('RGBA')

    print(i.mode + ":" + o.mode)

    #merge
    new_img = Image.alpha_composite(i, o)
    new_img.save(img)

def clear_overlay():
    for o in camera.overlays:
        camera.remove_overlay(o) 

def set_overlay(overlay, camera, trans=128) :

    clear_overlay()
        
    # Load the arbitrarily sized image
    img = Image.open(overlay)

    # Set the camera resolution to match the overlay
    width, height = img.size
    camera.resolution = (width, height)
    
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size, alpha=trans, layer=3)
    

index = 0
overlays = [f for f in listdir('images') if isfile(join('images', f))]
def next_overlay():
    global index
    if index == (len(overlays) - 1):
        index = -1
    index = index + 1
    return 'images/' + overlays[index]

def prev_overlay():
    global index
    if index == 0:
        index = len(overlays) - 1
    index = index - 1
    return 'images/' + overlays[index]
    


if __name__ == "__main__":
    camera = picamera.PiCamera()
    camera.framerate = 24
    overlay = next_overlay()
    capture = None
    i = 0

    while True:
        camera.start_preview()
        set_overlay(overlay, camera)
        
        c = console.show()
        if c == console.QUIT:
            break
        elif c == console.LEFT:
            overlay = prev_overlay()
        elif c == console.RIGHT:
            overlay = next_overlay()
        elif c == console.CENTER:
            capture = 'image{0:04d}.png'.format(i)
            camera.capture(capture)
            write(capture,overlay)        
            i = i + 1
        elif c == console.PREVIEW and capture is not None:
            print 'preview ' + capture
            clear_overlay()
            camera.stop_preview()
            Image.open(capture).show(title="Image Preview")
            sleep(5)
        elif c == console.SEND and capture is not None:
            print 'sending ' + capture
            slack.send(capture)
        camera.stop_preview()    
