# kineCAM

Welcome to **kineCAM**!

[![Alt text](https://img.youtube.com/vi/6bRIexfb4wg/0.jpg)](https://www.youtube.com/watch?v=6bRIexfb4wg)

This code works with a Raspberry Pi to take photos of a camera, produce kinegrams out of photos taken 1 second apart from eachother, and print the resulting kinegram in a receipt printer.


**image.py** file has a OurImageClass, which we built and use to manipulate our images. This class has different functionalities that allow us to:
- Initialize an image into a class from another format like nparray, PIL and jpg.
- Set and get pixel values
- Save image as PNG, BMP or PIL
- Manipulate the image changing its brightness and contrast

At the end of the file we included some functions to test our Class locally, in lines 204-206 you can uncomment to run the different functions and their output will be saved to the 'Output/image_manipulation/' folder.


**creating_kinegram.py** file has all of the functions needed to create the clearest kinegram. Different functions have different functionalities
- grayscale: returns a grayscale image of OurImageClass when given the same image in RGB.
- ditheredRGBtoBW: given an RGB image in OurImageClass, it dithers it and returns the resulted dither.
- ims_from_frames: given a folder name with images, this function returns a list of OurImageClass images of the images in the folder. This function takes additional parameter dithered = False, and when set to True in returns a list of the dithered images instead. It also takes frame_num = 3, which indicates the maximum number of images that the list should have.
- detect_difference: given a list of three images, this function returns an OurImageClass grayscale image representing a map of difference between the same pixel number in the three images. If the three images have pixels that are totally different in the three images, the map value at that pixel is higher and no more than 512. If the images have a very similar value in all the images, then the map at that point is lower and no less than 0.
- generate_kinegram: This function generates a kinegram from the images in img_list, with each frame having hole_width pixels between eachother. if different_detection = True, the kinegram will not alternate images where the difference between images (according to detect_difference map) is less than threshold = 30 and uses the value of the pixel in the second image of the list, otherwise it creates a kinegram in every pixel. If dithered = True, this function returns a grayscale image, otherwise an RGB.

 At the end of the file we included some functions to test the functions in the files locally. In lines 142 to 145, you can uncomment the function calls to test the different functionalities. Which will be saved to "Output/dithered_images/" folder for the function that tests dithering and to "Output/kinegrams/" folder for the function testing kinegrams.


**Input** folder, provides the user photo files to test different functionalities of our code in image.py and creating_kinegram.py. These can be used to run the code locally and see test results. We used some of these for our test functions in both files, and users are encouraged to change them.


**take_vid.py** file handles the taking of the video by the picamera. Its function video_to_frames takes in three arguements, camera, num_seconds and num_frames. camera corresponds to the camera being used, which in our case is the picamera, and num_seconds corresponds to the number of seconds the video will take. This function calls the helper function get_allowed to get the frames that will be picked from the video taken according to num_seconds and num_frames. It then saves num_frames of the video to our Output folder.


 **new_video.py** file handles taking a video and saving num_frames of that video that will be used in our kinegram and sending the print command to the receipt printer. The file has a Video class with a capture_kinegram function that takes num_frames images my calling take_vid.py in an interval of num_seconds second using picamera. It stores these images in an nparray and uses our OurImageClass to make turn this nparrays into images of our class. It then uses our generate_kinegram function to create a kinegram of the frames. It then sends a command to our receipt printer to print the kinegram image. Note that running the code with dithering and/or difference detection takes significantly more time.


 **gpio_button.py** this function is what is called upon starting the Raspberry Pi. It controls the button that allows our capture_kinegram function in video.py to run. It is an infinite loop that looks for a press in our button. Once it is pressed it calls the capture_kinegram function and allows for all of that process to run and so print a kinegram from our live images. The kinegrams created will also be available in the "Output/live/" folder. In this file, you can change all of the parameters of the code to create different outputs.
 - num_frames: takes in an int value and corresponds to the number of frames the final kinegram will have, we set it to 3 which we tested and observed produced the best results balancing motion and quality of the image but it can be changed to any integer greter than 0 and less than num_seconds * 32 since that is the maximum number of frames our video will produce.
 - hole_width: is the number of pixels each frame should have. This means that in the final kinegram, we can see hole_width rows of pixels of one frame, then hole_width of the next frame and so on. We set it to hole_width = 3 which we observed had the best results, but it can take any int value greater than 0 and less than 320//num_frames. Because the final image has a width of 320 pixels and we want to at least have a visible part of each frame. Note that the greater the value the lower the sensation of motion of the kinegram.
 - difference_detection and threshold: this parameter defines if we use our differnce_detection method in creating_kinegram.py which accounts for parts of the image that are static and prints out a static image in that area. If difference_detection = True it will call the function and use threshold as the pixel_difference threshold that decides whether a part of an image is static (if less than threshold difference) or in motion. Setting threshold to 0 means all pixels are considered to be in motion and a very high threshold means that it will probably all be static and produce a static image as kinegram. Our default value is 30 which we considered produced good results. Note that running the code with difference_detection = True significantly increases the runtime of the code and depending on the battery used could even lead to errors in the execution. We recommend setting this to False the first time testing.
 - num_seconds: corresponds to the number of seconds we want the recording to happen in. This value must be an int greater than 0. Our preset value is 1 second, which we tested and showed good result for the creation of a kinegram from frames that appeared to be in motion. Increasing this parameter a lot will create a kinegram of frames that do not necesarily appear to be in motion since they are taken very far away from each other.


The code is currently automated to run upon startup of the raspberry pi (plugging into the power bank). To turn off automation, ssh into the pi and run the command line "sudo crontab -e," and comment out the last line of this file. Then run "sudo reboot.


To test the kinegrams online, we have included the **Testing_Kinegrams folder** with Testing_Kinegrams.pde Processing file. Running the file in Processing 5 will allow the user to see if the kinegram works. The input image needs to be added to the data folder and the filename changed in line 8. The size of the image should also be changed correspondly in line 7 and the hole_w to whatever parameter was used for hole_width when calling the generate_kinegram function, and the slit_w to (frame_num - 1)*hole_w. Where frame_num is the number of frames used in the kinegram.


Enjoy using **kineCAM**!
