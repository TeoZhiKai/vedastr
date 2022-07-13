
import re
import matplotlib.pyplot as plt
import os
import numpy as np



# Folder Path


path=["D:/FYPtesting/vedastr/vedastr/workdir/tuning_satrnV2/Trained","D:/FYPtesting/vedastr/vedastr/workdir/tuning_satrnV3/Trained","D:/FYPtesting/vedastr/vedastr/workdir/tuning_satrnV4/Trained"]
 
# Change the directory

iter_incr=50

accuracy = []
loss=[]
edit=[]
acc_=[]
acc_list=[]


def logging(filepath):
    
    
    dataLog = []
    with open(filepath, 'rt') as f:
        data = f.readlines()
    for line in data:
        if 'Train,' in line:
            #print(line)
            dataLog.append(line)
    

    #accuracy = [] 
    for logstep in range(len(dataLog)):
        time,_,_,i,_,l,a,e = dataLog[logstep].split(",")
        accuracy.append(float(re.search(r'\d+\.\d+',a).group())*100)
        loss.append(float(re.search(r'\d+\.\d+',l).group()))
        


    return accuracy  
   


# iterate through all file
for p in path:
    os.chdir(p)
    accuracy=[]
    for file in os.listdir():
        
       
        # Check whether file is in text format or not
        if file.endswith(".log"):
            file_path = f"{p}\{file}"
            
            # call read text file function
            logging(file_path)
    acc_list.append(accuracy)    

end= (len(loss)*iter_incr)


print(len(acc_list))
g1=acc_list[0]
g2=acc_list[1]
g3=acc_list[2]

#print(len(g1))
#print(len(g2))

x_a=np.arange(0, len(g1)*50, iter_incr).tolist()
x_b=np.arange(0, len(g2)*50, iter_incr).tolist()
x_c=np.arange(0, len(g3)*50, iter_incr).tolist()

plt.plot(x_a, g1,color='r', label='1')
plt.plot(x_b, g2,color='g', label='2')
plt.plot(x_c, g3,color='b', label='3')
plt.xlabel('iter')
plt.ylabel('Accuracy - %')
plt.legend()
plt.savefig('acc_com.png')
plt.show()

