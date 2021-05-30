import os

print 'waiting for cloning current project from github to cloud...'

try:
		os.system('sudo apt-get update')
		os.system('sudo apt-get install -y git')
		os.system('sudo apt-get install -y python-dev')
		os.system('sudo git clone https://github.com/fanboqia/csc326project.git')
		# os.system('sudo git clone git@github.com:fanboqia/csc326SearchEngine.git')
except Exception as e:
		print '________Exception from cloning project-->', e

print 'successfully cloned project from github...'

os.chdir('csc326project')

print 'Start to download necessary libraries...'

try:
		os.system('sudo apt-get install -y python-pip')
		os.system('sudo pip install redis')
		os.system('sudo apt-get install -y python-numpy')
		os.system('sudo apt-get install -y redis-server')
		os.system('sudo redis-server&')
except Exception as e:
		print '________Exception from downloading libraries-->', e

print 'successfully downloaded necessary libraries...'

print 'Start to crawl information from targeted websites...'

try:
		os.chdir('crawler')
		os.system('sudo python crawler.py')
except Exception as e:
		print '________Exception from crawling-->', e

print 'successfully crawled website information...'

print 'Start to activate bottle web server...'

try:
		os.chdir('..')
		os.system('screen -dm sudo python searchEngineAWS.py')
		#os.system('screen -dm sudo python searchEngineAWS.py')
except Exception as e:
		print '________Exception from server-->', e	

print 'Server Successfully deployed!!!'

os.system('exit()')