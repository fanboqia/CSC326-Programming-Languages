#Q1: no idea
#Q2: 6789

#Q3:
def foo():
    for i in range(10):
        yield i
gen=foo()
print gen==0
#print gen()==0 Error
print gen.next()==0
print gen.next()==2
print reduce (lambda a,b:a+b,gen)

print "-----------------------------"

#Q4: not sure how to normalize....
import numpy as np
import math
def normalize(A):


    ar=np.array(A)
    ar_=ar**2
    ar_=np.add.reduce(np.add.reduce(ar_))
    mag=math.sqrt(ar_)
    ar=ar/mag
    return ar

print normalize(np.random.random((5,5)))
print "-----------------------------"

#Q5
def mv(A,X,n):
    Y=[0]*n
    for i in range(n):
        for j in range(n):
            Y[i]+=A[i][j]*X[j]
    return Y

def mv_a(A,X,n):
    X=X[:n]


    X=X*n
    X_r=np.array(X)
    X_r=X_r.reshape(-1,n)
    A_r=np.array(A)
    A_r=A_r[:n,:n]
    result=A_r*X_r
    result_t=result.transpose()
    Y=np.add.reduce(result_t)
    return list(Y)

def mv_f(A,X,n):
    def helper(l,x=X,dim=n):
        l=l[:dim]
        x=x[:dim]
        return reduce(lambda x,y:x+y,map(lambda a,b:a*b,l,x))

    return map(helper,A)[:n]

print mv([[1,2,3],[1,5,3],[1,2,7]],[20,20,30],2)
print mv_a([[1,2,3],[1,5,3],[1,2,7]],[20,20,30],2)
print mv_f([[1,2,3],[1,5,3],[1,2,7]],[20,20,30],2)
print "-----------------------------"

#Q6
def memorize(func):
    memory={}
    def new(*args):
        print args
        if args in memory:
            return memory[args]
        else:
            result=func(*args)
            memory[args]=result
            return result
print "-----------------------------"
#Q7 ...whatever easton has tried his best
def top_two(l):
   try:
        if l[0]<=l[1] and l[0]<=l[2]:
            return top_two(l[1:])
        if l[1] <= l[0] and l[1] <= l[2]:
            return top_two([l[0]]+l[2:])
        else:
            return top_two(l[0:2]+l[3:])
   except IndexError:
       return l

print top_two([0,11,4,125,90,10])
