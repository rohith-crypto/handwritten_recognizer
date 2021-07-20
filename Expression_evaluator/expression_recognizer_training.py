
import os

import cv2
import easyocr
import numpy as np
from matplotlib import pyplot as plt

font = cv2.FONT_HERSHEY_SIMPLEX

with os.scandir('images/') as entries:
    for entry in entries:
        IMAGE_PATH = "images/"+entry.name

        reader = easyocr.Reader(['en'])
        result = reader.readtext(IMAGE_PATH)

        
        img = cv2.imread(IMAGE_PATH)
        spacer = 100
        for detection in result: 
            top_left = tuple(detection[0][0])
            bottom_right = tuple(detection[0][2])
            text = detection[1]
            try:
                text=text + " = " + str(eval(text))
            except:
                pass
            
            img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
            img = cv2.putText(img,text,(20,spacer), font, 4,(0,0,0),2,cv2.LINE_AA)
            spacer+=15
            
        plt.imshow(img)
        plt.show()      


