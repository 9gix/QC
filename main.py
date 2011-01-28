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
    fp = "images\m1.jpg"
    img = Image.open(fp)
    img = img.convert("L")
    saveImage(img)

def saveImage(image):
    outfile = "output.jpg"
    try:
        image.save(outfile)
    except IOError:
        print "cannot save"

if __name__ == '__main__':
    main()
