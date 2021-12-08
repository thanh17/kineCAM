import PIL
from PIL import Image
import os
import numpy as np

class OurImageClass():
    def __init__(self, width = 0, height = 0, channels = 0, data=[], mode = "RGB"):
        '''Initiates a image of given height, width and black pixels of a specific number of channels'''
        self.width = width
        self.height = height
        self.channels = channels
        self.data=[]
        if(not data):
            self.data = [[0 for j in range(channels)] for i in range(width*height)]
        else:
            self.data=data
        self.mode = mode

    def initialize_image(self,filename):
        '''Initialize image from filename'''
        image=Image.open(filename)
        data=[[x for x in y] for y in list(image.getdata())]
        self.channels=len(data[0])
        self.mode=image.mode
        self.width=image.size[0]
        self.height=image.size[1]
        self.data=data
        
    
    def get_pixel_index(self, x, y):
        '''[[r, g, b], [r, g, b],...] structure from top top left to top right and then bottom.'''
        if x >= self.width: x = self.width -1
        if x < 0: x = 0
        if y >= self.height: y = self.height -1
        if y < 0: y = 0
        index = self.width*y + x
        return index

    def get_pixel_value(self, x, y, z):
        '''Gets value of pixel for a specific channel'''
        # assert (x < 0 or x >= self.width or y < 0 or y >= self.height or z < 0 or z >= self.channels) == False, "Accesing pixel out of range"
        index = self.get_pixel_index(x,y)
        return self.data[index][z]


    def get_pixel_values(self, x, y):
        '''Gets pixel values for all channels of a specific pixel'''
        # assert (x < 0 or x >= self.width or y < 0 or y >= self.height) == False, "Accesing pixel out of range"
        index = self.get_pixel_index(x,y)
        return self.data[index]

    def set_pixel_value(self, x, y, z, c):
        '''Sets the value of one channel of a pixel'''
        if c < 0: c = 0
        if c > 255: c = 255
        if (x < 0 or x >= self.width or y < 0 or y >= self.height or z < 0 or z >= self.channels) == False:
            index = self.get_pixel_index(x,y)
            self.data[index][z] = c
        

    def set_pixel_values(self, x, y, data):
        '''Sets the value of all channels of a pixel'''
        assert (x < 0 or x >= self.width or y < 0 or y >= self.height) == False, "Accesing pixel out of range"
        index = self.get_pixel_index(x,y)
        self.data[index]=data
        
    def create_from_dict(self, image):
        '''given a filename this function uploads an input picture and changes its parameters to represent this image in our class.
        Used to debug for now'''
        self.width = image['width']
        self.height = image['height']
        self.data = image['pixels']
        try:
            self.channels = len(self.data[0])
        except:
            self.channels = 0
            
    def create_from_PIL(self, img):
        '''creates an image of our class from a PIL format'''
        img = img.convert('RGB')  # in case we were given a greyscale image
        img_data = img.getdata()
        self.data = []
        for pixel in img_data:
            self.data.append(list(pixel))
        self.width, self.height = img.size
        self.channels = len(self.data[0])
    @staticmethod
    def create_from_PIL(img):
        img = img.convert('RGB')  # in case we were given a greyscale image
        img_data = img.getdata()
        data = []
        for pixel in img_data:
            data.append(list(pixel))
        width, height = img.size
        channels = len(data[0])
        return OurImageClass(width,height,channels,data)

    @staticmethod
    def create_from_nparray(arr):
        '''creates an image of our format given an nparray'''
        data = []
        for y in range(arr.shape[0]):
            for x in range(arr.shape[1]):
                data.append(list(arr[y][x]))
        width=arr.shape[1]
        height=arr.shape[0]
        channels = len(data[0])
        return OurImageClass(width,height,channels,data)

    def create_from_filename(self, filename):
        '''creates image from a given file'''
        with open(filename, 'rb') as img_handle:
            img = Image.open(img_handle)
            self.create_from_PIL(img)

    @staticmethod
    def create_from_filename(self, filename):
        with open(filename, 'rb') as img_handle:
            img = Image.open(img_handle)
            return OurImageClass.create_from_PIL(img)

    def create_PIL(self):
        '''Generates an image of type PIL from our image class'''
        '''Makes and returns a PIL image of a given mode from our image data'''
        out = Image.new(mode= self.mode, size=(self.width, self.height))
        # Change RGB to L if image needs to be saved in greyscale
        img_data = []
        for pixel in self.data:
            if len(pixel) == 1: img_data.append(pixel[0])
            else: img_data.append(tuple(pixel))
        out.putdata(img_data)
        return out
    
    def save_PNG(self, filename):
        '''Saves a PNG image as filename from our image class'''
        pil_img = self.create_PIL()
        # if self.mode == "L" or self.mode == "BW": pil_img.convert("L")
        # if self.mode == "BW": pil_img.convert("1")
        pil_img.save(filename, "PNG")
    
    def save_BMP(self, filename):
        '''saves image as BMP from filename'''
        pil_img = self.create_PIL()
        pil_img.save(filename, "BMP")

    def brighten_image(self, percentage):
        '''Modifies the image based on the desired brightness change. Percentage is between -1.0 and 1.0'''
        for x in range(self.width):
            for y in range(self.height):
                original=self.get_pixel_values(x,y)
                c=[x for x in original]
                if(percentage<0):
                    c=[int(x*percentage*-1) for x in original]
                elif(percentage>0):
                    c=[int(((255-x)*percentage)+x) for x in original]              
                self.set_pixel_values(x,y,c)

    def contrast_image(self, percentage):
        '''Modifies the image based on the desired contrast change. Percentage is between -1.0 and 1.0'''
        contrast_value=255*percentage
        factor=(259*(255+contrast_value))/(255*(259-contrast_value))
        for x in range(self.width):
            for y in range(self.height):
                original=self.get_pixel_values(x,y)
                c=[int(factor*(x-128)+128) for x in original]
                self.set_pixel_values(x,y,c)


def set_pixels_test():
    '''crates a black 10x10 image and sets diagonal pixels to red, green and blue'''
    img = OurImageClass(10,10,3, mode = "RGB")
    img.set_pixel_value(0,0,0,255)
    img.set_pixel_value(1,1,1,255)
    img.set_pixel_value(2,2,2,255)
    img.set_pixel_value(3,3,0,255)
    img.set_pixel_value(4,4,1,255)
    img.set_pixel_value(5,5,2, 255)
    img.set_pixel_value(6,6,0, 255)
    img.set_pixel_value(7,7,1, 255)
    img.set_pixel_value(8,8,2, 255)
    img.set_pixel_value(9,9,0,255)
    img.save_PNG('./Output/image_manipulation/set_pixels_example.png')

def brightness_test():
    '''Tests the brightness function of our class'''
    filename = './Input/monkey.jpg'
    brightImageTest=OurImageClass()
    brightImageTest.initialize_image(filename)
    brightImageTest.brighten_image(0.3)
    brightImageTest.create_PIL().save("./Output/image_manipulation/monkey_brightness.jpg")

def contrast_test():
    '''Tests the contrast function of our class'''
    filename = './Input/monkey.jpg'
    contrastImageTest=OurImageClass()
    contrastImageTest.initialize_image(filename)
    contrastImageTest.contrast_image(0.5)
    contrastImageTest.create_PIL().save("./Output/image_manipulation/monkey_contrast.jpg")





# set_pixels_test()
# brightness_test()
# contrast_test()
