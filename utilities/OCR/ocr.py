import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
import time
import argparse

import os
import sys


sys.path.append("D:/FYPtesting/vedastr/vedastr/tools/")
#D:\FYPtesting\vedastr\vedastr\tools\test1.py
#D:\FYPtesting\vedastr\vedastr\tools\inference_ocr.py
#from vedastr.vedastr.tools.inference_ocr import main
#from test1 import pr

from inference_ocr import main

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))



def parse_args():
    parser = argparse.ArgumentParser(description='Inference')
    parser.add_argument('config', type=str, help='Config file path')
    parser.add_argument('checkpoint', type=str, help='Checkpoint file path', default='vedastr/vedastr/checkpoint/small_satrn.pth')
    parser.add_argument('image', type=str, help='input image path', default='D:/FYPtesting/vedastr/OCR/input_img/orchard.jpg')
    parser.add_argument('gpus', type=str, help='target gpus',default='0')
    args = parser.parse_args()

    return args


def crop(img,X,Y,W,H):
    cropped_image = img[Y:H, X:W]
    #print([X,Y,W,H])
    #plt.imshow(cropped_image)
    #cv2.imwrite('contour1.png', cropped_image)
    return cropped_image

args = parse_args()
if os.path.isfile(args.image):
        images = [args.image]
else:
    images = [os.path.join(args.image, name)
                for name in os.listdir(args.image)]

print(images)

detector = easyocr.Reader(['en'])
result = detector.detect(images[0])
print(result)

cord_list = result[0][0]
cord=cord_list[0]
print(cord)

image = cv2.imread(images[0])
cv2.rectangle(image,(cord[0],cord[2]),(cord[1],cord[3]),(0,0,255),2)
cimage=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cropped=crop(image,cord[0],cord[2],cord[1],cord[3])

#pr()
pred_text=main(cropped,args.config,args.gpus,args.checkpoint)
#a_image,config,gpus,checkpoint
#print(pred_text)
org = (cord[0]-1,cord[0]-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cimage = cv2.putText(image, pred_text[0], org, font, 
                   1, (0, 0, 255), 2, cv2.LINE_AA)




cv2.imwrite('result.png', cimage)
cv2.imshow("image", cimage)
cv2.waitKey(0) 






#closing all open windows 
cv2.destroyAllWindows() 


# test run
#python ocr.py configs/small_satrn_modifiedV4.py D:\FYPtesting\vedastr\vedastr\workdir\small_satrn_modifiedV4\best_acc_86.pth D:/FYPtesting/vedastr/OCR/input_img/orchard.jpg "0"