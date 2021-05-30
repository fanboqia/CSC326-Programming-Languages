# import json

# file = open('csc326project/client_secrets_localHost.json','r')
# words = file.read()
# pythonObj = json.loads(words)
# redirect_uri = str(pythonObj['web']['redirect_uris'][0])
# client_id = str(pythonObj['web']['client_id'])
# client_secret =  str(pythonObj['web']['client_secret'])

# print str(pythonObj['web']['javascript_origins'][0])
# print redirect_uri
# print client_id
# print client_secret

# import paramiko
# import os
# os.system("scp -i key_pair_test3.pem cloudDeploy.py ubuntu@ec2-*****.compute-1.amazonaws.com");
# k = paramiko.RSAKey.from_private_key_file("key_pair_test3.pem") # must be in your current dir
# c = paramiko.SSHClient()
# c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# c.connect( hostname = "ec2-*****.compute-1.amazonaws.com", username = "ec2-user", pkey = k )

# commands = [ "sudo pip2.7 install some-library", "cd my_code/frontend", "sudo python2.7 frontend.py &"] # these commands will exec in series

# for command in commands:
#     print "Executing {}".format( command )
#     stdin , stdout, stderr = c.exec_command(command) # this command is executed on the *remote* server
#     print stdout.read()
#     print( "Errors")
#     print stderr.read()

# c.close()

# import threading

# def worker(num):
#     """thread worker function"""
#     print 'Worker: %s' % num
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()

# import time

# second = 0

# while second != 120: 
# 	time.sleep(1)
# 	second += 1
# 	print second

