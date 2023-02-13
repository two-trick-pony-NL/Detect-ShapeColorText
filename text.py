import cv2
import numpy as np
import easyocr

reader = easyocr.Reader(['en'],gpu = False) # load once only in memory.

def findText(image):
    # sharp the edges or image.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
    thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    result=reader.readtext(thresh,detail=0)
    if len(result) == 0:
        return ["no words found"]
    else:
        return result