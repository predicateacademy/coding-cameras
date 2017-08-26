from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.resolution = (498,286)

raw_input("Press enter to start")

for i in range(10):
    camera.capture('image{0:04d}.jpg'.format(i))
camera.stop_preview()
