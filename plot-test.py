#matplotlib sample test for sensor data

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np
import random

file = open('data.txt')
contents = file.read() #read in contents of file
#print(contents)

contents = contents.split('\n') # split contents by new lines

#print(contents)

#timelist = list(range(0,638))

#x = np.array(timelist)
x = np.arange(0.0, 5., 1.0) #makes array from 0.0 to 638.0 by a step of 1.0
y = np.array(contents) #converting list to array in python

fig, ax = plt.subplots()

ax.bar(x,y)
#ax.yaxis.set_major_locator(MultipleLocator(20))
#ax.yaxis.set_major_formatter(FormatStrFormatter('%f'))
plt.xlabel('Time') #x axis label
plt.ylabel('Conductivity')#y axis label
plt.title('Conductivity Sensor Graph') #title of graph
#plt.legend()# shows legend to plt
plt.show()

'''fig, ax = plt.subplots() #create a figure containing a single axes
ax.plot([1,2,3,4],[1,2,3,4]) #Plot some data on the axes
plt.xlabel('Time')
plt.ylabel('Conductivity')
plt.show() #shows figure in image viewer
#plt.savefig('test_fig.png')'''