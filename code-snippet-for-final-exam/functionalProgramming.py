# # utility function for "identity with side-effect"
# def monadic_print(x): 
# 	print x 
# 	return x
# # FP version of "echo()"
# echo_FP = lambda: monadic_print(raw_input("FP -- ")) !='quit' and echo_FP()
# echo_FP()

#a = lambda x,y : x*y*c

#print type({1,2,3,4,5,})

#--- Functional Python code for "print big products" ----#
A  =  [1,2,4,5,6,7,8,89]
bigmuls = filter(lambda x: x > 2, A)
print bigmuls
# combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
# dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
# print bigmuls((1,2,3,4),(10,15,3,22))

# def add1(n) : return n+1

# def add2(n) : return n+2

# def compose(a,b) : return lambda n : b(a(n))

# add3 = compose(add1,add2)

# print add3(1)


# def profile(fn):
# 	def frank(*args,**kwargs):
# 		print 'enter...'
# 		print args
# 		print kwargs
# 		return fn(*args,**kwargs)
# 	return frank

# @profile
# def james(n = 2):
# 	print n**2
# james()

# regular binomial
def bernoulli( p ) :
 return { 0:p, 1:1-p }
def sample( dist ) :
 return dist.values()
def binomial() :
 a = sample(bernoulli(0.5))
 b = sample(bernoulli(0.5))
 c = sample(bernoulli(0.5))
 return (a, b, c)
def explore_first( comp ) :
 return comp()
x = explore_first( binomial )
print x
