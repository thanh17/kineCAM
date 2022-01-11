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
            print("Cheese!")
            led.on()
            video_to_frames(camera)
            led.off()

        for i in range(num_frames): 
            new_storage.append(OurImageClass.create_from_filename("./Output/frame"+str(i)+".png"))
        creating_kinegrams.generate_kinegram(new_storage,3,False).save_PNG('/home/pi/newKinegram/Output/camera_kinegram_capture.png')
        conn = cups.Connection()
        printer_name = "ZJ-58-3"
        #conn.printFile(printer_name,'/home/pi/newKinegram/Output/camera_kinegram_capture.png', "Hello",{'fit-to-page':'True'})
        conn.printFile(printer_name,'/home/pi/newKinegram/Output/camera_kinegram_capture.png', "Hello", {})
        #creating_kinegrams.generate_kinegram_np_array(storage,5).create_PIL().save('./Testing_Kinegrams/data/camera_kinegram_capture.jpg')
        # for i in range(num_frames):
        #     out = storage[i].create_PIL()
        #     out.save('./Input/campera_capture_'+str(i)+'.jpg')
        #     print("Image "+str(i)+" saved")
'''
def brightness_test():
    filename = './Input/campera_capture.jpg'
    brightImageTest=OurImageClass()
    brightImageTest.initialize_image(filename)
    brightImageTest.brighten_image(0.3)
    brightImageTest.create_PIL().save("./Output/capture_brightness.jpg")
def contrast_test():
    filename = './Input/campera_capture.jpg'
    contrastImageTest=OurImageClass()
    contrastImageTest.initialize_image(filename)
    contrastImageTest.contrast_image(0.5)
    contrastImageTest.create_PIL().save("./Output/capture_contrast.jpg")
'''
#Video.capture_kinegram()
#brightness_test()
#contrast_test()
