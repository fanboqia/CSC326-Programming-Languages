from time import clock

#when flag is True, execute decorator attribute
PROFILE_FUNCTIONS = True
#{funcName:(average runtime, # of function calls)}
PROFILE_RESULTS = dict()

def profile(function):
  if PROFILE_FUNCTIONS == True:
	def wrapper(*args, **kwargs):
		start = clock()
		function(*args,**kwargs)
		duration = clock() - start
		if function.__name__ not in PROFILE_RESULTS:
			PROFILE_RESULTS[function.__name__] = [duration, 1]
		else:
			PROFILE_RESULTS[function.__name__][0] = PROFILE_RESULTS[function.__name__][0] + duration
			PROFILE_RESULTS[function.__name__][1] = PROFILE_RESULTS[function.__name__][1] + 1
		return PROFILE_RESULTS
	return wrapper
  else:
  	return function

@profile
def foo():
	print "hhhh"

@profile
def foo1():
	print "asdas"

foo()
foo()
foo()
foo()
foo1()
foo1()
foo()
foo1()
foo1()


# always put these two operations at the bottom of the program to make it functional
# calculate the average runtime over all the calls, after all the function calls
for key in PROFILE_RESULTS:
	PROFILE_RESULTS[key][0] = PROFILE_RESULTS[key][0] / PROFILE_RESULTS[key][1]
# transform the list data structure to tuple data structure (to read only)(according to the requirement of the handout)
for key in PROFILE_RESULTS:
	PROFILE_RESULTS[key] = tuple(PROFILE_RESULTS[key])

print PROFILE_RESULTS



