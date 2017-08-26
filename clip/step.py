from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.resolution = (498,286)


for i in range(100):
    a = raw_input("Enter for next one, s to stop")
    print a
    if a == 's':
        break
    camera.capture('image{0:04d}.jpg'.format(i))
camera.stop_preview()
