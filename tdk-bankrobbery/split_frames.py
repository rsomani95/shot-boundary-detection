'''
Source: https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57
Wrapping this code as a function to call into other programs
'''

def split_video(filename, path = 'data', ext = '.jpg', verbose = False):  

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
    src = cv2.VideoCapture(filename)
    
    fps = src.get(cv2.CAP_PROP_FPS)
    print(f"Frame Rate = {fps}")
    
    try:
        if not os.path.exists(path): os.makedirs(path)
    except OSError: print ('Error: Creating directory of data')
    
    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = src.read()
        
        if not ret: break
    
        name = f'./{path}/frame{str(currentFrame)}{ext}'
        
        # prints for every 1 second worth of frames extracted
        if verbose:
            if (currentFrame % int(fps) == 0): print ('Creating...' + name)
                
        cv2.imwrite(name, frame)
    
        # To stop duplicate images
        currentFrame += 1
    
    print(f"Created {currentFrame} frames")
    
    # When everything done, release the captured source video
    src.release()
    cv2.destroyAllWindows()