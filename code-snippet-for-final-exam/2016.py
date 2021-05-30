def foo():
    for i in range(10):
        yield i

gen=foo()
print gen
print (gen==0,gen.next()==0,gen.next()==1,reduce(lambda a,b:a+b,gen))


print '------------------------------------------'
class A(object):
    pass
class B(A):
    pass
class C(B):
    pass
a=A()
b=B()
c=C()
l=[]

print isinstance(a,A)
print isinstance(c,A)
print issubclass(B,A)
print isinstance(A,B)
print isinstance(a,C)
print isinstance(l,object)
print isinstance(c,object)
print 'asdasd', isinstance(A,object)
print 'asdasdasda', isinstance(A,type)

print "________"

print issubclass(object,type)
print issubclass(type,object)
print isinstance(object,type)
print isinstance(type,object)

print "asdasd", type.__class__
print "asdasd", object.__class__
print "asdasd", None.__class__


print '------------------------------------------'
class Point(object):
    def __str__(self):
        return "(x:%s,y:%s,z:%s)"%(self.x,self.y,self.z)
    def __gt__(self, other):
        from math import sqrt
        if sqrt(self.x**2+self.y**2+self.z**2)<=sqrt(other.x**2+other.y**2+other.z**2):
            return False
        else:
            return True
    def __lt__(self, other):
        from math import sqrt
        if sqrt(self.x**2+self.y**2+self.z**2)>=sqrt(other.x**2+other.y**2+other.z**2):
            return False
        else:
            return True
    def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c

p=Point(3,4,5)
print p
print Point(3,5,6)>Point(3,5,6)
print Point(1,2,3)<Point(3,1,5)

print '------------------------------------------'

def helper(l,str):
    temp_len=len(l)
    str.append("[%s:"%temp_len)

    for temp in range(temp_len):
        if isinstance(l[temp],list):
            helper(l[temp],str)

        else:
            str.append("%s,"%l[temp])

def pickle(l):
    str=[]
    helper(l,str)
    return "".join(str)



listi=[0]

def string_int(l):
    temp=int(l[listi[0]])
    listi[0] = listi[0] + 1
    while (l[listi[0]]!=':' and l[listi[0]]!=','):
        temp=temp*10+int(l[listi[0]])
        listi[0]=listi[0]+1
    return temp

def helper2(l):

    list=[]

    if l[listi[0]]=="[":
        listi[0]=listi[0]+1
        len_l=string_int(l)

        for k in range(int(len_l)):

            listi[0]=listi[0]+1
            if l[listi[0]]=="[":
                list.append(helper2(l))
            else:
                 list.append(string_int(l))

    return list

def unpickle(list):
    listi[0]=0
    return helper2(list)

print pickle([1,[[2],45],[3,4]])
print pickle([12,[1234,5,[6]],123,[[0],1,2]])
print unpickle(pickle([1,[[2],45],[3,4]]))
print unpickle(pickle([12,[1234,5,[6]],123,[[0],1,2]]))

print '------------------------------------------'


def dynamic(func):
    memory = {}
    def new(a,b):
        if (a,b) in memory:
            return memory[(a,b)]
        else:
            result=func(a,b)
            memory[(a,b)]=result
            #print memory
            return result

    return new

profile={}
def counter(func):
    def new(*args):
        if func.__name__ in profile:
            profile[func.__name__]= profile[func.__name__]+1
        else:
            profile[func.__name__] = 1
        return func(*args)
    return new


@dynamic
@counter
def factorial(n,b):

    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return n*factorial(n-1,b)

@dynamic
@counter
def fibonacci(n,a):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return fibonacci(n-1,1)+fibonacci(n-2,1)


#print factorial(7,2)
#print fibonacci(20,1)
print profile


@dynamic
@counter
def choice(n,k):
    if k==0 or k==n:
        return 1
    else:
        return choice(n-1,k)+choice(n-1,k-1)

c=choice(4,2)
print profile['choice']


@counter
def choice(n,k):
    if k==0 or k==n:
        return 1
    else:
        return choice(n-1,k)+choice(n-1,k-1)

c=choice(4,2)
print profile['choice']


print '------------------------------------------'

a=[x+" "+y+" "+z for x in ["I","You"] for y in ["Play","Love"] for z in ["Hockey","Football"]]
print a

# not sure what is generator comprehension
b=(x+" "+y+" "+z for x in ["I","You"] for y in ["Play","Love"] for z in ["Hockey","Football"])
for i in b:
    print i

print '------------------------------------------'
def func(k,n):
    if n==1:
        k(1)
    else:
        func(lambda x:k(n*x),n-1)

def p(n):
    print(n)

func(p,5)

print '------------------------------------------'

def degree(A):
    n=len(A)
    t=[]
    for i in range(n):
        d=0
        for j in range(n):
            d+=A[i][j]
        t.append(d)
    return t

#array programming
from numpy import *
def degree_a(A):
    A_r=array(A)
    t=[]
    A_t=A_r.transpose()
    t=add.reduce(A_t)
    return list(t)

#functional programming
def degree_f(A):
    def add_row(l):
        return reduce(lambda a,b:a+b, l)
    return map(add_row,A)

A=[[1,2,3],[4,5,6],[7,8,9]]
print degree(A)
print degree_a(A)
print degree_f(A)