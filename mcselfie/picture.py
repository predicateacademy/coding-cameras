from picamera import PiCamera

camera = PiCamera()
camera.resolution = (80,60)
camera.start_preview(alpha=128)
input('Enter to capture')
camera.capture('capture.jpg')
camera.close()

