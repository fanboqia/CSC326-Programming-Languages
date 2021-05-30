# def qsort(s) :
#     if( len(s) <= 1 ) : return s
#     pivot = s[0]
#     less = [e for e in s if e < pivot]
#     grt =[e for e in s if e > pivot]
#     eq = [e for e in s if e == pivot]
#     return qsort(less) + eq + qsort(grt)
# print qsort( [1, 2, 1, 5, 3, 4, 4] )

import numpy as np
from numpy import *
a = arange(10).reshape(2,5)
print type(a.shape)
print a.itemsize
print a.size
print a

print np.array([(1,2),(3,4)])

print np.zeros((3,4),dtype = int16)

print np.arange(0,30,5)

print np.arange(0,30,0.3)

print np.linspace(0,2,5)  #5-1 = 4      2/4 = 0.5


x = np.linspace(0,2*pi,101)

y = sin(x)

b = np.array([[1,2,3],[4,5,6]])
print b.ravel()
b.shape = (3,2)
print b
print b.transpose()
print b.resize((3,2))
print b.reshape(-1,3)