def find_product(l):

	# Imperative programming Way ----->>>>>>>>> Imperative programming -->> do one by one, line by line, convert data in a local view
	# brute force  O(n^2)
	# max = 0
	# maxIndex = 0
	# length = len(l) - 5
	# for i in range(length):
	# 	max5 = 1
	# 	for j in range(5):
	# 		max5 = max5 * l[i+j]
	# 	if max < max5:
	# 		max = max5
	# 		maxIndex = i
	# return maxIndex, max

	# Functional Programming Way ----->>>>> Funtional Programming ---> different ways of thinking ---> convert data in a global view

	#step 0 get valid range
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

list = [1,3,4,6,8,9,2,5,9,7,5]

print find_product(list)


arr = [[1,2,3,5,6],
	   [2,5,7,8,9],
	   [2,6,7,8,9],
	   [2,5,10,8,9],
	   [2,5,7,8,3],]

print arr[:len(arr)]

print map(lambda list: reduce(lambda x,y: x + y, list), arr[:len(arr)])

import numpy as np

print np.sum(arr, axis = 1)


print [arr[i][j] if j == i else 0 for i in range(len(arr)) for j in range(len(arr))]

print [[arr[i][j] for j in range(len(arr))] for i in range(len(arr))]

print [arr[i][j] for i in range(len(arr)) for j in range(len(arr))]

print [sum([arr[i][j] for j in range(len(arr))]) for i in range(len(arr))]
