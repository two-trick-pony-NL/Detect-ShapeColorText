import cv2
from shape import findShape
from text import findText
from color import findColor
import timeit


starttime = timeit.default_timer()
img = cv2.imread('images/multi.png')
print("\n")
print("\n")
print("\n")
print("#### RESULTS ####")
print("\n")
print("🔸 I found these shapes:")
for i in findShape(img):
    print('--- '+i)
print("\n")
print("💬 I found these words:")    
for j in findText(img):
    print('--- '+j)
print("\n")
print("🎨 The dominant color is (RGB) ")
print("---", str(findColor(img)[0]))
print("---", str(findColor(img)[1]))
print("\n")
print("⏱ This calculation took :", timeit.default_timer() - starttime, " Seconds")
print("\n")
print("\n")
print("\n")