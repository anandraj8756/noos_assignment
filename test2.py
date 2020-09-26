import numpy as np
import cv2
from pylibdmtx import pylibdmtx



if __name__ == '__main__':

    image = cv2.imread('datamatrix_sample3_130x116.png', cv2.IMREAD_UNCHANGED);

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('datamatrix_sample3_130x116.png', gray)

    ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    msg = pylibdmtx.decode(thresh)
    print(msg)

    cv2.waitKey(0)


 # here we have to change to imput image then it will give the decded output 
 #of the input image
 #All the output i have taken screenshot and uploaded output folder   