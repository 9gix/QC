#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      91315
#
# Created:     29/01/2011
# Copyright:   (c) 91315 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import Image

def main():
    # m1 == m3 # m1 != m2
    originalImageFile = "images\m1.jpg"
    ori = getImage(originalImageFile)
    img = getImage("images\m3.jpg")
    samePercentage = compare(ori,img)
    saveImage(img)

def compare(ori,img):
    ori = list(ori.getdata())
    img = list(img.getdata())
    print ori==img

def getImage(fp):
    return grayscale(Image.open(fp))

def grayscale(img):
    return img.convert("L")

def saveImage(image):
    outfile = "output.jpg"
    try:
        image.save(outfile)
    except IOError:
        print "cannot save"

if __name__ == '__main__':
    main()
