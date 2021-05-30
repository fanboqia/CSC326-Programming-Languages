import os
import redis
import pickle
import pprint

r_server = redis.Redis("localhost",'6379')
print "waiting for crawling..."
os.system('python crawler.py')
print "crawling finished..."

stuff = pickle.loads(r_server.get('pageRank_Score'))
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

# print pickle.loads(r_server.get('pageRank_Score'))