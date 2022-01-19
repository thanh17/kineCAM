from gpiozero import LED
import time
import picamera
import picamera.array
import numpy as np
from PIL import Image
from image import OurImageClass
import cups
import subprocess
from take_vid import video_to_frames
import creating_kinegrams
class Video():
    @staticmethod
    def capture_kinegram(num_frames, hole_width, difference_detection, threshold, num_seconds):
        led = LED(12)
        x_resolution=320
        y_resolution=240
        storage=[np.empty((y_resolution, x_resolution, 3), dtype=np.uint8)]*num_frames
        with picamera.PiCamera() as camera:
            camera.resolution = (x_resolution, y_resolution)
            time.sleep(2)
            new_storage = []
            print("Cheese!")
            led.on()
            video_to_frames(camera, num_seconds, num_frames)
            led.off()

        for i in range(num_frames):
            new_storage.append(OurImageClass.create_from_filename("/home/pi/newKinegram/Output/frame"+str(i)+".png"))
        creating_kinegrams.generate_kinegram(new_storage,hole_width,difference_detection, threshold).save_PNG('/home/pi/newKinegram/Output/camera_kinegram_capture.png')
        conn = cups.Connection()
        printer_name = "ZJ-58-3"
        #prints white image before image to make sliding the overlay easier
        conn.printFile(printer_name,'/home/pi/newKinegram/white.jpg', "Buffer", {})
        conn.printFile(printer_name,'/home/pi/newKinegram/Output/camera_kinegram_capture.png', "Hello", {})

