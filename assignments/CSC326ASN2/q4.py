# import os

# def find_popular(filename):
# 	f = open(filename)
# 	#print f.peek()
# 	f.seek(0, os.SEEK_END)
# 	size = f.tell()
# 	print size
# 	f.seek(0,0)
# 	print f
# 	wordList = []
# 	wordFrequency = {}
# 	word = ''
# 	currSpacePos = 0
# 	lastSpacePos = 0

# 	for line in f:
# 		print line
			
wordFrequency = {}
wordList = []

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