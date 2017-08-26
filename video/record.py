import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.image_effect = 'gpen'
camera.start_preview()
camera.start_recording('my_video.h264')
camera.wait_recording(10)
camera.stop_recording()
camera.stop_preview()


