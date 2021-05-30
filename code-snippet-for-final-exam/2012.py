#Q3
def palidrome(s):
    a=list(s)
    a.reverse()
    if a==list(s):
        return True
    else:
        return False

print palidrome("aba")
print palidrome("abacd")
print palidrome("abacdcaba")

def palindrome(s):
    m=reduce(lambda a,b:b+a,s)
    return m==s


print palindrome("aba")
print palindrome("abacd")
print palindrome("abacdcaba")

#Q6
def func(A):
    result=[]
    for e in A:
        result+=[e*e]
    return result

from numpy import *
def func_a(a):
    a=array(a)
    return list(a**2)
def func_f(a):
    return map(lambda x:x**2,a)

print func([1,2,3,4,5])
print func_a([1,2,3,4,5])
print func_f([1,2,3,4,5])