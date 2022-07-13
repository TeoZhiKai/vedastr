import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'base model':76.18,'tuning_1':76.47, 'tuning_2':72.69, 'tuning_3':76.23}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='g',
        width = 0.9)
plt.plot(courses, values,color='black',marker='*', ms=10)
plt.margins(x=0, y=+0.25)
plt.xlabel("Model")
plt.ylabel("Accuracy Achieved")
plt.title("Tuning Comparison")
plt.savefig('bar_chart.png')
plt.show()