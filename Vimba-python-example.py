#Vimba Synchronous grab python example
import cv2
from vimba import *
from pathlib import Path #for dealing with filepaths

test = ()

with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()
    with cams[0] as cam:
        settings = Path("C:/Users/lsceedlings/Desktop")
        settomgs = settings / "test.xml"
        cam.load_settings("C:/Users/lsceedlings/Desktop/test.xml", PersistType.All) 
        test = cam.get_pixel_formats()
        print(test)
        #Acquire single frame synchronously
        frame = cam.get_frame()
        #converting pixel format
        frame.convert_pixel_format(PixelFormat.Mono8)
        #saving image as open cv image
        #cv2.imshow('frame.jpg', frame.as_opencv_image())
        #cv2.waitKey()
        cv2.imwrite('frame.jpg', frame.as_opencv_image())
        
        #Acquire ten frames synchronously
        #for frame in cam.get_frame_generator(limit = 10)
            #pass