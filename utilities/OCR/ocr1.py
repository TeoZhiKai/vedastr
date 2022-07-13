import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
import time
import argparse

import os
import sys

##error list 
sys.path.append("D:/FYPtesting/vedastr/vedastr/tools/")
#D:\FYPtesting\vedastr\vedastr\tools\test1.py
#D:\FYPtesting\vedastr\vedastr\tools\inference_ocr.py
#from vedastr.vedastr.tools.inference_ocr import main
#from test1 import pr

from inference_ocr import main

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

cord_list=[]

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


def process_cord(i_cord):
    cord_list=[]

    for outer in range(len(i_cord)):
        #print(test[outer])           
        try:                                                    # if the format is free_list
            o_i=outer
            #print(len(test[outer][0]))
            for inner_f in range(len(i_cord[outer][0])):
                cord=i_cord[o_i][0][inner_f]
                x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
                x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
                x=[x_min, y_min,x_max, y_max]
                cord_list.append(x)
                #print(x)
        except:                                                         # if the format is horizontal_list
            for inner_h in range(len(i_cord[outer][0])):
                x=i_cord[outer][0][inner_h]
                #print(x[0])
                x_f=[x[0],x[2],x[1],x[3]]
                cord_list.append(x_f)
    return cord_list


args = parse_args()
if os.path.isfile(args.image):
        images = [args.image]
else:
    images = [os.path.join(args.image, name)
                for name in os.listdir(args.image)]

#print(images)

detector = easyocr.Reader(['en'])
result = detector.detect(images[0],text_threshold=0.8)
#print(result)


proc_cl=process_cord(result)
print(proc_cl)


# cord_list = result[0][0]
# print(cord_list)
# #cord=cord_list[0]
# print(len(cord_list))


croplist=[]
image = cv2.imread(images[0])
for t_dect in range(len(proc_cl)):
    cord=proc_cl[t_dect]
    cv2.rectangle(image,(cord[0],cord[1]),(cord[2],cord[3]),(0,0,255),2)
    cimage=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cropped=crop(image,cord[0],cord[1],cord[2],cord[3])
    croplist.append(cropped)

#print(croplist)
# cv2.imshow("image", cimage) 
# cv2.waitKey(0)   


pred_text_list=main(croplist,args.config,args.gpus,args.checkpoint)
#a_image,config,gpus,checkpoint

print(pred_text_list)



for i in range(len(pred_text_list)):
    cord=proc_cl[i]
    org = (cord[0],cord[1])
    font = cv2.FONT_HERSHEY_SIMPLEX
    cimage = cv2.putText(image, pred_text_list[i][0], org, font, 
                    1, (0, 0, 255), 2, cv2.LINE_AA)




cv2.imwrite('result.png', cimage)
cv2.imshow("image", cimage)
cv2.waitKey(0) 






#closing all open windows 
cv2.destroyAllWindows() 


# test run
#python ocr.py configs/small_satrn_modifiedV4.py D:\FYPtesting\vedastr\vedastr\workdir\small_satrn_modifiedV4\best_acc_86.pth D:/FYPtesting/vedastr/OCR/input_img/orchard.jpg "0"
#python ocr1.py configs/small_satrn_modifiedV4.py D:\FYPtesting\vedastr\vedastr\workdir\small_satrn_modifiedV4\best_acc_86.pth D:/FYPtesting/vedastr/OCR/input_img/sign.jpg "0"