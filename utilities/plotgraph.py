
import re
import matplotlib.pyplot as plt
import os
import numpy as np

#filepath = 'D:/FYPtesting/vedastr/vedastr/workdir/small_satrn/20211209_122731.log'

# Folder Path
path = "D:/FYPtesting/vedastr/vedastr/workdir/tuning_satrnV2/Trained"
#path = "D:/FYPtesting/vedastr/vedastr/workdir/tps_resnet_bilstm_attn/Trained"
#path = "D:/FYPtesting/vedastr/vedastr/workdir/small_satrn_modified/Trained"  
#path = "D:/FYPtesting/vedastr/vedastr/workdir/small_satrn_modifiedV4/Trained"  
# Change the directory

iter_incr=50

os.chdir(path)
accuracy = []
loss=[]
edit=[]


def logging(filepath):
    dataLog = []
    with open(filepath, 'rt') as f:
        data = f.readlines()
    for line in data:
        if 'Train,' in line:
            #print(line)
            dataLog.append(line)
    # print(dataLog[2])
    #time,_,_,i,_,l,a,e = dataLog[0].split(",")
    #print(i)
    #print(a)

    #accuracy = [] 
    for logstep in range(len(dataLog)):
        #print(dataLog[logstep])
        time,_,_,i,_,l,a,e = dataLog[logstep].split(",")
        #accuracy.append(a.split(" "))
        #iter.append(float(re.search(r'\d+\.\d+',i).group()))
        accuracy.append(float(re.search(r'\d+\.\d+',a).group())*100)
        loss.append(float(re.search(r'\d+\.\d+',l).group()))
        edit.append(float(re.search(r'\d+\.\d+',e).group()))
        
    #print(iter)


# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".log"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        logging(file_path)

end= len(loss)*iter_incr
#print(end)

x_a=np.arange(0, end, iter_incr).tolist()
#print(x_a)
plt.plot(x_a, accuracy)
plt.xlabel('iter')
plt.ylabel('Accuracy - %')
plt.savefig('acc.png')
plt.show()
plt.plot(x_a, loss)
plt.xlabel('iter')
plt.ylabel('Loss')
plt.savefig('loss.png')
plt.show()
plt.plot(x_a, edit)
plt.xlabel('iter')
plt.ylabel('edit')
plt.savefig('edit.png')
plt.show()






# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

# x = [0,5,9,10,15]
# y = [0,1,2,3,4]
# fig, ax = plt.subplots()
# ax.plot(x,y)
# start, end = ax.get_xlim()
# ax.xaxis.set_ticks(np.arange(start, end, 0.712123))
# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
# plt.show()


# dataLog = []
# with open(filepath, 'rt') as f:
#     data = f.readlines()
# for line in data:
#     if 'Train,' in line:
#         #print(line)
#         dataLog.append(line)
# # print(dataLog[2])
# # time,_,_,_,_,l,a,e = dataLog[0].split(",")
# # print(a)

# accuracy = [] 
# for logstep in range(len(dataLog)):
#     #print(dataLog[logstep])
#     time,_,_,_,_,l,a,e = dataLog[logstep].split(",")
#     #accuracy.append(a.split(" "))
#     accuracy.append(float(re.search(r'\d+\.\d+',a).group())*100)
    

# #print(accuracy)



# plt.plot(range(len(accuracy)), accuracy)
# plt.show()