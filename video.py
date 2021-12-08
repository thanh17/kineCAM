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
                #time.sleep(1)
                led.on()
                camera.capture(storage[i],'rgb')
                led.off()
                new_storage.append(OurImageClass.create_from_nparray(storage[i]))
                #OurImageClass.create_from_nparray(storage[i]).save_PNG("./Output/test"+str(i)+".png")
        #new_storage = []
        #for i in range(num_frames):
            #rgb_image = OurImageClass.create_from_nparray(storage[i])
            #dithered_output=creating_kinegrams.ditherRGB_to_BW(rgb_image)
            #rgb_image.save_PNG("./Output/fixing_camera_"+str(i)+".png")
            #new_storage.append(rgb_image)
        #for i in range(len(new_storage)):
            #new_storage[i].save_PNG("Output/another_test"+str(i)+".png")
            # for i in range(num_frames):
            #     output = OurImageClass.create_from_nparray(holder)
            #     storage[i]=output   

        #creating_kinegrams.generate_kinegram(storage,3).save_PNG('./Output/camera_kinegram_capture.png')
        creating_kinegrams.generate_kinegram(new_storage,3,False).save_PNG('/home/pi/newKinegram/Output/camera_kinegram_capture.png')
        # led.on()
        # print("printing")
        # print_command = 'lp -o fit-to-page /home/pi/newKinegram/Output/camera_kinegram_capture.png'
        # led.off()
        # subprocess.run([print_command], shell=True)
        conn = cups.Connection()
        printer_name = "ZJ-58-3"
        conn.printFile(printer_name,'/home/pi/newKinegram/Output/camera_kinegram_capture.png', "Hello",{'fit-to-page':'True'})
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
