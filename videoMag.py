import sys
from time import sleep
from datetime import datetime
from pytz import timezone
from picamera import PiCamera

def videoMag(directory):
  camera= PiCamera()
#  camera.resolution = (2592, 1944)
  
  camera.start_preview()

  key = None
  while (key != "q"):
    key = input("")
    if(key == "s"):
      dateNow  = datetime.now(timezone('US/Central'))
      filename = dateNow.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
      camera.capture(directory + '/' + filename, quality=100)
    if(key == "b" and camera.brightness >= 30):
      camera.brightness = camera.brightness - 1
    if(key == "B" and camera.brightness < 70):
      camera.brightness = camera.brightness + 1
    if(key == "c" and camera.contrast >= -30):
      camera.contrast = camera.contrast -1
    if(key == "C" and camera.contrast < 30):
      camera.contrast = camera.contrast + 1
  camera.close()

if len(sys.argv) != 2:
  print("bad command line args")
  camera.close()
  quit(1)

videoMag(sys.argv[1])
