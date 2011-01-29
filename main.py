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
import ImageChops
import math, operator

def main():
    # m1 == m3 # m1 != m2
    originalImageFile = "images\m1.jpg"
    ori = getImage(originalImageFile)
    img = getImage("images\m2.jpg")
    samePercentage = compare(ori,img)
    saveImage(img)

def compare(ori,img):
    #ori = list(ori.getdata())
    #img = list(img.getdata())
    #img = repositionImage(ori,img)
    return img

def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None

def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

def repositionImage(ori,img):
    """
    for each pixel in img:
        for eac
    """
    return img

def getImage(fp):
    img = grayscale(Image.open(fp))
    #img = img.point(lambda i: i * 0.2)
    x,y = img.size
    lvl = 90
    source = img.split()
    # select regions where color is less than lvl
    mask = source[0].point(lambda i: i <= lvl and 255)
    # process the green band
    out = source[0].point(lambda i: i * 0.0)
    # paste the processed band back, but only where color was < 105
    source[0].paste(out, None, mask)
    img = Image.merge(img.mode, source)
    # select regions where color is less than lvl
    mask = source[0].point(lambda i: i > lvl and 255)
    # process the green band
    out = source[0].point(lambda i: i * 100.0)
    # paste the processed band back, but only where color was < 105
    source[0].paste(out, None, mask)
    # build a new multiband image
    img = Image.merge(img.mode, source)
    return img

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
