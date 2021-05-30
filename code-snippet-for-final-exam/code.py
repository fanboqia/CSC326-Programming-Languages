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

#Generally speaking, a closure is a structure (code blocks, function object, callable object, etc.) storing a function together with an environment. The environment here means information about free variables that function bounded, especially values or storage locations of free variables.