#from video import Video
from gpiozero import Button
import new_video
button = Button(26)
import time


# Adjustable parameters to change the kinegram produced
num_frames = 3 #must be int > 0 (> 1 for kinegram and not static image)
hole_width = 3 #must be int > 0
difference_detection = False #must be bool
threshold = 30 #must be int
num_seconds = 1 #must be int > 0




while True:
        #time.sleep(10)
        button.wait_for_press()
        print('You pushed me')
        new_video.Video.capture_kinegram(num_frames, hole_width, difference_detection, threshold, num_seconds)

