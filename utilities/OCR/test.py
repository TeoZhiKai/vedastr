
import matplotlib.pyplot as plt

import cv2
#test=([[[140, 946, 304, 608]]], [[[[790.9468755654001, 702.1112552016804], [1108.2464368646947, 671.1484372203447], [1111.0531244346, 831.8887447983196], [793.7535631353053, 861.8515627796553]], [[200.82089210036585, 782.2029583828537], [791.2259041294647, 696.5540755887588], [803.1791078996341, 909.7970416171463], [212.77409587053535, 994.4459244112412]]]])
#test=([[[53, 312, 67, 120], [121, 209, 264, 278], [213, 273, 265, 279]]], [[]])
test=([[[86, 416, 104, 156], [125, 375, 321, 389]]], [[[[218.3500052999841, 221.76000847997457], [299.7307065064177, 201.67106188658113], [309.6499947000159, 246.23999152002543], [227.26929349358232, 266.3289381134189]], [[150.6712678358369, 242.5754088880901], [225.71647073123583, 225.65517634188774], [233.3287321641631, 270.42459111190993], [158.28352926876417, 286.34482365811226]]]])




#print(len(test))
#print(test)

#print(test[0][0][0])

cord_list=[]

for outer in range(len(test)):
    #print(test[outer])           
    try:                                                    # if the format is free_list
        o_i=outer
        #print(len(test[outer][0]))
        for inner_f in range(len(test[outer][0])):
            cord=test[o_i][0][inner_f]
            x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
            x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
            x=[x_min, y_min,x_max, y_max]
            cord_list.append(x)
            #print(x)
    except:                                                         # if the format is horizontal_list
        for inner_h in range(len(test[outer][0])):
            x=test[outer][0][inner_h]
            #print(x[0])
            x_f=[x[0],x[2],x[1],x[3]]
            cord_list.append(x_f)

print(cord_list)
image = cv2.imread('input_img/sign.jpg')
for t_dect in range(len(cord_list)):
    cord=cord_list[t_dect]
    cv2.rectangle(image,(cord[0],cord[1]),(cord[2],cord[3]),(0,0,255),2)
    cimage=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow("image", cimage) 
cv2.waitKey(0)  

# cord=test[1][0][1]
# x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
# x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
# x=[x_min, y_min,x_max, y_max]
# print(x)


# image = cv2.imread("input_img/sample2.jpg")
# #image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.rectangle(image,(x[0],x[1]),(x[2],x[3]),(0,0,255),2)



# cv2.imshow("image", image)
# cv2.waitKey(0) 