from image import OurImageClass
import os
from os import listdir
import numpy as np

def grayscale(im):
    '''converts RGB image into grayscale'''
    output = OurImageClass(im.width, im.height, channels = 1, mode = 'L')
    for i in range (im.width):
        for j in range (im.height):
            r = im.get_pixel_value(i,j,0)
            g = im.get_pixel_value(i,j,1)
            b = im.get_pixel_value(i,j,2)
            output.set_pixel_value(i,j,0,np.uint8(1/3*(r+g+b)))
    return output


def quantize_val(val):
    if val >= 128: return 255
    else: return 0

def ditherRGB_to_BW(im):
    '''Converts an image in RGB to its dithered version in BW'''
    gr = grayscale(im)
    for j in range(im.height):
        for i in range(im.width):
            old_val = gr.get_pixel_value(i,j,0)
            new_val = quantize_val(old_val)
            gr.set_pixel_value(i,j,0,new_val)
            error = old_val - new_val

            right = gr.get_pixel_value(i+1, j, 0)
            bottom_left = gr.get_pixel_value(i-1, j+1, 0)
            bottom = gr.get_pixel_value(i, j+1, 0)
            bottom_right = gr.get_pixel_value(i+1, j+1, 0)

            gr.set_pixel_value(i+1, j, 0, right +error*7/16)
            gr.set_pixel_value(i-1, j+1, 0, bottom_left +error*3/16)
            gr.set_pixel_value(i, j+1, 0, bottom +error*5/16)
            gr.set_pixel_value(i+1, j+1, 0, bottom_right +error*1/16)
    return gr

def ims_from_frames(folder, dithered = False, frame_num = 3):
    '''Returns an image list of images in the folder, dithered if dithered=True and a maximum number frame_num images.'''
    to_kinegram = []
    files = os.listdir(folder)
    for file in files:
        filename = folder+'/'+file
        im=OurImageClass()
        im.initialize_image(filename)
        if dithered:
            im1 = ditherRGB_to_BW(im)
            to_kinegram.append(im1)
        else: to_kinegram.append(im)
        if len(to_kinegram) == frame_num: break
    return to_kinegram


def detect_difference(img_list):
    '''Returns an grayscale image mapping the difference between the three images in the input image list'''
    im1 = img_list[0]
    im2 = img_list[1]
    im3 = img_list[2]
    diff_im = OurImageClass(width = im1.width, height = im1.height, channels = 1, mode = 'L')
    for i in range(im1.width):
        for j in range(im1.height):
            diff = 0
            for c in range(3):
                p1 = int(im1.get_pixel_value(i,j,c))
                p2 = int(im2.get_pixel_value(i,j,c))
                p3 = int(im3.get_pixel_value(i,j,c))
                diff += 1/3.0*(abs(p1-p2) + abs(p2-p3) + abs(p3-p1))
            diff_im.set_pixel_value(i,j,0, int(diff))
    return diff_im


def generate_kinegram(img_list, hole_width=3, difference_detection=False, threshold=30, dithered = False):
    if difference_detection == True:
        diff_im = detect_difference(img_list)
        mid_im = img_list[1]
    width = img_list[0].width
    height = img_list[0].height
    output = OurImageClass(width, height, img_list[0].channels, mode="RGB")
    if dithered: output.mode = "L"
    for x in range(width):
        img_num = x // hole_width % len(img_list)
        current_image = img_list[img_num]
        for y in range(height):
            image_pixel = current_image.get_pixel_values(x, y)
            if difference_detection == False:
                output.set_pixel_values(x, y, image_pixel)
            else:
                diff_pix = diff_im.get_pixel_value(x, y, 0)
                if diff_pix < threshold:
                    pix_val = mid_im.get_pixel_values(x, y)
                    output.set_pixel_values(x, y, pix_val)
                else:
                    output.set_pixel_values(x, y, image_pixel)
            # print(output.get_pixel_values(x,y))
    return output


    


def test_dithering():
    filename = './Input/monkey.jpg'
    im=OurImageClass()
    im.initialize_image(filename)
    im1 = ditherRGB_to_BW(im)
    filename = './Output/dithered_images/dithered_monkey.jpg'
    im1.save_PNG(filename)

def test_dithered_kinegram():
    folder = './Input/cata3'
    dithered_frames = ims_from_frames(folder, True)
    out = generate_kinegram(dithered_frames, 3, dithered=True)
    filename = './Output/kinegrams/cata3_kinegram_dithered.jpg'
    out.save_PNG(filename)

def test_undithered_kinegram():
    folder = './Input/cata3'
    frames = ims_from_frames(folder)
    out = generate_kinegram(frames, 3)
    filename = './Output/kinegrams/cata3_kinegram_undithered.jpg'
    out.save_PNG(filename)

def test_difference_kinegram():
    folder = './Input/cata3'
    frames = ims_from_frames(folder)
    out = generate_kinegram(frames, 3, difference_detection= True)
    filename = './Output/kinegrams/cata3_difference.jpg'
    out.save_PNG(filename)


# test_dithering()
# test_dithered_kinegram()
# test_undithered_kinegram()
# test_difference_kinegram()


