def foo():
	for i in range(10):
		yield i 

gen = foo()

print gen.next() == 0

print gen.next() == 2

print gen.next() 


# class A(object):
# 	pass
# class B(A):
# 	pass
# class C(B):
# 	pass


# a = A()
# b = B()
# c = C()
# l = []

# print isinstance(a, A)
# print isinstance(c, A)
# print issubclass(B,A)
# print isinstance(B,A)
# print isinstance(c, A)
# print isinstance(l, object)
# print isinstance(c, object)
# print 'object', isinstance(A, object)
# print 'asdasdasdas', isinstance(A, type)
# print 'subclass', issubclass(A, type)
# print isinstance(A,B)
# print 'asdasdasdas', isinstance(C, type)
# print '123', isinstance(a, type)




# print type.__doc__
# print object.__doc__
# print A.__doc__


#imperative programming note 
# By value: == !=
# By reference: is

# from numpy import *

# a = arange(10).reshape(2,5)

# print 'shape: ', a.shape
# print 'ndim: ', a.ndim
# print 'matrix: ', a
# print a.dtype.name
# print a.itemsize
# print a.size

# print array([(1,2,4),(2,3,5)])  # tuple row
# print zeros((3,5))
# print ones((1,2))
# print empty((2,3))   # random 

# print arange(10,30,5)
# print linspace(0,2,9)
# x = linspace(0,2*pi, 100)
# print sin(x)
# print random.random((2,3))
# print a.ravel()   #flatten 2d array
# a.shape = (5,2)
# print a.transpose()
# a.resize((5,2))
# print a
# a.reshape(2,-1)
# print a 



