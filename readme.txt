Welcome to kineCAM!

This code works with a Raspberry Pi to take photos of a camera, produce kinegrams out of photos taken 1 second apart from eachother, and print the resulting
kinegram in a receipt printer.


image.py file has a OurImageClass, which we built and use to manipulate our images. This class has different functionalities that allow us to:
- Initialize an image into a class from another format like nparray, PImage and jpg.
- Set and get pixel values
- Save image as PNG, BMP or PImage
- Manipulate the image changing its brightness and contrast

At the end of the file we included some functions to test our Class locally, in lines 193-195 you can uncomment to run the different functions and their output
will be saved to the 'Output/image_manipulation/' folder.


creating_kinegram.py file has all of the functions needed to create the clearest kinegram. Different functions have different functionalities
- grayscale: returns a grayscale image of OurImageClass when given the same image in RGB.
- ditheredRGBtoBW: given an RGB image in OurImageClass, it dithers it and returns the resulted dither.
- ims_from_frames: given a folder name with images, this function returns a list of OurImageClass images of the images in the folder. This function
takes additional parameter dithered = False, and when set to True in returns a list of the dithered images instead. It also takes frame_num = 3, which
indicates the maximum number of images that the list should have.
- detect_difference: given a list of three images, this function returns an OurImageClass grayscale image representing a map of difference between the 
same pixel number in the three images. If the three images have pixels that are totally different in the three images, the map value at that pixel is higher and 
no more than 512. If the images have a very similar value in all the images, then the map at that point is lower and no less than 0.
- generate_kinegram: This function generates a kinegram from the images in img_list, with each frame having hole_width pixels between eachother.
if different_detection = True, the kinegram will not alternate images where the difference between images (according to detect_difference map) is
less than threshold = 30 and uses the value of the pixel in the second image of the list, otherwise it creates a kinegram in every pixel. If dithered = True, 
 this function returns a grayscale image, otherwise an RGB.

 At the end of the file we included some functions to test the functions in the files locally. In lines 136 to 139, you can uncomment the function
 calls to test the different functionalities. Which will be saved to "Output/dithered_images/" folder for the function that tests dithering and to
 "Output/kinegrams/" folder for the function testing kinegrams.


The Input folder, provides the user photo files to test different functionalities of our code in image.py and creating_kinegram.py. These can be used
to run the code locally and see test results. We used some of these for our test functions in both files, and users are encouraged to change them.


 video.py file 

