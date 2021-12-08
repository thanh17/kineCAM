#from video import Video
from gpiozero import Button
import video
button = Button(26)
import time

while True:
        button.wait_for_press()
        print('You pushed me')
        video.Video.capture_kinegram()
