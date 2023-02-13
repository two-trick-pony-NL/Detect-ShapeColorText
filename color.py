
from sklearn.cluster import KMeans
from collections import Counter
import cv2 #for resizing image
from webcolors import rgb_to_name
import webcolors
import warnings
warnings.filterwarnings("ignore")

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def findColor(image, k=4, image_processing_size = None):
    #resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image, image_processing_size, 
                            interpolation = cv2.INTER_AREA)
    
    #reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    #cluster and assign labels to the pixels 
    clt = KMeans(n_clusters = k)
    labels = clt.fit_predict(image)

    #count labels to find most popular
    label_counts = Counter(labels)

    #subset out most popular centroid
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    colorlist = list(dominant_color)
    try: 
        color = rgb_to_name((round(colorlist[2]),round(colorlist[1]), round(colorlist[0])))
    except: 
         color = closest_colour((round(colorlist[2]),round(colorlist[1]), round(colorlist[0])))
    
    rgb = [round(colorlist[2]),round(colorlist[1]), round(colorlist[0])]
    
    return color, rgb