import numpy as np
#__________________________________________________________
def my_map(function, iterable):
    if iterable == None:
        return []
    if function == None:
        return [i for i in iterable]
    return [function(i) for i in iterable]

def my_filter(function, iterable):
    if iterable == None:
        return None
    if function == None:
        return iterable
    if type(iterable) == str:
        return ''.join([i for i in iterable if function(i)])
    if type(iterable) == tuple:
        return tuple([i for i in iterable if function(i)])
    # a list iterable
    return [i for i in iterable if function(i)]

def my_reduce(function, iterable):
    if function == None:
        return iterable
    if iterable == None:
        return None

    i = iter(iterable)
    result_accu = i.next()
    for item in i:
        result_accu = function(result_accu, item)
    return result_accu
#__________________________________________________________

    checkRange = range(len(l)-4)
    print 'step 0 get valid range: ', checkRange
    #step 1 get range combination list
    indexRangeList = map(lambda x: [x,x+5],checkRange)
    print 'step 1 get range combination list:', indexRangeList
    #step 2 get range corresponding list of number
    rangeNumber = map(lambda x: l[x[0]:x[1]], indexRangeList)
    print 'step 2 get range corresponding list of number: ', rangeNumber
    #step 3 calculate each list product
    rangeProduct = map(lambda list: reduce(lambda x,y : x*y, list), rangeNumber)
    print 'step 3 calculate each list product: ', rangeProduct
    #step 4 find the maximum product
    maxProduct = max(rangeProduct)
    print 'step 4 find the maximum product: ', maxProduct
    return rangeProduct.index(maxProduct), maxProduct

#__________________________________________________________
print np.sum(arr, axis = 1)

print [arr[i][j] if j == i else 0 for i in range(len(arr)) for j in range(len(arr))]

print [[arr[i][j] for j in range(len(arr))] for i in range(len(arr))]

print [arr[i][j] for i in range(len(arr)) for j in range(len(arr))]

print [sum([arr[i][j] for j in range(len(arr))]) for i in range(len(arr))]

#______________________pickle______________________________
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
#__________________________________________________________
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
#__________________________________________________________
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
#__________________________________________________________
def walk(dir) :
    for name is os.listdir(dir) :
        path = os.path.join( dir, name )
        if os.path.isfile(path) :
           print path
        else
walk(path)
#__________________________________________________________
def pr(s): return s
(x==1 and pr('one')) or (x==2 and pr('two')) or (pr('other'))

 namenum = lambda x: (x==1 and pr("one")) \
     or (x==2 and pr("two")) \
     or (pr("other"))

# utility function for "identity with side-effect"
def monadic_print(x):
    print x
    return x
# FP version of "echo()"
echo_FP = lambda: monadic_print(raw_input("FP -- "))=='quit' or echo_FP()
echo_FP()

#--- Functional Python code for "print big products" ----#
bigmuls = lambda xs,ys: filter(lambda (x,y):x*y > 25, combine(xs,ys))
combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
print bigmuls((1,2,3,4),(10,15,3,22))

#What is Currying?
#Currying is like a kind of incremental binding of function arguments.

# continuation-passing-style (CPS) with exception handling
def cps_factorial_with_except( n, ret, err ) :
    if n < 0 :
        err( n )
    elif n == 0 :
        ret( 1 )
    else :
        cps_factorial_with_except( n-1, lambda t0:ret(n*t0), err )
def error( n ) :
    print "exception handled ", n
cps_factorial_with_except( 5, pr, error )
cps_factorial_with_except( -1, pr, error )
#__________________________________________________________
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
#__________________________________________________________
def reverse(s):
    if len(s)==1:
        return s[0]
    return reverse(s[1:])+s[0]
def reverse2(s):
    return reduce(lambda a,b:b+a,s)

wordFrequency = {}
wordList = []
#__________________________________________________________
def lineIterator(filename):
    f = open(filename,'r')

    for line in f.readlines():
        wordList = line.split()

    # print '_____wordlist:', wordList

    for word in wordList:
        if word not in wordFrequency:
            wordFrequency[word] = 1
        else:
            wordFrequency[word] += 1
    
    # print '_____wordFrequency:', wordFrequency

    sortedDic = sorted(wordFrequency.items(), key = lambda x : x[1] , reverse = True)

    # print '_______sortedDic: ', sortedDic

    return map(lambda x: x[0], sortedDic[:10])

print '______top 10 frequent word: ', lineIterator('q5File.txt')
#__________________________________________________________
memo = {}
def memfib(n,l):
    l.append(n)
    print l
    if n == 0 or n == 1:
        memo[n] = n
    if n not in memo:
        memo[n] = memfib(n-1,l)+memfib(n-2,l)
    return memo[n]
print memfib(6,[])  
#__________________________________________________________
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
#__________________________________________________________
# countdown.py
#
# A simple generator function

def countdown(n):
    print "Counting down from", n
    while n > 0:
        yield n
        n -= 1
    print "Done counting down"

# Example use
if __name__ == '__main__':
    for i in countdown(10):
        print i
#__________________________________________________________
# follow.py
#
# A generator that follows a log file like Unix 'tail -f'.
#
# Note: To see this example work, you need to apply to 
# an active server log file.  Run the program "logsim.py"
# in the background to simulate such a file.  This program
# will write entries to a file "access-log".

import time

import time
def follow(thefile):
    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         yield line

# Example use
if __name__ == '__main__':
    logfile = open("access-log")
    for line in follow(logfile):
        print line,
#__________________________________________________________
# pipeline.py
#
# An example of setting up a processing pipeline with generators

def grep(pattern,lines):
    for line in lines:
        if pattern in line:
             yield line

if __name__ == '__main__':
    from follow import follow

    # Set up a processing pipe : tail -f | grep python
    logfile  = open("access-log")
    loglines = follow(logfile)
    pylines  = grep("python",loglines)

    # Pull results out of the processing pipeline
    for line in pylines:
        print line,
#__________________________________________________________
# grep.py
#
# A very simple coroutine

def grep(pattern):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        if pattern in line:
            print line,

# Example use
if __name__ == '__main__':
    g = grep("python")
    g.next()
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")

#__________________________________________________________
# coroutine.py
#
# A decorator function that takes care of starting a coroutine
# automatically on call.

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

# Example use
if __name__ == '__main__':
    @coroutine
    def grep(pattern):
        print "Looking for %s" % pattern
        while True:
            line = (yield)
            if pattern in line:
                print line,

    g = grep("python")
    # Notice how you don't need a next() call here
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
#__________________________________________________________
# cofollow.py
#
# A simple example showing how to hook up a pipeline with
# coroutines.   To run this, you will need a log file.
# Run the program logsim.py in the background to get a data
# source.

from coroutine import coroutine

# A data source.  This is not a coroutine, but it sends
# data into one (target)

import time
def follow(thefile, target):
    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         target.send(line)

# A sink.  A coroutine that receives data

@coroutine
def printer():
    while True:
         line = (yield)
         print line,

# Example use
if __name__ == '__main__':
    f = open("access-log")
    follow(f,printer())