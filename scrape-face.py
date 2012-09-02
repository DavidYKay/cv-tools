#!/usr/bin/env python


import os, os.path
from SimpleCV import *

haarcascade = HaarCascade("face")

def gen_filename(x):
  fill = 3
  return "Face-%0*d.jpg" % (fill, x)

for root, dirs, files in os.walk('.'):
  face_counter = 0
  for f in files:
    # for every photo in the directory
    fullpath = os.path.join(root, f)
    image = Image(source=fullpath)
    # find the faces in it
    # save each one as a new face
    faces = image.findHaarFeatures(haarcascade) # load in trained face file
    if faces:
      for face in faces:
        #bb = faces[-1].boundingBox()
        bb = face.boundingBox()
        face_img = image.crop(bb[0],y=bb[1],w=bb[2],h=bb[3])
        face_img.save(gen_filename(face_counter))
        face_counter += 1
