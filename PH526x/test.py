# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:43:08 2018

@author: bob
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.array([0.,0.,0.,0.,0.])
print(a)
b = np.zeros(5)
print(b)
x = np.array([1,2,5])
print(x)
print(x[0:1])
a= np.array([1,2])
b = np.array([3,4,5])
c = b[1:]
print(c)
print(b[a] is c)

plt.plot([0,1,2],[0,1,4],"rd-") 

x=np.logspace(0,1,10)
y=x**2
plt.loglog(x,y,"bo-") 

plt.subplot(333) 
#plt.subplot(222) 