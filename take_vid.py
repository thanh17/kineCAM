from picamera import PiCamera 
from time import sleep 
from subprocess import call
import cv2
import os

def video_to_frames(camera):
	loc = '/home/pi/newKinegram/videos/video.h264'
	camera.start_preview()
	camera.start_recording(loc)
	sleep(1)
	camera.stop_recording()
	camera.stop_preview()

	command = "ffmpeg -i \"" + loc + "\" -c:v copy -f mp4 \"/home/pi/newKinegram/videos/convertedvid.mp4\""
	call([command], shell=True)

	vidcap = cv2.VideoCapture("/home/pi/newKinegram/videos/convertedvid.mp4")
	success, image = vidcap.read()
	count = 0
	allowed = {9:0, 20:1, 31:2}
	while success:
		if count in allowed:
			cv2.imwrite("/home/pi/newKinegram/Output/frame%d.png" % allowed[count], image)
		success, image = vidcap.read()
		count += 1

	os.remove("/home/pi/newKinegram/videos/convertedvid.mp4")
