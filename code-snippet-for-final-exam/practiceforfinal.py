class point:
	counter = 0
	def __new__():
		pass

	def __add__():
		pass
   	def __radd__(self,other):
   		return self.__add__(other)

   	def __cmp__():
   		pass

	def __del__(self):
		print 'youyouyou', self
		point.counter = point.counter + 1
		print point.counter

	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return '(x: %d y: %d z: %d)' %(self.x,self.y,self.z)

	def __eq__(self,other):
		distance = ((self.x**2) + (self.y**2) + (self.z**2))**0.5
		otherDis = ((other.x**2) + (other.y**2) + (other.z**2))**0.5
		if distance == otherDis:
			return True
		else:
			return False

	def __lt__(self, other):
		distance = ((self.x**2) + (self.y**2) + (self.z**2))**0.5
		otherDis = ((other.x**2) + (other.y**2) + (other.z**2))**0.5
		if distance > otherDis:
			return False
		else:
			return True

a = point(1,2,4)

# Meta Class

def class_with_method(func):
	class frank: pass
	setattr(frank, func.__name__, func)
	return frank

def say_foo(self): print 'foo'
Foo = class_with_method(say_foo)
foo = Foo()
foo.say_foo()

#
from new import classobj
Foo2 = classobj(’Foo2’,(Foo,),{’bar’:lambda self:’bar’})
Foo2().bar()
Foo2().say_foo()


class ChattyType(type):
...     def __new__(cls, name, bases, dct):
...         print "Allocating memory for class", name
...         return type.__new__(cls, name, bases, dct)
...     def __init__(cls, name, bases, dct):
...         print "Init’ing (configuring) class", name
...         super(ChattyType, cls).__init__(name, bases, dct)

X = ChattyType(’X’,(),{’foo’:lambda self:’foo’})


#decorator

def elementwise(fn):
    def newfn(arg):
        if hasattr(arg,’__getitem__’):  # is a Sequence
            return type(arg)(map(fn, arg))
        else:
            return fn(arg)
return newfn
@elementwise
def compute(x):


def trace( aFunc ):
    """Trace entry, exit and exceptions."""
    def loggedFunc( \*args, \*\*kw ):
        print "enter", aFunc.__name__
        try:
            result= aFunc( \*args, \*\*kw )
        except Exception, e:
            print "exception", aFunc.__name__, e
            raise
        print "exit", aFunc.__name__
        return result
    loggedFunc.__name__= aFunc.__name__
    loggedFunc.__doc__= aFunc.__
    return loggedFunc


# persistent
def walk(dir) :
    for name is os.listdir(dir) :
        path = os.path.join( dir, name )
        if os.path.isfile(path) :
           print path
        else
walk(path)

# array
a = np.array( [1]*10 )
>>> np.add.accumulate( a )
array([1, 2, 3, 4, 5, 6, 7, 8, 9,10])


#hhhhhhhh
ITERATIONS = 100
DENSITY = 1000 # warning: execution speed decreases with square of DENSITY
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5
x, y = np.meshgrid(np.linspace(x_min, x_max, DENSITY),
                   np.linspace(y_min, y_max, DENSITY))
c = x + 1j*y # complex grid
z = c.copy()
fractal = np.zeros(z.shape, dtype=np.uint8) + 255
for n in range(ITERATIONS):
    print "Iteration %d" % n
    # --- Uncomment to see different sets ---
    # Tricorn
    # z = z.conj()
    # Burning ship
    # z = abs(z.real) + 1j*abs(z.imag)
# ---
    # Leave the lines below in place
z *= z z += c
    mask = (fractal == 255) & (abs(z) > 10)
    fractal[mask] = 254 * n / float(ITERATIONS)


#second column
b[:,1]
b[1:3,:]