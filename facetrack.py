#!/usr/bin/python
'''
This program is modified from the face-blrring facetrack example in SimpleCV.
It shows the face in the top left when a face is found.
'''
print __doc__

import time
from SimpleCV import *

FACE_OFFSET = (5, 5)

LOGO = Image("simplecv").crop(0, y=0, w=50, h=50)

cam = Camera() #initialize the camera

haarcascade = HaarCascade("face")
# Loop forever
while True:
    image = cam.getImage().flipHorizontal().scale(0.5) # get image, flip it so it looks mirrored, scale to speed things up
    faces = image.findHaarFeatures(haarcascade) # load in trained face file
    if faces:
        bb = faces[-1].boundingBox()
        #image = image.pixelize(10,region=(bb[0],bb[1],bb[2],bb[3]))
	#image.drawText("Face Detected")
	image.drawText(text="Face Detected",
                x=image.width  - 100,
                y=image.height - 20,
                )
        image.getDrawingLayer().blit(image.crop(bb[0],y=bb[1],w=bb[2],h=bb[3]),
                                     FACE_OFFSET) #draw the cropped image onto the current image
        #image.blit(LOGO)
        #image.getDrawingLayer().blit(LOGO, (30, 30)) #draw the cropped image onto the current image
    image.show() #display the image
