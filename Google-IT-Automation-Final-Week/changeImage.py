#!/usr/bin/env python3

from PIL import Image
import os

path = "/home/student-00-2ba060bb2a28/supplier-data/images/"

files = os.listdir("/home/student-00-2ba060bb2a28/supplier-data/images/")

for img in files:
        if img.endswith(".tiff"):
                outfile = os.path.splitext(img)[0]+".jpeg"
                with Image.open(path+img) as im:
                        if im.mode != 'RGB':
                                im = im.convert('RGB')
                        im = im.resize((600,400))
                        im.save(path+outfile,"JPEG")
