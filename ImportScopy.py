''' Created by Konrad on
2016-01-18 Mon 11:56 AM'''

import sys
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

#import pandas as pd

sys.path.append('../functions-konrad/functions-konrad/')
sys.path.append('..')

import FunctionsKonrad as kon
reload(kon)

datadir = '//Volumes/data/Shared/2016/01/18/Lock Graphs/'
fname = 'triangular.csv'

datapath = datadir + fname

a = kon.importMultipleFromTxt(datadir+fname)
np.save('20160113_water.npy',a)

#a = np.load('20160113_water.npy')

#now = np.datetime64('2016-01-13T17:23:00+0000')
#b = a[:,0].astype('timedelta64[s]')
#print b
#b = now-np.timedelta64(a[-1,0].astype(np.int),'s')+b


fig = plt.figure(figsize = (16,9))

ax = fig.add_subplot(111)

ax.plot(a[:,0], a[:,3], 'b-', label = 'Doppler-broadened absorption')
ax.plot(a[:,0], a[:,4], 'r-', label = 'Doppler-free absorption')
ax.plot(a[:,0], a[:,2]/40., 'g-', label = 'Intensity signal')


#plt.ylim(ymin = 40, ymax = 50)
plt.xlim(xmin = 0.07, xmax = 0.21)

plt.title('Rb85 and Rb87 Spectroscopy')
plt.xlabel('Scan/s')
plt.ylabel('Oscilloscope trace/V')
plt.legend(loc = 0)

plt.savefig(datadir + fname[:-4] + '.pdf', format = 'pdf')

plt.show()
