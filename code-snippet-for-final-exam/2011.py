#Q1:

def map(f,ls):
    if len(ls)>1:
        return [f(ls[0])]+map(f,ls[1:])
    else:
        return [f(ls[0])]

print map(lambda x:x**2,[1,2,3,4,5])

'''def reduce(f,ls):
    a=f(ls[0],ls[1])
    for i in ls[2:]:
        a=f(a,i)
    return a
'''
def reduce_f(f,ls):
    if len(ls)==1:
        return f(ls[0],ls[1])
    return f(reduce(f,ls[:-1]),ls[-1])

print reduce(lambda a,b:a+b,[1,2,3,4,5])
print reduce_f(lambda a,b:a+b,[1,2,3,4,5])

def fold_right(f,ls):
    a=f(ls[-2],ls[-1])

    b=ls[:-2]
    b.reverse()
    for i in b:
        a=f(i,a)
    return a
def fold_right_f(f,ls):
    if len(ls)>2:
        return f(ls[0],fold_right_f(f,ls[1:]))
    else:
        return f(ls[0],ls[1])

print fold_right(lambda a,b:a*b,[1,2,3,4,5])
print fold_right_f(lambda a,b:a*b,[1,2,3,4,5])

#Q2:

class complex(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return complex(x,y)
    def __mul__(self,other):
        x=self.x*other.x-self.y*other.y
        y=self.x*other.y+self.y*other.x
        return complex(x,y)
    def __str__(self):
        return "< %f + %f i>" %(self.x,self.y)
print complex(1,2)+complex(2,3)
print complex(1,2)*complex(2,3)

#Q3:
#Q4:
def reverse(s):
    if len(s)==1:
        return s[0]
    return reverse(s[1:])+s[0]
def reverse2(s):
    return reduce(lambda a,b:b+a,s)

print reverse("abcde")
print reverse2("abcde")

#Q5:
def vectorize(f):
    def helper(l):
        return map(f,l)
    return helper

vec_f=vectorize(lambda x:x**2)
print vec_f([1,2,3,4])

#Q6:
def func(a):
    sum=[0]*len(a)
    for i in range(len(a)):
        if i==0:
            sum[i]=a[i]
        else:
            sum[i]=sum[i-1]+a[i]
    return sum

import numpy as np
def func_a(a):
    a=np.array(a)
    return np.add.accumulate(a)
def func_f(a):
    def temp(n,a=a):
        n=n+1

        return reduce(lambda a,b:a+b,a[:n])
    return map(temp,range(len(a)))

print func([1,2,3,4,5])
print func_a([1,2,3,4,5])
print func_f([1,2,3,4,5])
print (2,1)+(3,2)

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print a+[[1],[2],[3]],"2333"


print isinstance(object,object)
print isinstance(object,type)
print isinstance(type,type)
print isinstance(type,object)
class A(object):
    pass
class B(type):
    pass
class C(A):
    __metaclass__ = B
class D(C):
    pass
print isinstance(B,type)
print isinstance(B,object)
print issubclass(B,type)
print issubclass(B,object)
print issubclass(A,type)
print issubclass(C,object)
print D.__bases__
print type(C)