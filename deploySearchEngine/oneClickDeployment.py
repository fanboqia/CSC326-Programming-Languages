import sys
import os
sys.path.insert(0,'boto/')
import boto
import boto.ec2
import boto.ec2.connection
import time
import socket
import signal
sys.path.insert(0,'paramiko/')
import paramiko

# import threading

key_pair_name = 'key_pair_test3'
SecurityGroupName = 'csc326-group27'
ACCESS_KEY_ID = ''
SECRET_ACCESS_KEY = ''
AMI = 'ami-xxxxxxx'
ip = '34.237.131.228'
dns = ''
insId = ''


# get access to the aws cloud services 
def connect():

	'''step 0 get the user specified aws credential from a txt file'''

	file = open('credentialAWS.txt','r')
	lines = file.read()
	content = lines.split()

	#print content
	global ACCESS_KEY_ID
	global SECRET_ACCESS_KEY
	ACCESS_KEY_ID = content[1]
	SECRET_ACCESS_KEY = content[3]

	try:
		connObj = boto.ec2.connect_to_region('us-east-1',aws_access_key_id = ACCESS_KEY_ID, aws_secret_access_key = SECRET_ACCESS_KEY)
	except Exception as e:
		print "________Exception from connection_______--> ", e
	return connObj


# multiple steps to deploy an instance on aws cloud
def deploy():
	global ip
	global dns
	global insId
	# print ACCESS_KEY_ID
	# print SECRET_ACCESS_KEY

	print '''********The whole deployment may take 5 minutes...you can play your phone or stare at the screen ^_^ ~~~'''

	'''Step1'''
	# connect to us-east-1 with aws_access_key_id and aws_secret_access_key
	connObj = connect()

	'''Step2'''
	# create key pair
	try:
		# delete previous key_pair_test file first 
		os.system("rm -f %s" % key_pair_name+'.pem')
		key_pair = connObj.create_key_pair(key_pair_name)
		key_pair.save('.')
	except Exception as e:
		print "________Exception from key pair--> ", e

	'''Step3'''
	# create security group
	try:
		security_group = connObj.create_security_group(SecurityGroupName, 'mySecurityGroup')
		connObj.authorize_security_group(group_name=security_group.name, ip_protocol='icmp', from_port=-1, to_port=-1, cidr_ip='0.0.0.0/0')
		connObj.authorize_security_group(group_name=security_group.name, ip_protocol='tcp', from_port=22, to_port=22, cidr_ip='0.0.0.0/0')
		connObj.authorize_security_group(group_name=security_group.name, ip_protocol='tcp', from_port=80, to_port=80, cidr_ip='0.0.0.0/0')
	except Exception as e:
		print "________Exception from Security Group--> ", e

	'''Step4'''
	# run the instances
	try:
		reserve = connObj.run_instances(image_id  = AMI, key_name = key_pair_name, security_groups = [SecurityGroupName], instance_type = 't1.micro')
		
		# instanceStatus = connObj.get_all_instance_status(instance_ids=reserve.instances)	
		# for ins in instanceStatus:
		# 	print "_______instance status_________:", ins

		for instance in reserve.instances:
			print "________Instance state__________: ",instance.state
	except Exception as e:
		print "________Exception from instance--> ", e

	'''Once the state of the instance is changed to "running", 
	    you can access your instance with the key-pair generated 
	    in step 1 with the following command $ ssh -i key_pair.pem ubuntu@<PUBLIC-IP-ADDRESS>
	    Note that the default user name for the Ubuntu AMIs is "ubuntu". The public IP address
		of the instance can be found with boto.ec2.instance.Instance.ip_address'''
	# suspend the program until state becomes running	
	while reserve.instances[0].update() != 'running':
			time.sleep(2)

	print "state of the instance is now running!"			

	'''To copy a file from your local machine to the AWS instance, you may use the following command.
			scp -i key_pair.pem <FILE-PATH> ubuntu@<PUBLIC-IP-ADDRESS>:~/<REMOTE-PATH>'''

	'''Setup static IP address'''

	print "waiting for setup static IP address..."

	try:
		# address = connObj.allocate_address()
		# address.associate(instance_id = reserve.instances[0].id)
		connObj.associate_address(reserve.instances[0].id, None, 'eipalloc-02cfae36')
	except Exception as e:
		print "________Exception from address--> ", e

	print  "Address_Ip: " , ip
	print  "instanceId: ", reserve.instances[0].id
	#print  "Public_DNS_Name: ", reserve.instances[0].public_dns_name

	#dns = reserve.instances[0].public_dns_name
	insId = reserve.instances[0].id

	file = open('ip_instanceid.txt','w')
	file.write('IP ' + ip + ' instanceId ' + insId)

	return ip,insId


# this function copies local key pair to the cloud and deploy in the following step
def cloudInitialization():
	file = open('ip_instanceid.txt','r')
	global key_pair_name
	print '''****** Waiting for the initialization of the AWS Cloud Server...Normally takes at least 1 minute ******'''
	
	# for instance in connect().get_all_instance_status()
	while connect().get_all_instance_status()[0].system_status.status != 'ok' and connect().get_all_instance_status()[0].instance_status.status != 'ok':
		time.sleep(2)

	print 'status check: ' + connect().get_all_instance_status()[0].system_status.status + '/' + connect().get_all_instance_status()[0].instance_status.status

	# print 'check port 22 connection...'

	# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# try:
	# 	s.connect((ip, 22))
	# 	print "Port 22 reachable"
	# except socket.error as e:
	# 	print "Error on connect: %s" % e
	# 	s.close()
	# 	cloudInstruction()

# execute remote script from local machine
def cloudExecution():

	print "start to upload deploy file to the cloud..."
	os.system('scp -i '+ key_pair_name +'.pem -o StrictHostKeyChecking=no cloudDeploy.py ubuntu@'+ ip +':~/')

	print '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@   The cloud execution normally takes at least 2 minute...Please wait...   @\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''

	print """After 2 minutes you can access the ip address 34.237.131.228 """
	print '''@@@@@@@ ATTENTION @@@@@@@ The program won't stop, therefore you have to close the terminal'''
	print 'You can also terminate the instance by \'python terminator.py\', then enter the instance id...'
	print 'Good Luck!!!'

	k = paramiko.RSAKey.from_private_key_file(key_pair_name + '.pem') # must be in your current dir
	c = paramiko.SSHClient()
	c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	c.connect( hostname = ip, username = "ubuntu", pkey = k )

	commands = ["sudo python cloudDeploy.py", "exit"] # these commands will exec in series

	for command in commands:
		print "Executing {}".format( command )
		stdin , stdout, stderr = c.exec_command(command) # this command is executed on the *remote* server
		print stdout.read()
		print( "Errors" + stderr.read())


	c.close()

##################################################################__________MAIN_________ ###############################################################################################

deploy()

cloudInitialization()

def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
#150 SECONDS SHOULD BE ENOUGH TO DEPLOY ON CLOUD
signal.alarm(150)   # interrupt in 150 seconds to exit from the cloud
try:
    cloudExecution()
except Exception, msg:
    print "Everything is doing well..."

print 'oneClickDeployment finished....'
print 'You can now start to access the website: ', ip
print 'You can also terminate the instance by \'python terminator.py\', then enter the instance id...'
print 'Good Luck!!!'
# threading.Thread(target=cloudInstruction()).start()