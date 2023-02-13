import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# reading image


def findShape(img):
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
    contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    shapes = []

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
        elif len(approx) == 4 :
            x, y , w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            #print(aspectRatio)
            if aspectRatio >= 0.95 and aspectRatio < 1.05:
                shapes += ['square']


            else:
                shapes += ['rectangle']

        elif len(approx) == 5 :
            shapes += ['pentagon']
        elif len(approx) == 10 :
            shapes += ['star']
        else:
            shapes += ['circle']

    return shapes