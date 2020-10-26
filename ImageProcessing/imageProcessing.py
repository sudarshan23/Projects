#!/usr/bin/env python3

from PIL import Image
import os

def imgProcessing(img):
	outfile = "/home/sudarshan/scripts/Project1/TargetImages/images/" + os.path.splitext(img)[0] + ".jpeg"
	infile = "/home/sudarshan/scripts/Project1/SourceImages/images/" + img
	print(outfile)
	with Image.open(infile) as im:
		if im.mode != 'RGB':
			im = im.convert('RGB')
		im = im.rotate(90)
		im = im.resize((128,128))
		im.save(outfile)

def main():
	#files = []
	for d,r,f in os.walk("/home/sudarshan/scripts/Project1/SourceImages/images"):
		continue

	for img in f:
		print(img)
		imgProcessing(img)

if __name__ == "__main__":
	main()
