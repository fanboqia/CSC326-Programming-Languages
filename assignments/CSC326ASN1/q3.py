
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