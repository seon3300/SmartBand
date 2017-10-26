import os
os.chdir("/home/pi/A")#adjust path for location of this program
import time
import RPI.GPIO as GPIO
import Picamera
import datetime
from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(21)

with PiCamera() as camera:
    camera.rotation = 180
    camera.start_preview(fullscreen=False, window=(100,20,640,480))
    button.wait_for_press()
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.&S.jpg")
    camera.capture(filename)
    camera.stop_preview()