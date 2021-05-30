# one command cloud enter script

import os

key_pair_name = 'key_pair_test3'

file = open('ip_instanceid.txt','r')

public_ip = file.read().split()[1]

print 'Cloud Entering...'

os.system('ssh -o StrictHostKeyChecking=no -i '+ key_pair_name +'.pem'+ ' ubuntu@' + public_ip)

print 'Successfully exit cloud...'