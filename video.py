from gpiozero import LED
import time
import picamera
import picamera.array
import numpy as np
from PIL import Image
from image import OurImageClass
import cups
import subprocess
import creating_kinegrams
class Video():
    @staticmethod
    def capture_kinegram():
        led = LED(12)
        x_resolution=320
        y_resolution=240
        num_frames=3
        storage=[np.empty((y_resolution, x_resolution, 3), dtype=np.uint8)]*num_frames
        with picamera.PiCamera() as camera:
            camera.resolution = (x_resolution, y_resolution)
            time.sleep(2)
            new_storage = []
            for i in range(num_frames):
                print("Cheese!")
                led.on()
                camera.capture(storage[i],'rgb')
                led.off()
                new_storage.append(OurImageClass.create_from_nparray(storage[i]))

        creating_kinegrams.generate_kinegram(new_storage,3,False).save_PNG('/home/pi/newKinegram/Output/live/camera_kinegram_capture.png')
        conn = cups.Connection()
        printer_name = "ZJ-58-3"
        conn.printFile(printer_name,'/home/pi/newKinegram/Output/live/camera_kinegram_capture.png', "Hello",{'fit-to-page':'True'})



