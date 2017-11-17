from time import sleep

from picamera import PiCamera
from sense_hat import SenseHat

camera = PiCamera()
sense = SenseHat()

__W = [255, 255, 255]     # White

WHITE_FLAG = [
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W]

camera.resolution = (1024, 768)
camera.iso = 200
#camera.vflip = True
#camera.hflip = True
camera.rotation = 180
#camera.exposure_mode = "off"
# camera.zoom = (0.0, 0.0, 1.0, 1.0)
camera.zoom = (0.25, 0.25, 0.5, 0.5)
camera.shutter_speed = 3000000


sense.set_pixels(WHITE_FLAG)
camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
sense.clear()

    


##import termios
##import sys
##import fcntl
##import os
##
##def getKeyCode(blocking = True):
##    fd = sys.stdin.fileno()
##    oldterm = termios.tcgetattr(fd)
##    newattr = termios.tcgetattr(fd)
##    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
##    termios.tcsetattr(fd, termios.TCSANOW, newattr)
##    if not blocking:
##        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
##        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
##    try:
##        return ord(sys.stdin.read(1))
##    except IOError:
##        return 0
##    finally:
##        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
##        if not blocking:
##            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
##
####while True:
####    print ("in")
####    key = ord(sys.stdin.read(1))
####    print (key)
####    if key ==ord("q"):
####        break
##
##while True:
##    key = getKeyCode(True)
##    print (key)
##    if ord(key)=="q":
##        break
##
##    
    
