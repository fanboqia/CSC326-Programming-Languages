import math

def Q(D):
	z = []
	if D == None:
		return 'empty list takes no value'
	for num in D:
		if num < 0:
			print 'negative number has no real value...'
			continue
		num = int(math.sqrt(2*num *50/30))
		z.append(num)
	return z

print Q([100,150,180])
