# #set
# documentIds = set({})
# #list
# wordIds = []
# #dictionary 
# dict = {}
# #convert from wordId to wordStr
# wordIdToStr = {}
# #convert from docId to docStr
# docIdToStr = {}

# #open urls.txt
# test = open("urls.txt","r")

# for line in test.readlines():
# 	lineStrip = line.strip()
# 	# documentIds = document_id(self,lineStrip)
# 	documentIds.add(lineStrip)
# print documentIds

# test.close()
# import signal
# import time
# import sys
# def signal_handler(signal, frame):
#         print('You pressed Ctrl+C!')
#         sys.exit(0)
# signal.signal(signal.SIGINT, signal_handler)
# print('Press Ctrl+C')
# signal.pause()

# while True:
#     # task
#     if handler.SIGINT:
#         break

# MaxVal = 10000000
# StepInterval = 10

# try:
#    print "hhh"
# except KeyboardInterrupt:
#    print "out"
# finally:
# 	print "in"

# print "done"

# import re

# keywords = "a+b++c+++d+++++++++d "
# # keywords = "a b     a    b"

# print re.sub('(\+)+',' ',keywords)

# re.sub
#!/usr/bin/python


# store submit in json form in a file
# @route('/', method='POST')
# def default():
#     json_text = request.json
#     with open('/path/to/file', 'wb') as f:
#         f.write(json_text)
#     return 'My first bottle program.'


# import sqlite3

# conn = sqlite3.connect('test.db')

# conn.execute("CREATE TABLE IF NOT EXISTS dummyTable(value TEXT,id INTEGER PRIMARY KEY);")

# # a = 0
# # b = 'str'

# # conn.execute("INSERT INTO dummyTable (value,id) VALUES(?,?)",(b,a))
# # conn.execute("INSERT INTO dummyTable (id,value) VALUES(null,'two')")
# # conn.execute("INSERT INTO dummyTable (id,value) VALUES(null,'three')")

# # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# cursor = conn.execute("SELECT value,id from dummyTable")
# for row in cursor:
#    print "ID = ", row[0]
#    print "VALUE = ", row[1]

# print "Operation done successfully";

# conn.close()

# sort = [2,34234235,24234234,12312312312,23434]

# print sorted(sort,reverse = True)

# def fib(n,l):
# 	if n == 0 or n == 1:
# 		l.append(n) 
# 	else:
# 		l.append(fib(n-1,l)+fib(n-2,l))
# 	return l[n]
# list = []


# print fib(6,list)

# def fib(n, lookup):

# 	# Base case
# 	if n == 0 or n == 1 :
# 		lookup.append(n)

# 	# If the value is not calculated previously then calculate it
# 	if lookup[n] is None:
# 		lookup.append(fib(n-1 , lookup) + fib(n-2 , lookup))

# 	# return the value corresponding to that value of n
# 	return lookup[n]
# # end of function

# lookup = [None]*11

# print fib(6,lookup)
# print lookup

# def prime_factors_generate(n):
#     a = []
#     prime_list = sorted(primes())
#     pindex = 0
#     p = prime_list[pindex]
#     num = n
#     while p != num:
#         if num % p == 0:
#             a.append(p)
#             num //= p
#         else:
#             pindex += 1
#             p = prime_list[pindex]
#     return a

# print prime_factors_generate(6
# def primes(n):
#     primfac = []
#     primfac.append(1)
#     d = 2
#     while d*d <= n:
#         while (n % d) == 0:
#             primfac.append(d)  # supposing you want multiple factors repeated
#             n //= d
#         d += 1
#     if n > 1:
#        primfac.append(n)
#     return primfac

# print primes(11)
# import re, collections, Cookie, signal, sys, os
# import sqlite3
# sys.path.insert(0,'bottle/')
# from bottle import route, run, template, static_file, get,post, request, response, redirect, error
# from operator import itemgetter, attrgetter

# keywords = ""
# keyList = keywords.split(' ')
# print keywords
# print keyList

# import os

# key_pair_name = 'key_pair_test1'
# try:
# 	os.system("rm -f %s" % key_pair_name+'.pem')
# except:
# 	print "hhh"


# import re, collections, Cookie, signal, sys, os
# import sqlite3
# sys.path.insert(0,'bottle/')
# import bottle
# from bottle import route, run, template, static_file, get,post, request, response, redirect, error
# from operator import itemgetter, attrgetter
# sys.path.insert(0,'beaker/')
# from beaker.middleware import SessionMiddleware

# session_opts = {
#     'session.type': 'file',
#     'session.cookie_expires': 300,
#     'session.data_dir': './data',
#     'session.auto': True
# }

# app = SessionMiddleware(bottle.app(), session_opts)

# @route('/',method = "GET")
# def index():
# 	s = bottle.request.environ.get('beaker.session')
# 	s['email'] = 'boqian'
# 	s['photo'] = 'asdas'
# 	s.save()
# 	#safari
# 	#1508333167.53212

# 	#chrome
# 	#1508333206.857031
# 	print s

# @route('/test',method = "GET")
# def another():
# 	s = bottle.request.environ.get('beaker.session')
# 	s['email'] = 'lishishuo'
# 	s.save()
# 	print s

# run(host='localhost', port=8082, debug = True, app = app)

# import redis

# r_server = redis.Redis("localhost",'6379')
# r_server.set("frank","1")

# key = []
# if key == []:
# 	print "adsas"

# print len([1,2,3,4,5,6])%5

# key = {}
# if key == {}:
# 	print 'asdas'


# print ~~(16/5)

# list = ["1asd",'2asdasd','3','4','5','6']
# print list[0:6]

# import anydbm

# db = anydbm.open('captions.db','c')

# print 43%15

print (12.123%1)

print (2000&1)

list = ['1','3','5']

arr = list[:]

print arr

matrix = [[1 ,0 ,0] , [0,1,0], [0 ,0 ,1]]
print matrix [0][1]

print "False"

if None:    # String is always True, only None is False
	pass
else:
	print 'asdas'

as_list = [("key1", 1), ("key2", 2), ] 
print {k:v for k, v in as_list}

print ",".join(list)

print type(letter for letter in list)

print type(list[:])
print type(list)

print list is list[:]

print zip([10,2],[3,4],[5,6])

a = b = c = range(20)
print zip(a,b,c)

del a[::]
print a

arr = [3,]
print len(arr)
del arr[:]  # Deletes all the elements in the array
del arr # Deletes the array itself

print ",".join("frank")

jiji = [1,2]
print type(jiji)

for _ in range(8):
	print _

ls = range(2)
print [ls.append(ls[-2] + ls[-1]) or ls[-2] for _ in range(8)]

#print ls.append(ls[-2])

print [x + 1 for x in xrange(20)]

print range(20)

parts = [[part for part in str(x).split(".")] for x in [10.55, 19.11]]

print parts

parts = zip(*parts)

print parts

parts = zip(*parts [0]) + zip(*parts [1])

print parts

parts = [str(int(a) + int(b)) for a, b in parts]

print parts

print float("".join(parts[:2]) + "." + "".join(parts[2:]))


a = (1,3)
b = (2,4)
print a+b

arrayList = [1,4,5,6,2,5,6]

print arrayList[:-1]