#Vimba Synchronous grab python example
from vimba import *

with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()
    with cams[0] as cam:
        #Acquire single frame synchronously
        frame = cam.get_frame()
        
        frame = frame.save("test_image.png")
        
        #Acquire ten frames synchronously
        #for frame in cam.get_frame_generator(limit = 10)
            #pass