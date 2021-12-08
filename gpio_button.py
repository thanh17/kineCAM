#from video import Video
from gpiozero import Button
import video
button = Button(26)
import time

# Will send a command to capture_kinegram if the button is pressed

while True:
        button.wait_for_press()
        print('You pushed me')
        video.Video.capture_kinegram()
