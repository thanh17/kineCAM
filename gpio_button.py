#from video import Video
from gpiozero import Button
import new_video
button = Button(26)
import time

while True:
        #time.sleep(10)
        button.wait_for_press()
        print('You pushed me')
        new_video.Video.capture_kinegram()
        #Video.capture_kinegram()
        #print('You pushed me')
