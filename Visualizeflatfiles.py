# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:18:11 2017

@author: noelg
"""

#PART 1 VISUALIZE FLAT FILE

import csv

x = []
y = []



with open ('C:/Users/noelg/Desktop/example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',' )
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot (x,y, label = 'loaded data')


#PART2

import numpy as np

x,y =np.loadtxt ('C:/Users/noelg/Desktop/example.txt', 
                 delimiter = ',', 
                 unpack = True)
plt.plot (x,y, label = 'loaded data')