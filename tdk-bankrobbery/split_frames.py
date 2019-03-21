'''
Source: https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57
Wrapping this code as a function to call into other programs
'''

def split_video(filename, path = 'data', ext = '.jpg'):  

    """
    Takes a video as input and outputs every frame as a .jpg image in a subfolder called `path` in the current working directory 
    
    Parameters:
    filename (String): Name of the video file
    path     (String): Directory where the images should be saved
    ext      (String): Output image's format
    
    .
    """
    
    import cv2
    import numpy as np
    import os

    # Playing video from file:
    cap = cv2.VideoCapture(filename)
    
    try:
        if not os.path.exists(path): os.makedirs(path)
    except OSError: print ('Error: Creating directory of data')
    
    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret: break
    
        name = f'./{path}/frame{str(currentFrame)}{ext}'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
    
        # To stop duplicate images
        currentFrame += 1
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()