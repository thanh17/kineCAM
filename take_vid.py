from picamera import PiCamera 
from time import sleep 
from subprocess import call
import cv2
import os

def get_allowed(num_seconds, num_frames):
	total_frames = 32*num_seconds
	interval = total_frames//num_frames
	start = interval - 1
	allowed = {}
	for i in range(num_frames):
		allowed[start] = i
		start += interval
	return allowed




def video_to_frames(camera, num_seconds, num_frames):
	loc = '/home/pi/newKinegram/videos/video.h264'
	camera.start_preview()
	camera.start_recording(loc)
	sleep(num_seconds)
	camera.stop_recording()
	camera.stop_preview()

	command = "ffmpeg -i \"" + loc + "\" -c:v copy -f mp4 \"/home/pi/newKinegram/videos/convertedvid.mp4\""
	call([command], shell=True)

	vidcap = cv2.VideoCapture("/home/pi/newKinegram/videos/convertedvid.mp4")
	success, image = vidcap.read()
	count = 0
	allowed = get_allowed(num_seconds, num_frames)
	while success:
		if count in allowed:
			cv2.imwrite("/home/pi/newKinegram/Output/frame%d.png" % allowed[count], image)
		success, image = vidcap.read()
		count += 1

	os.remove("/home/pi/newKinegram/videos/convertedvid.mp4")
